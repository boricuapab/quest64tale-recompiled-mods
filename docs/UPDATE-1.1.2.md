# Quest 64 Tale: Recompiled v1.1.2

Fixes an access violation when loading a saved game and entering gameplay.
The gameplay and accelerated door-check hooks now sign-extend guest addresses
before accessing game memory on a 64-bit host. Existing saves need no conversion.

Includes the latest readable vertical attack preview, spell/staff damage
percentages, and accelerated character/camera rendering changes. Game Speed
offers Default (1x), 2x, 4x and 8x in its Configure menu.

Debug travel uses normal grounded arrival coordinates for every selectable
location and all eight bosses, clearing leftover door input locks. This
avoids replaying a door animation that places Brian behind level geometry.
Ordinary door travel retains its native animations.

Mods load from the user profile's Quest64Recompiled/mods folder first, then
the mods folder beside the executable. The profile copy wins duplicate IDs.
On Windows the profile is %LOCALAPPDATA%/Quest64Recompiled; on Linux it is
~/.config/Quest64Recompiled. Restart the launcher after installing mods.

Controller Pak reads prefer the profile, then fall back to the game folder.
Successful writes mirror to both locations. Keep the header and numbered
Controller Pak save files together. Auto Save checkpoints remain separate.

The game archives contain no ROM, extracted game assets, saves, movies or
personal settings. Supply your own supported USA ROM. Optional mods are
distributed separately.

## Game Speed (updated for game v1.1.2)

Enable **Game Speed**, open **Configure**, and choose **Default (1x)**, **2x**, **4x**, or **8x**. Brian, enemies and combat timers advance faster; menus and transitions keep normal timing. Choose Default (1x) for normal speed. The v1.1.2 mods ZIP contains thirteen installable packs at its root. Put them in `mods/` beside the updated executable. See [Game Speed](../GAME-SPEED.md) and [v1.1.2 notes](UPDATE-1.1.2.md).

Spell Preview now shows 50%, 100% or 125% element multipliers and estimated damage as a percentage of enemy maximum HP, including staff attacks in reach. Solvaring FMV includes the monastery-exit backstory, pre-dialogue battle introduction, and post-celebration defeat movie.

## v1.1.2 update

Use the matching v1.1.2 game executable for the save-load crash fix and safe debug arrivals at all selectable locations and bosses. The runtime also includes the vertical, bold attack preview and the latest speed rendering fixes. Install the thirteen packs from the ZIP into your profile mods folder or the mods folder beside the executable. See [release notes](UPDATE-1.1.2.md).
