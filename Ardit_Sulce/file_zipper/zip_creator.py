import zipfile
import pathlib


def make_archive(filepaths, dest_dir):
    with zipfile.ZipFile (pathlib.Path(dest_dir, "compressed.zip"), "w") as zip:
        for filepath in filepaths:
            filepath = pathlib.Path(filepath)
            zip.write(filepath, arcname=filepath.name)
            