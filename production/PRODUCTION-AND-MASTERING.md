# Production and Mastering

## Arrangement
Confirm tempo, meter, note events, instrument assignments, section markers, dynamics, and transitions. Preserve composition source separately from rendered output.

## Render
Render WAV and MIDI from the same arrangement revision. Record renderer version, settings, source revision, output hashes, and validation receipt.

## Mix
The future full production engine should support independent tracks and buses, gain staging, pan, EQ, compression, saturation, modulation, delay, reverb, automation, and aligned stem export.

## Master
Select targets for the intended platform and genre. Measure integrated loudness, loudness range where relevant, sample peak, true peak, and clipping. Keep a high-resolution premaster.

## Human review
Listen on headphones, speakers, and a representative mobile device. Review noise, clicks, phase, balance, translation, fades, and metadata. Document reviewer and date.

The current starter renderer creates basic sine-wave WAV/MIDI files. It does not yet implement these mix/master functions.
