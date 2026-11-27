# Persistent Render and Master Storage

This directory stores versioned production outputs committed to the private main branch after explicitly dispatched workflows.

## Layout
- wav/ — immutable premaster renders and separately named mastered candidates
- midi/ — Standard MIDI files
- stems/ — aligned track and bus stems
- receipts/ — render settings, validation, and SHA-256 receipts
- previews/ — listening copies

Mastering outputs include a matching `.mastering.json` report with input/output hashes and loudness measurements. Never overwrite a premaster or previously approved master. A successful automated process does not imply human listening approval or rights clearance.
