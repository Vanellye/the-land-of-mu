#!/usr/bin/env python3
"""Render arrangement JSON to PCM WAV and Standard MIDI File (format 0).

This transparent starter renderer uses a sine oscillator per note event.
It validates the pipeline; it is not a sampled-instrument or mastering engine.
"""
from __future__ import annotations
import argparse
import hashlib
import json
import math
import struct
import sys
import wave
from array import array
from datetime import datetime, timezone
from pathlib import Path

VERSION = "0.1.0"


def vlq(value: int) -> bytes:
    value = max(0, int(value))
    buffer = value & 0x7F
    out = bytearray()
    while True:
        value >>= 7
        if not value:
            break
        buffer <<= 8
        buffer |= (value & 0x7F) | 0x80
    while True:
        out.append(buffer & 0xFF)
        if buffer & 0x80:
            buffer >>= 8
        else:
            break
    return bytes(out)


def midi_file(data: dict) -> bytes:
    ppq = 480
    tempo = int(60_000_000 / float(data["tempo_bpm"]))
    events = [(0, b"\xff\x51\x03" + tempo.to_bytes(3, "big"))]
    for n in data["notes"]:
        start = round(float(n["start_beats"]) * ppq)
        end = round((float(n["start_beats"]) + float(n["duration_beats"])) * ppq)
        pitch = int(n["pitch"])
        velocity = int(n.get("velocity", 90))
        events.append((start, bytes([0x90, pitch, velocity])))
        events.append((end, bytes([0x80, pitch, 0])))
    events.sort(key=lambda item: (item[0], 0 if item[1][0] == 0x80 else 1))
    track = bytearray()
    previous = 0
    for tick, event in events:
        track.extend(vlq(tick - previous))
        track.extend(event)
        previous = tick
    track.extend(b"\x00\xff\x2f\x00")
    header = b"MThd" + struct.pack(">IHHH", 6, 0, 1, ppq)
    return header + b"MTrk" + struct.pack(">I", len(track)) + track


def render_wav(data: dict, path: Path) -> dict:
    sr = int(data.get("sample_rate", 44100))
    channels = int(data.get("channels", 2))
    if int(data.get("bit_depth", 16)) != 16:
        raise ValueError("Starter renderer currently writes 16-bit PCM only.")
    bpm = float(data["tempo_bpm"])
    gain = float(data.get("master_gain", 0.2))
    if not (0.0 <= gain <= 1.0):
        raise ValueError("master_gain must be between 0 and 1.")
    beat_seconds = 60.0 / bpm
    tail = 0.35
    end_beats = max(float(n["start_beats"]) + float(n["duration_beats"]) for n in data["notes"])
    duration = end_beats * beat_seconds + tail
    frames = math.ceil(duration * sr)
    samples = array("h")
    peak = 0
    for i in range(frames):
        t = i / sr
        value = 0.0
        for n in data["notes"]:
            start = float(n["start_beats"]) * beat_seconds
            length = float(n["duration_beats"]) * beat_seconds
            local = t - start
            if 0 <= local < length:
                freq = 440.0 * (2.0 ** ((int(n["pitch"]) - 69) / 12.0))
                attack = min(1.0, local / 0.012)
                release = min(1.0, max(0.0, (length - local) / 0.045))
                velocity = int(n.get("velocity", 90)) / 127.0
                value += math.sin(2.0 * math.pi * freq * local) * attack * release * velocity
        value *= gain / max(1.0, math.sqrt(len(data["notes"]) / 3.0))
        value = max(-0.98, min(0.98, value))
        sample = int(value * 32767)
        peak = max(peak, abs(sample))
        for _ in range(channels):
            samples.append(sample)
    path.parent.mkdir(parents=True, exist_ok=True)
    with wave.open(str(path), "wb") as wf:
        wf.setnchannels(channels)
        wf.setsampwidth(2)
        wf.setframerate(sr)
        wf.writeframes(samples.tobytes())
    return {
        "sample_rate": sr, "channels": channels, "bit_depth": 16,
        "duration_seconds": round(duration, 6), "frames": frames,
        "peak_sample": peak,
        "peak_dbfs": round(20 * math.log10(max(1, peak) / 32767), 3)
    }


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("arrangement", type=Path)
    parser.add_argument("--out", type=Path, required=True, help="Output prefix without extension")
    args = parser.parse_args()
    data = json.loads(args.arrangement.read_text(encoding="utf-8"))
    if not data.get("notes"):
        raise SystemExit("Arrangement must contain at least one note.")
    for n in data["notes"]:
        if not 0 <= int(n["pitch"]) <= 127 or float(n["duration_beats"]) <= 0:
            raise SystemExit(f"Invalid note event: {n}")
    args.out.parent.mkdir(parents=True, exist_ok=True)
    wav_path = args.out.with_suffix(".wav")
    midi_path = args.out.with_suffix(".mid")
    receipt_path = args.out.with_suffix(".render.json")
    wav_stats = render_wav(data, wav_path)
    midi_path.write_bytes(midi_file(data))
    receipt = {
        "receipt_version": "1.0",
        "renderer": "the-land-of-mu/tools/render.py",
        "renderer_version": VERSION,
        "rendered_at": datetime.now(timezone.utc).isoformat(),
        "source_arrangement": str(args.arrangement),
        "track_id": data.get("track_id"),
        "title": data.get("title"),
        "tempo_bpm": data["tempo_bpm"],
        "meter": data.get("meter"),
        "wav": {"file": wav_path.name, "bytes": wav_path.stat().st_size,
                "sha256": sha256(wav_path), **wav_stats},
        "midi": {"file": midi_path.name, "bytes": midi_path.stat().st_size,
                 "sha256": sha256(midi_path), "format": 0, "ppq": 480},
        "validation": {
            "wav_nonempty": wav_path.stat().st_size > 44,
            "midi_header_valid": midi_path.read_bytes()[:4] == b"MThd",
            "midi_track_valid": midi_path.read_bytes()[14:18] == b"MTrk",
            "pcm_peak_below_full_scale": wav_stats["peak_sample"] < 32767
        },
        "limitations": [
            "Sine oscillator proof renderer; not a sampled instrument engine.",
            "No EQ, compression, reverb, loudness normalization, or mastering.",
            "Human listening and rights review are not automated."
        ]
    }
    receipt_path.write_text(json.dumps(receipt, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(receipt, indent=2))
    return 0 if all(receipt["validation"].values()) else 2


if __name__ == "__main__":
    sys.exit(main())
