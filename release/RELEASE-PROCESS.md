# Release Production — Separate from Rendering

**Current release state: PRIVATE / NOT APPROVED FOR PUBLICATION.**

## Required sequence
1. Composition and contributor credits finalized.
2. Rights review completed for every asset.
3. Final arrangement and source revision frozen.
4. WAV master, MIDI, and requested stems rendered.
5. Technical validation and checksums recorded.
6. Mastering completed and measurement report attached.
7. Human listening review approved against the exact master hash.
8. Metadata, artwork, credits, territory, date, and explicit-content fields checked.
9. Human release approver signs the release record naming exact asset hashes and destination.
10. Only then may the approved package be copied to a public distribution destination.
11. Verify published listing and record its URL.

## Storage
- Candidate audio: renders/wav/
- MIDI: renders/midi/
- Stems: renders/stems/
- Render receipts: renders/receipts/
- Mastering reports: evidence/mastering/
- Rights evidence index: evidence/rights/
- Listening records: evidence/listening/
- Human release approvals: evidence/approvals/
- Final package manifest: release/

Do not commit private contracts, personal data, credentials, or confidential third-party evidence. Main-branch storage is still private storage.

No automatic workflow may publish to streaming services or public repositories.
