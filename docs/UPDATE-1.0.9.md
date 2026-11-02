# Mod update notes — 1.0.9

## Solvaring Backstory FMV (game v1.0.9 or later)

[Watch Solvaring Backstory FMV](https://www.youtube.com/watch?v=IJ6um13d1Uc)

Enable **Solvaring Backstory FMV** before leaving the monastery. After Brian
exits its main front door and finishes the door animation, the supplied
30-second video plays fullscreen with sound. Gameplay pauses and game audio is
muted. Press Escape, Enter, Space, controller B or Start to skip and resume.
The video plays once per game session; loading directly outside and interior
monastery doors do not trigger it. No external player is required.

The optional `.qsmod` includes its movie and `quest64_fmv.json` door rule.
Other movie packs can use this same content format: MPEG-1 video with MP2 audio
in an MPEG program stream, with source/destination map and scene IDs and the
source door position. `once_per_session` controls replay on subsequent exits.
The v1.0.9 mods ZIP contains only twelve installable packs at its root.
