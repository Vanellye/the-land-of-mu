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

IDEA → COMPOSED → ARRANGED → RENDER_QUEUED → WAV_MIDI_RENDERED → TECH_CHECKED → LISTENED → MIXED → MASTERED → RELEASE_CANDIDATE

### Render command

    python3 tools/render.py arrangements/demo-returning-light.json --out renders/demo-returning-light

Expected outputs:
- PCM WAV, 16-bit, stereo, 44.1 kHz by default
- Standard MIDI File, format 0
- JSON render receipt with renderer version, settings, file sizes, SHA-256 hashes, and validation results

The starter engine synthesizes sine-wave note events so the pipeline creates real audio and MIDI files. It is transparent and dependency-free. Future engines can replace the oscillator with sampled instruments, soundfonts, synthesis plugins, and a mix/master chain while retaining the envelope and receipt format.

## 3. Quality gates

Technical checks:
- WAV header and PCM format parse correctly
- Sample rate, bit depth, channels, and duration match settings
- MIDI header, track chunk, tempo, note-on/note-off events, and end marker are valid
- Output files are non-empty and SHA-256 hashes are recorded
- No clipping in generated PCM

Listening and production checks:
- Musical phrasing and timing reviewed
- Melody, bass, harmony, rhythm, and dynamics reviewed
- Mix translation and headroom checked
- Master loudness and true-peak targets selected for intended platform and genre
- Artifacts and metadata read back after export

Technical validation does not establish subjective quality or mastering compliance. Those require listening and appropriate measurement.

## 4. Separate public release stream

PRIVATE_COMPOSITION → RENDERED_MASTER → RIGHTS_REVIEW → TECHNICAL_QA → LISTENING_REVIEW → METADATA_AND_ARTWORK → HUMAN_RELEASE_APPROVAL → PUBLIC_RELEASE

A public release must have:
- Confirmed authorship and rights for lyrics, composition, samples, performances, and artwork
- Final WAV master and requested distribution formats
- Verified hashes and render/mastering receipts
- Track title, contributors, credits, ISRC if assigned, release date, territory, explicit-content status, and artwork
- Human approval receipt naming the approved assets and destination
- Public listing URL and post-publication readback

No renderer, CI job, mirror, or assistant may publish automatically. A rendered file is not automatically approved for distribution.

## 5. Connected repositories

- DataEnvelopeMint — https://github.com/Vanellye/DataEnvelopeMint — envelopes, lyrics, notation, catalog, provenance
- $ilk Mirror — https://github.com/vanellyetm-ux/-ilk--mirror — lineage and evidence bridge
- Lumi — https://github.com/vanellyetm-ux/Lumi/blob/main/MUSIC-MAIN-STREAM.md — public-facing stream index

Private materials remain private. Public indexes may link to this production repository but must not expose its files.

## 6. Directory map

- arrangements/ — composition event data
- schemas/ — input contracts
- tools/ — rendering and validation tools
- renders/ — actual WAV/MIDI/stem outputs
- production/ — mixing and mastering plans
- release/ — release packaging and approval checklists
- research/phd/ — research and .PhD materials
- evidence/ — render receipts, checksums, tests, approvals

## 7. Governance

Keep composition source immutable once tagged; make revisions through reviewable commits. Preserve source references and transformation notes. Never overwrite a released master silently. Every new render receives a new receipt. Public promotion is a distinct, human-authorized step.
