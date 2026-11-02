![Brian high resolution texture mod](media/brian-texture-mod.gif)

# Quest 64 Tale: Recompiled Mods

Download the [v1.1.6 mod packs ZIP](https://github.com/boricuapab/quest64tale-recompiled-mods/releases/tag/v1.1.6).

Companion packs for [Quest 64 Tale: Recompiled](https://github.com/boricuapab/quest64tale-recompiled), version **1.1.6**.

## Custom characters — v1.1.6

The [v1.1.6 release](https://github.com/boricuapab/quest64tale-recompiled-mods/releases/tag/v1.1.6) contains **fifteen installable packs**, including both custom characters. Use the matching v1.1.6 game executable and enable one character replacement at a time.

- **[CustomChrKidMageMod](CustomChrKidMageMod.md)** replaces Brian with Kid Mage, including all 30 animations, original-resolution textures, an animated staff and smooth high-framerate motion.
- **[CustomChrMr.McCloudMod](CustomChrMr.McCloudMod.md)** replaces Brian with Mr. McCloud, with all 30 animations, animated tail/staff, a repeating eyelid cycle and corrected door placement. The current pack is revision **1.0.4**. It is distributed through release assets because it exceeds GitHub's Git-file size limit.

Native shadows, collision and story progression remain handled by the game. If an older copy is installed in the profile mods folder, replace it there; profile copies take priority over the game folder.

See [v1.1.6 release notes](docs/UPDATE-1.1.6.md).


Open Mods → Open Mods Folder in the game launcher, copy the `.qsmod` files and `brian-hires.rtz` into that folder, then enable the packs. Installable files in this repository are in `mods/dist`. Packs are shared by Windows and Linux; install them in each platform's own profile.

- **Maximum Stats**: HP/MP maxima 500, agility/defense 255 and all elemental levels 50. Fills HP/MP once when enabled; does not provide infinite health.
- **All Spells**: elemental levels 50 independently of physical stat boosts.
- **Quest 64 Debug Menu**: after loading a game, open Settings → Debug. Choose a region/submap/entrance or a boss, then press its arrow. Finish active battles first. Boss encounters use native progression; travel does not complete earlier quests automatically.
- **Brian High Resolution Textures**: the three supplied 2048×2048 face replacements, with original cutout masks retained. No ROM, GLB models or unchanged original character textures are included.

Disabling the stat packs restores values captured in the current session. Saving with boosts active records boosted values; boss victories update saves normally.

The `.qsmod` files contain feature manifests for handlers compiled into the game. The RT64 texture pack and its three replacement PNGs are included here by the maintainer's request. `tools/package.py` rebuilds packs from their editable folders.

Code is GPL-3.0. Supplied texture artwork is maintained separately from the game's source repository; no additional licensing grant is asserted here.

## Videos

- [Auto Save](https://www.youtube.com/watch?v=2KT1_DY_U60)
- [Random Encounter Rate](https://www.youtube.com/watch?v=H31UjwU_MD0)
- [Enemy Health Bars](https://www.youtube.com/watch?v=1xy7mQerDz4)
- [Solvaring Backstory FMV](https://www.youtube.com/watch?v=IJ6um13d1Uc)

## Documentation

See the [gameplay pack guide](docs/GAMEPLAY-PACKS.md), [Game Speed settings](GAME-SPEED.md), and [previous update notes](docs/).

## Contributors

<a href="https://openai.com/">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="media/openai-white-wordmark.svg">
    <img src="media/openai-black-wordmark.svg" alt="OpenAI" width="120">
  </picture>
</a>

**OpenAI Codex** — AI-assisted implementation, debugging and release preparation.
The OpenAI logo is a trademark of OpenAI.
