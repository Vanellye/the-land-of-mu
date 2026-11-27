# The Łand Ơf Mů — Main Stream Frame

**Stream key:** LAND-OF-MU-MAIN  
**Repository:** https://github.com/Vanellye/the-land-of-mu  
**Visibility:** Private production source  
**Default branch:** main

## 1. Purpose

A reproducible route from original composition data to actual WAV/MIDI artifacts, mastering candidates, quality checks, release candidates, and separately authorized public distribution.

The stream distinguishes composition source, render recipe, rendered artifact, verified release candidate, and public release. These are separate states.

## 2. Production stream

IDEA → COMPOSED → ARRANGED → RENDERED_PREMASTER → MASTERING_PROCESSED → TECH_CHECKED → RIGHTS_REVIEWED → LISTENING_APPROVED → RELEASE_CANDIDATE → HUMAN_RELEASE_APPROVED → PUBLIC_RELEASE

### Render command

    python3 tools/render.py arrangements/demo-returning-light.json --out renders/demo-returning-light

The starter engine synthesizes sine-wave note events. It is a pipeline proof, not a sampled-instrument production.

## 3. Persistent main-branch storage

- renders/wav/ — premaster and mastered WAV candidates
- renders/midi/ — Standard MIDI files
- renders/stems/ — aligned track and bus stems
- renders/receipts/ — render and mastering reports
- evidence/rights/ — rights review records and safe evidence references
- evidence/mastering/ — engineering notes and measurements
- evidence/listening/ — human listening reviews
- evidence/approvals/ — human release approvals
- release/ — metadata, selected public files, and package rules

The render workflow stores WAV/MIDI/receipt outputs on main. The separate `.github/workflows/master-and-store-main.yml` workflow runs the two-pass mastering process on a selected WAV under `renders/wav/` and stores a new master plus measurement report on main. Neither workflow publishes externally.

### Existing demo premaster

- WAV: `renders/wav/returning-light-demo.wav`
- MIDI: `renders/midi/returning-light-demo.mid`
- Receipt: `renders/receipts/returning-light-demo.render.json`

This is a short sine-oscillator demo premaster. It is not a finished commercial recording.

## 4. Mastering process

`tools/master.py` uses FFmpeg two-pass EBU R128 loudnorm, preserves the source, and writes a 24-bit PCM WAV at 48 kHz by default with a JSON report containing source/output SHA-256 hashes and measured loudness data.

Example:

    python3 tools/master.py renders/wav/returning-light-demo.wav --out renders/wav/returning-light-demo-master.wav

Default targets are -14 LUFS-I, -1 dBTP, and 11 LU LRA. These are configurable starting values, not universal artistic targets. The automated chain does not perform creative EQ, saturation, stereo widening, or reverb. Human engineering and listening checks remain required.

**Status:** mastering engine and workflow implemented; no final master has yet been generated or approved.

See `production/MASTERING-SPECIFICATION.md`.

## 5. Rights review and listening approval

Rights review remains pending. No clearance is claimed for composition, performances, soundfonts, samples, loops, or artwork until individually documented.

Human listening approval remains pending and must identify the exact final master SHA-256. Check tonal balance, transient integrity, timing, artifacts, noise, fades, stereo/mono compatibility, and translation.

See `production/RIGHTS-REVIEW.md` and `production/LISTENING-APPROVAL.md`.

## 6. Public distribution file selection

`release/PUBLIC-DISTRIBUTION-SELECTION.json` is the allowlist for the intended export package. It names the candidate master, mastering report, optional MIDI, artwork, and metadata. `tools/package_release.py` builds a ZIP only when every required gate is marked approved and all required files exist. Use `--allow-pending` only for a diagnostic selection report; it never creates a ZIP.

The current selection is blocked: the master and report do not yet exist, artwork is not selected, and rights/listening/release approvals remain pending.

See `release/PUBLIC-DISTRIBUTION.md`.

## 7. Public release gates

A public release requires:
- Confirmed authorship and rights for every asset
- Final WAV master and requested formats
- Verified hashes and mastering report
- Human listening approval against the exact master hash
- Complete metadata, credits, and cleared artwork
- Human authorization naming exact asset hashes and destination
- Post-publication URL and verification

No CI job or assistant publishes automatically. The production repository remains private. A dedicated export destination must receive only the approved selected assets; making this repository public would expose all repository files and history.

## 8. Connected repositories

- DataEnvelopeMint — https://github.com/Vanellye/DataEnvelopeMint
- $ilk Mirror — https://github.com/vanellyetm-ux/-ilk--mirror
- Lumi — https://github.com/vanellyetm-ux/Lumi/blob/main/MUSIC-MAIN-STREAM.md

Public indexes must not expose private source materials.

## 9. Governance

Preserve provenance and immutable history. Never silently overwrite a released master. Every render/master gets a distinct receipt and hash. Public promotion is a separate, human-authorized event.
