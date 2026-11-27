# The Łand Ơf Mů

**Repository:** Vanellye/the-land-of-mu  
**Purpose:** Original composition, actual WAV/MIDI rendering, production validation, and separately authorized public releases.

This repository is a reproducible production workspace. It includes a starter renderer that converts JSON note arrangements into real PCM WAV audio and Standard MIDI Files using Python's standard library.

## Quick start

Requires Python 3.10+; no third-party packages are needed.

    python3 tools/render.py arrangements/demo-returning-light.json --out renders/demo-returning-light

Expected outputs:
- renders/demo-returning-light.wav
- renders/demo-returning-light.mid
- renders/demo-returning-light.render.json

The starter renderer uses sine-wave synthesis for pipeline verification. It is functional, but is not a sampled-instrument library, full mix engine, or mastering chain.

## Repository map

- MAIN-STREAM.md — canonical production and release stream
- arrangements/ — machine-readable note events
- schemas/ — arrangement data contracts
- tools/render.py — WAV/MIDI renderer
- renders/ — generated output files
- production/ — mix and mastering specifications
- release/ — release checklist and packaging
- research/phd/ — .PhD research files, methods, references
- evidence/ — validation receipts, checksums, listening notes, approvals

## Release boundary

A successful render is not a public release. Publication requires rights review, technical validation, listening review, metadata/artwork checks, and explicit human approval. Private production files remain private unless individually approved for publication.
