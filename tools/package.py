from pathlib import Path
import zipfile
ROOT=Path(__file__).resolve().parents[1]
DIST=ROOT/'mods'/'dist'
DIST.mkdir(parents=True,exist_ok=True)
for folder in sorted((ROOT/'packs').iterdir()):
    extension='rtz' if (folder/'rt64.json').exists() else 'qsmod'
    archive=DIST/(folder.name+'.'+extension)
    with zipfile.ZipFile(archive,'w',zipfile.ZIP_DEFLATED) as z:
        for path in sorted(folder.rglob('*')):
            if path.is_file():z.write(path,path.relative_to(folder).as_posix())
    print(archive.name)
