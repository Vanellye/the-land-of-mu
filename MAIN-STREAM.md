# The Łand Ơf Mů — Main Stream Frame

**Stream key:** LAND-OF-MU-MAIN  
**Repository:** https://github.com/Vanellye/the-land-of-mu  
**Visibility:** Private production source  
**Default branch:** main

## 1. Purpose

A reproducible route from original composition data to actual WAV/MIDI artifacts, quality checks, release candidates, and separately authorized public distribution.

The stream distinguishes:
1. Composition source — lyrics, melody, harmony, rhythm, arrangement.
2. Render recipe — machine-readable arrangement plus renderer version/settings.
3. Rendered artifact — actual WAV, MIDI, and later stems.
4. Verified release candidate — checksums, technical checks, rights status, listening notes.
5. Public release — separate publication event with explicit human authorization.

## 2. Production stream

IDEA → COMPOSED → ARRANGED → RENDER_QUEUED → WAV_MIDI_RENDERED → TECH_CHECKED → RIGHTS_REVIEWED → MASTERED → LISTENING_APPROVED → RELEASE_CANDIDATE → HUMAN_RELEASE_APPROVED → PUBLIC_RELEASE

### Render command

    python3 tools/render.py arrangements/demo-returning-light.json --out renders/demo-returning-light

The starter engine synthesizes sine-wave note events and produces actual PCM WAV and Standard MIDI files. It is transparent and dependency-free. Future engines can replace the oscillator with sampled instruments, soundfonts, synthesis plugins, and a mix/master chain while retaining the envelope and receipt format.

## 3. Persistent main-branch file storage

The private main branch stores versioned production files:

- renders/wav/ — WAV masters and premaster exports
- renders/midi/ — Standard MIDI files
- renders/stems/ — aligned stems
- renders/receipts/ — renderer settings, technical validation, and SHA-256 receipts
- evidence/rights/ — rights review records and safe evidence references
- evidence/mastering/ — mastering measurements and reports
- evidence/listening/ — human listening reviews
- evidence/approvals/ — human release approvals

The manually dispatched workflow at .github/workflows/render-and-store-main.yml renders the demo and commits WAV, MIDI, and receipt files to main. The workflow does not publish to external services.

### Stored first render

- WAV: renders/wav/returning-light-demo.wav
- MIDI: renders/midi/returning-light-demo.mid
- Receipt: renders/receipts/returning-light-demo.render.json

The receipt records 44.1 kHz, 16-bit, stereo PCM, 5.644118 seconds, MIDI format 0 at 480 PPQ, file sizes, SHA-256 hashes, and technical validation. This is a basic sine-oscillator demo render, not a mastered commercial release.

## 4. Technical quality checks

- WAV header and PCM format parse correctly
- Sample rate, bit depth, channels, and duration match settings
- MIDI header, track chunk, tempo, note-on/note-off events, and end marker are valid
- Output files are non-empty and SHA-256 hashes are recorded
- No clipping in generated PCM

Technical validation does not establish subjective quality or mastering compliance.

## 5. Rights review

Current status: NOT REVIEWED. No rights clearance is claimed.

Before release, inventory composition, lyrics, samples, loops, soundfonts, performances, artwork, and contributions. Record each creator/rightsholder, source, rights basis, permitted scope, restrictions, evidence reference, reviewer, decision, and date. Pending, restricted, or rejected material blocks release until resolved.

See production/RIGHTS-REVIEW.md.

## 6. Mastering

Current status: NOT MASTERED. The starter renderer has no EQ, compression, limiting, true-peak oversampling, loudness normalization, dithering, or mastering measurement.

A master record must include the premaster and final hashes, sample format, LUFS-I, LRA where relevant, sample peak, true peak, clipping inspection, stereo/mono checks, chain/settings, engineer, and date.

See production/MASTERING-SPECIFICATION.md.

## 7. Human listening approval

Current status: PENDING. No listening approval is recorded.

A human reviewer must identify the exact file hash, review playback on appropriate devices, check musical balance, timing, artifacts, fades, vocal intelligibility if applicable, stereo image, and translation, and record a decision and notes.

See production/LISTENING-APPROVAL.md.

## 8. Separate public release stream

PRIVATE_COMPOSITION → RENDERED_MASTER → RIGHTS_REVIEW → TECHNICAL_QA → MASTERING → LISTENING_REVIEW → METADATA_AND_ARTWORK → HUMAN_RELEASE_APPROVAL → PUBLIC_RELEASE

A public release must have:
- Confirmed authorship and rights for all material
- Final WAV master and requested distribution formats
- Verified hashes and render/mastering receipts
- Track title, contributors, credits, ISRC if assigned, release date, territory, explicit-content status, and artwork
- Human approval receipt naming the approved asset hashes and destination
- Public listing URL and post-publication readback

No renderer, CI job, mirror, or assistant may publish automatically. A rendered file is not automatically approved for distribution.

See release/RELEASE-PROCESS.md and release/RELEASE-GATE.md.

## 9. Connected repositories

- DataEnvelopeMint — https://github.com/Vanellye/DataEnvelopeMint — envelopes, lyrics, notation, catalog, provenance
- $ilk Mirror — https://github.com/vanellyetm-ux/-ilk--mirror — lineage and evidence bridge
- Lumi — https://github.com/vanellyetm-ux/Lumi/blob/main/MUSIC-MAIN-STREAM.md — public-facing stream index

Private materials remain private. Public indexes may link to this production repository but must not expose its files.

## 10. Governance

Keep composition source immutable once tagged; make revisions through reviewable commits. Preserve source references and transformation notes. Never overwrite a released master silently. Every new render receives a new receipt. Public promotion is a distinct, human-authorized step.
