# Release Production — Separate from Rendering

**Current release state: PRIVATE / NOT APPROVED FOR PUBLICATION.**

## Required sequence
1. Composition and contributor credits finalized.
2. Rights review completed for every asset.
3. Final arrangement and source revision frozen.
4. Premaster rendered and preserved.
5. Mastering performed; final WAV and measurement report stored.
6. Technical validation and checksums recorded.
7. Human listening review approved against the exact master hash.
8. Metadata, artwork, credits, territory, date, and explicit-content fields checked.
9. Human release approver signs the release record naming exact asset hashes and destination.
10. Build the export ZIP from the explicit allowlist in `PUBLIC-DISTRIBUTION-SELECTION.json`.
11. Copy only approved files to the named public destination.
12. Verify the published listing and record its URL.

## Mastering

Run the manual `Master and store release candidate` workflow on main, or use `tools/master.py` locally. The script requires FFmpeg/ffprobe, preserves the premaster, applies two-pass EBU R128 loudnorm, exports 24-bit PCM WAV, and writes a SHA-256 measurement report. Automated loudness processing is not a substitute for creative engineering or listening review.

## File selection and packaging

- Allowlist: `release/PUBLIC-DISTRIBUTION-SELECTION.json`
- Policy: `release/PUBLIC-DISTRIBUTION.md`
- Builder: `tools/package_release.py`

The builder refuses to create a ZIP while any required approval gate is pending or any required file is missing. `--allow-pending` prints a diagnostic report only and cannot create a distributable package.

## Storage
- Candidate audio: renders/wav/
- MIDI: renders/midi/
- Stems: renders/stems/
- Render and mastering receipts: renders/receipts/
- Mastering reports: adjacent to mastered WAVs
- Rights evidence index: evidence/rights/
- Listening records: evidence/listening/
- Human release approvals: evidence/approvals/
- Final package manifest: release/

Do not commit private contracts, personal data, credentials, or confidential third-party evidence. Main-branch storage is still private storage.

No automatic workflow may publish to streaming services or public repositories. Never make the production repository public as a shortcut: that would expose its entire file tree and history.
