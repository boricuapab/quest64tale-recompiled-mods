# CustomChrMr.McCloudMod

Requires Quest 64 Tale: Recompiled v1.1.6 or later.
Copy CustomChrMr.McCloudMod.qsmod into the profile mods folder or the mods folder
beside the game executable. Enable it in Mods. Disable Kid Mage when using this
character; disable this mod to return to Brian (or another enabled character).

MrMcCloud.glb contains the skinned character, animated staff, UVs, vertex colors,
embedded textures and all 30 animation_00 through animation_29 clips.
Original PNGs and the four composited eye variants are in textures/.
The head/body map retains 2048x1024; iris, eyelids and staff maps retain 2048x2048;
hair and jewel retain their original smaller sizes. No source PNG was overwritten.

The eyelids hold open for about three seconds, then blink through
001,002,003,004,003,002 at 12 fps (half a second). This repeats independently of
the body animation. A 180-degree export correction aligns the character and
staff with Brian's facing direction without changing movement controls.
The GLB includes the same blink cycle in every clip using four gated eye skins,
so only one eye surface is visible at each sample. The normal character and staff
animations remain intact. Texture UVs match Maya repeat wrapping without the old proxy half-texel offset.
The GLB preserves Maya's centimeter-to-meter scale;
the game fits the model to Brian's native character height.

Door clips are exported in place. The game applies Brian's original horizontal
door root motion separately, preventing scale or facing changes from moving
the custom character away from the native player location.

The v1.1.6 game renderer blends custom-character vertices between native poses
at display framerates above the original rate. This also applies to Kid Mage.
The installable pack contains the GLB, PNGs, RT64 texture mapping and native
30 fps pose cache. The cache comes from the same evaluated Maya scene. Changes
to geometry or animation require rebuilding that cache, rather than replacing
only the loose GLB. The Maya scene file was not saved or overwritten.

Both platform executables can check the pack without loading a game or saves:
Quest64Recompiled --validate-character CustomChrMr.McCloudMod.qsmod
Use Quest64Recompiled.exe on Windows.
