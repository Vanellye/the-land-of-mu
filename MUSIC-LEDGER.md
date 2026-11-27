# THE LAND OF MU — MUSIC LEDGER

**Ledger ID:** MU-MUSIC-LEDGER-001  
**Production repository:** `Vanellye/the-land-of-mu`  
**Visibility:** Private  
**Default branch:** `main`  
**Purpose:** Human-readable catalog of rendered audio, MIDI, mastering reports, fingerprints, and review/release state.

> Access note: this repository is private. A raw-file URL opened outside an authenticated GitHub session may show GitHub's 404 page. Open the repository file page while signed into an account with repository access, then use the file page's download control. This ledger does not make audio public and does not bypass repository permissions.

## Track catalog

### Returning Light — Render Test
- **Track ID:** `demo-returning-light`
- **Arrangement:** `arrangements/demo-returning-light.json`
- **Tempo / meter:** 68 BPM / 3/4
- **Source render:** `renders/wav/returning-light-demo.wav`
- **Source render page:** [Open premaster file in GitHub](https://github.com/Vanellye/the-land-of-mu/blob/main/renders/wav/returning-light-demo.wav)
- **Master candidate:** `renders/wav/returning-light-demo-master.wav`
- **Master file page:** [Open mastered WAV in GitHub](https://github.com/Vanellye/the-land-of-mu/blob/main/renders/wav/returning-light-demo-master.wav)
- **Master report:** [Open mastering measurements](https://github.com/Vanellye/the-land-of-mu/blob/main/renders/wav/returning-light-demo-master.wav.mastering.json)
- **Render receipt:** [Open render receipt](https://github.com/Vanellye/the-land-of-mu/blob/main/renders/receipts/returning-light-demo.render.json)
- **MIDI:** [Open MIDI file in GitHub](https://github.com/Vanellye/the-land-of-mu/blob/main/renders/midi/returning-light-demo.mid)
- **Master format:** WAV / PCM S24LE / 48,000 Hz / 24-bit / stereo
- **Duration:** 5.644146 seconds
- **Master SHA-256:** `e69f1f247a17d0cbd4f8877bc9e4ddaac1ac4c77f7bd3e4bde8f8d836f45b2dc`
- **Measured final pass:** -13.77 LUFS integrated / -9.41 dBTP true peak / 0.20 LU loudness range
- **Premaster:** 44,100 Hz / 16-bit / stereo / 5.644118 seconds
- **Premaster SHA-256:** `5506ff80d0485eadf4f7795b01cc048e9388c4aaf69433ab8bb660a4acae5342`
- **MIDI SHA-256:** `036fd8055f7cce06ad1c41f4109083418c256400b2f8430796701d8f49d072ef`
- **Render type:** Sine-oscillator pipeline proof; not a sampled-instrument production.
- **Mastering process:** Automated two-pass FFmpeg EBU R128 loudness processing. No creative EQ, saturation, stereo widening, or reverb.
- **Listening review:** PENDING — no human listening approval is recorded.
- **Rights review:** PENDING.
- **Artwork / metadata:** Not complete.
- **Publication:** NOT PUBLISHED. Human publication authorization has not been granted.

## Listening instructions on Android
1. Open the **Master file page** above while signed in to GitHub with access to this private repository.
2. On the file page, use **Download** (or the download/raw control shown by GitHub). If the browser redirects to a 404, first verify that the same signed-in account can open the repository root.
3. Open the downloaded `.wav` with the phone's music player or an audio editor. A WAV file may download rather than play inline; that is normal browser behavior.
4. Listen to the complete track, then record your decision and timestamped notes in a review record. Do not mark approval merely because the file downloads or its hash matches.

## Evidence and release gates
This ledger points to source render receipts and mastering measurement reports. Those records prove file identity and automated checks; they do not prove artistic quality, rights clearance, or human approval.

Required before public distribution:
- Rights and source-asset clearance
- Human engineering review of the master
- Human listening approval against the exact master SHA-256
- Completed credits, metadata, and approved artwork
- Human release authorization naming the exact asset hashes and destination
- Post-publication URL and verification

The production repository stays private. Public distribution must copy only individually approved allowlisted assets to a separate destination. Never make this entire repository public merely to solve a playback-link problem.

## Ledger maintenance
Add one catalog entry per track/version. Keep prior premaster and master files immutable. Record hashes, format, duration, tool/version, validation results, reviewer decision, and publication URL. A new master gets a new filename and new ledger entry; do not overwrite a previously reviewed master.
