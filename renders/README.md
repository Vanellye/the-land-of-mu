# Persistent Render Storage

This directory stores versioned production outputs committed to the private main branch after a successful, explicitly dispatched render-and-store workflow.

## Layout
- wav/ — PCM masters and premaster exports
- midi/ — Standard MIDI files
- stems/ — aligned track and bus stems
- receipts/ — render settings, validation, and SHA-256 checksums
- previews/ — listening copies

Each render receives a unique track/revision identifier. Do not silently overwrite a previously approved master. The GitHub Actions artifact is a temporary handoff; files here are the persistent repository copy.
