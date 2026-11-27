#!/usr/bin/env python3
"""Two-pass EBU R128 mastering with FFmpeg loudnorm.

Requires ffmpeg and ffprobe. Keeps the source untouched, writes a new 24-bit
PCM WAV, and records input/output hashes plus loudnorm measurements. Targets
are configurable; defaults are conservative streaming-delivery starting points,
not universal artistic requirements.
"""
from __future__ import annotations
import argparse, hashlib, json, re, shutil, subprocess, sys
from datetime import datetime, timezone
from pathlib import Path

def sha256(path: Path) -> str:
    h=hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda:f.read(1024*1024),b""): h.update(chunk)
    return h.hexdigest()

def run(cmd: list[str]) -> subprocess.CompletedProcess:
    return subprocess.run(cmd,check=True,text=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)

def last_json(stderr: str) -> dict:
    matches=re.findall(r"\{[^{}]*\}",stderr,re.S)
    for item in reversed(matches):
        try:
            obj=json.loads(item)
            if "input_i" in obj and "input_tp" in obj: return obj
        except json.JSONDecodeError: pass
    raise RuntimeError("Could not parse FFmpeg loudnorm first-pass measurements.")

def main() -> int:
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("input",type=Path)
    p.add_argument("--out",type=Path,required=True,help="Output WAV path")
    p.add_argument("--target-i",type=float,default=-14.0,help="Integrated loudness target LUFS")
    p.add_argument("--target-tp",type=float,default=-1.0,help="True-peak ceiling dBTP")
    p.add_argument("--target-lra",type=float,default=11.0,help="Loudness-range target LU")
    p.add_argument("--sample-rate",type=int,default=48000)
    a=p.parse_args()
    if not a.input.is_file(): p.error(f"Input not found: {a.input}")
    if a.input.resolve()==a.out.resolve(): p.error("Output must not overwrite the premaster.")
    if not shutil.which("ffmpeg") or not shutil.which("ffprobe"):
        p.error("ffmpeg and ffprobe are required.")
    a.out.parent.mkdir(parents=True,exist_ok=True)
    filt=f"loudnorm=I={a.target_i}:TP={a.target_tp}:LRA={a.target_lra}:print_format=json"
    first=run(["ffmpeg","-hide_banner","-nostats","-i",str(a.input),"-af",filt,"-f","null","-"])
    measured=last_json(first.stderr)
    second_filter=(f"loudnorm=I={a.target_i}:TP={a.target_tp}:LRA={a.target_lra}:"
      f"measured_I={measured['input_i']}:measured_TP={measured['input_tp']}:"
      f"measured_LRA={measured['input_lra']}:measured_thresh={measured['input_thresh']}:"
      f"offset={measured['target_offset']}:linear=true:print_format=json")
    second=run(["ffmpeg","-y","-hide_banner","-nostats","-i",str(a.input),"-af",second_filter,
      "-ar",str(a.sample_rate),"-c:a","pcm_s24le",str(a.out)])
    final=last_json(second.stderr)
    probe=json.loads(run(["ffprobe","-v","error","-show_entries",
      "stream=codec_name,sample_rate,channels,bits_per_sample,duration","-of","json",str(a.out)]).stdout)
    report={
      "report_version":"1.0","created_at":datetime.now(timezone.utc).isoformat(),
      "tool":"tools/master.py","ffmpeg_version":run(["ffmpeg","-version"]).stdout.splitlines()[0],
      "input":{"file":a.input.name,"sha256":sha256(a.input),"bytes":a.input.stat().st_size},
      "output":{"file":a.out.name,"sha256":sha256(a.out),"bytes":a.out.stat().st_size,"streams":probe.get("streams",[])},
      "targets":{"integrated_loudness_lufs":a.target_i,"true_peak_dbtp":a.target_tp,"loudness_range_lu":a.target_lra},
      "first_pass_measurements":measured,"final_pass_measurements":final,
      "notes":["Two-pass FFmpeg EBU R128 loudnorm processing; no creative EQ, saturation, stereo widening, or reverb is applied.",
       "Loudness targets are delivery starting points; a qualified human engineer must assess artistic balance, translation, phase, noise, fades, and codec behavior.",
       "This report does not establish rights clearance or human listening approval."]
    }
    report_path=a.out.with_suffix(a.out.suffix+".mastering.json")
    report_path.write_text(json.dumps(report,indent=2)+"\n",encoding="utf-8")
    print(json.dumps(report,indent=2))
    return 0 if a.out.stat().st_size>44 else 2

if __name__=="__main__": sys.exit(main())
