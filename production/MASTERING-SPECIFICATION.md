# Mastering Specification

**Current status: NOT MASTERED.** The stored WAV is a short sine-wave proof render, not a finished commercial master.

## Executable processing

`tools/master.py` provides a reproducible FFmpeg two-pass EBU R128 loudnorm workflow. It preserves the premaster, measures it, applies measured loudness normalization, exports 24-bit PCM WAV at 48 kHz by default, and records input/output SHA-256 hashes and first/final-pass loudnorm data.

Default starting targets: -14 LUFS integrated, -1 dBTP, 11 LU LRA. These are configurable and are not universal mastering targets. Choose targets for the actual genre, dynamics, and delivery specification. The script does not apply creative EQ, saturation, stereo widening, or reverb.

Example:

```sh
python3 tools/master.py renders/wav/returning-light-demo.wav \
  --out renders/wav/returning-light-demo-master.wav
```

Requires FFmpeg and ffprobe. The workflow must be run on a real premaster; the existence of the script is not evidence that a master has been produced.

## Required master records

- Track ID and arrangement revision
- Premaster filename and SHA-256
- Sample rate and bit depth
- Integrated loudness (LUFS-I)
- Loudness range (LRA), when useful
- Maximum sample peak and true peak (dBTP)
- Clipping / inter-sample peak inspection
- Stereo correlation / mono compatibility
- Noise, clicks, fades, and tail inspection
- Mastering chain, plugin versions, and settings
- Final output filename, format, SHA-256
- Engineer/reviewer and date

## Human engineering and approval

After automated loudness processing, a human engineer must audition the premaster and export, assess tonal balance, transient integrity, low-frequency balance, stereo image, phase, noise, clicks, fades, and translation, and record any corrective EQ/dynamics decisions. The automated report does not claim those checks have passed.

A final master is not publicly distributable until rights review and exact-hash listening approval are complete.
