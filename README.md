![Brian high resolution texture mod](media/brian-texture-mod.gif)

# Quest 64 Tale: Recompiled Mods

Download the [v1.0.9 mod packs ZIP](https://github.com/boricuapab/quest64tale-recompiled-mods/releases/tag/v1.0.9).

Companion packs for [Quest 64 Tale: Recompiled](https://github.com/boricuapab/quest64tale-recompiled), version **1.0.9**.

Open Mods → Open Mods Folder in the game launcher, copy the `.qsmod` files and `brian-hires.rtz` into that folder, then enable the packs. Installable files in this repository are in `mods/dist`. Packs are shared by Windows and Linux; install them in each platform's own profile.

- **Maximum Stats**: HP/MP maxima 500, agility/defense 255 and all elemental levels 50. Fills HP/MP once when enabled; does not provide infinite health.
- **All Spells**: elemental levels 50 independently of physical stat boosts.
- **Quest 64 Debug Menu**: after loading a game, open Settings → Debug. Choose a region/submap/entrance or a boss, then press its arrow. Finish active battles first. Boss encounters use native progression; travel does not complete earlier quests automatically.
- **Brian High Resolution Textures**: the three supplied 2048×2048 face replacements, with original cutout masks retained. No ROM, GLB models or unchanged original character textures are included.

Disabling the stat packs restores values captured in the current session. Saving with boosts active records boosted values; boss victories update saves normally.

The `.qsmod` files contain feature manifests for handlers compiled into the game. The RT64 texture pack and its three replacement PNGs are included here by the maintainer's request. `tools/package.py` rebuilds packs from their editable folders.

Code is GPL-3.0. Supplied texture artwork is maintained separately from the game's source repository; no additional licensing grant is asserted here.

## New gameplay packs

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

The release ZIP contains exactly the twelve installable `.qsmod`/`.rtz` files at its root. Editable sources remain under `packs`; `tools/package.py` rebuilds them into `mods/dist`.

Linux's usual mod directory is `~/.config/Quest64Recompiled/mods`. Windows uses `%LOCALAPPDATA%/Quest64Recompiled/mods`. Portable mode can change the profile location.

## Additional gameplay packs for v1.0.8

- **All Stats Experience**: compact vertical HP, MP, speed, defense and element progress bars. Successful magical hits also grant health XP; successful physical and magical hits grant speed and defense XP. Original growth remains active.
- **Story Direction Arrow**: horizontal purple 3D arrow toward the next story route, with a compact destination label. Clipped inside the gameplay viewport.
- **Spirit Tracker**: current level's collected/total spirits and remaining count, plus a smaller orange 3D arrow beside the story arrow toward the nearest uncollected spirit. Uses connecting doors when the target is in another reachable room; disappears when none remain.
- **Spell Preview**: selected spell's native hit radius and distance to the locked enemy, in game world units, with **Effective**, **Super Effective**, or **Not Very Effective** from the original damage matchup table. Support spells are labelled separately. Hit radius is the collision area, rather than a prediction of projectile travel or a guaranteed hit.

The v1.0.8 mods ZIP contains only the Brian texture pack and the ten gameplay `.qsmod` packs. Enable the new packs in the launcher's Mods tab after restarting the updated game.

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

## Contributors

<a href="https://openai.com/">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="media/openai-white-wordmark.svg">
    <img src="media/openai-black-wordmark.svg" alt="OpenAI" width="120">
  </picture>
</a>

**OpenAI Codex** — AI-assisted implementation, debugging and release preparation.
The OpenAI logo is a trademark of OpenAI.
