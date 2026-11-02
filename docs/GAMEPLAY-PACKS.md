# Gameplay packs

These three packs require game v1.0.7 or later and are disabled by default.

### Auto Save

[Watch Auto Save](https://www.youtube.com/watch?v=2KT1_DY_U60)

checkpoints after door/zone movement finishes. Keeps two generations in the profile's `autosaves` folder, separate from Controller Pak saves. Use **Restore Auto Save** in the Mods footer, load a game if needed, and close settings. Older checkpoints use native entrance placement. Battles and dead-player states are protected.
### Random Encounter Rate

[Watch Random Encounter Rate](https://www.youtube.com/watch?v=H31UjwU_MD0)

use **Configure** to select **Off**, **10%**, **25%**, **50%**, or **Default**. Rates apply per distance travelled; scripted bosses remain available.
### Enemy Health Bars

[Watch Enemy Health Bars](https://www.youtube.com/watch?v=1xy7mQerDz4)

overhead bars update every battle frame, including bosses. Close-range bars stay at the screen edge. Green/yellow/red indicate remaining health.

The release ZIP contains exactly fifteen installable `.qsmod`/`.rtz` files at its root. Editable sources remain under `packs`; `tools/package.py` rebuilds them into `mods/dist`.

Linux's usual mod directory is `~/.config/Quest64Recompiled/mods`. Windows uses `%LOCALAPPDATA%/Quest64Recompiled/mods`. The profile directory is searched first; the executable’s mods folder is the fallback. The profile copy wins duplicate mod IDs.
