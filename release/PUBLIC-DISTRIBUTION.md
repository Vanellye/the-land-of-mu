# Public Distribution Selection

This file defines a narrow export set. It does not make this production repository public and does not authorize publication.

## Selected package

The machine-readable selection lives in `PUBLIC-DISTRIBUTION-SELECTION.json`. The current WAV is a sine-oscillator render test. It is not eligible as a final master. The selected final-master path is reserved for the output of `tools/master.py`.

## Mastering

Example:

```sh
python3 tools/master.py renders/wav/returning-light-demo.wav \
  --out renders/wav/returning-light-demo-master.wav
```

The script requires FFmpeg/ffprobe, preserves the premaster, performs two-pass EBU R128 loudness processing, exports 24-bit PCM WAV, and writes a JSON measurement report beside the output. Targets can be overridden for the actual destination. The defaults are not a substitute for genre- and platform-specific engineering judgment.

## File selection rules

- Include only paths explicitly listed in the selection manifest.
- Require a final master and its matching report.
- Include MIDI only if its rights and intended distribution are confirmed.
- Include artwork and complete credits/metadata only after review.
- Exclude source arrangements, private evidence, credentials, internal notes, and unrelated repository history.
- Verify SHA-256 hashes after copying to the destination.

## Publication gates

Publication remains blocked until rights review, mastering review, exact-hash human listening approval, metadata/artwork review, and explicit human release authorization are recorded. No CI workflow publishes externally.

The repository remains private. Making it public is a separate visibility change that would expose the repository's files and history; use a dedicated export repository or distributor upload containing only approved assets.
