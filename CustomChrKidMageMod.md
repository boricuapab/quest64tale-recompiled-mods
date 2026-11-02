# CustomChrKidMageMod

Requires Quest 64 Tale: Recompiled v1.1.4 or later.

Copy CustomChrKidMageMod.qsmod into your profile mods folder or the mods folder
beside the executable. Enable CustomChrKidMageMod in the launcher and load a game.
Disable the mod to restore Brian. NPC models, collision and story logic remain
native. Brian's native shadow and attachment calculations continue to run.

KidMage.glb is a skinned, UV-mapped character with vertex colors, embedded PNG
textures, the staff and all 30 animation_00 through animation_29 clips. Nine
standalone PNGs are in textures/. The head, leg and cape maps retain 2048x2048
resolution; the six supplied solid-color maps retain their original 8x8 size.
The identical blue shirt/arm maps share an embedded GLB image.

The installable pack contains the GLB, original PNGs, RT64 replacement mapping,
and a 30 fps native pose cache built from the same evaluated Maya scene. The
cache avoids a GLTF dependency in the game and preserves exact whole-body poses.
Editing geometry, rig or clips requires re-exporting and rebuilding the pack;
changing the loose GLB alone does not update the packed runtime geometry.

Maya export preserved the original scene file, selection and current frame.
Validation compares every sampled skin pose with Maya and every serialized
joint transform with the reference. Both platform executables also provide:
  Quest64Recompiled --validate-character CustomChrKidMageMod.qsmod
(Use Quest64Recompiled.exe on Windows.) This check does not touch saves.
