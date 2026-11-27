# Mastering Specification

**Current status: NOT MASTERED.** The starter renderer is a sine-wave proof renderer; its output is not a finished commercial master.

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

## Mastering approach
1. Preserve an unprocessed high-resolution premaster.
2. Select loudness and peak targets for the actual genre and destination.
3. Use corrective EQ and dynamics only where listening and measurement justify them.
4. Check transient integrity, low-frequency balance, stereo image, phase, and translation.
5. Render distribution masters at required sample rate and bit depth.
6. Read back and re-measure exports.
7. Store measurement report and final hashes in renders/receipts/.

The current renderer does not include EQ, compression, limiting, true-peak oversampling, loudness normalization, dithering, or mastering measurements. A successful render smoke test is not evidence of mastering completion.
