import zipfile

def unpzip_contents(archive_file, dest_folder):
    with zipfile.ZipFile(archive_file, "r") as zip:
        zip.extractall(dest_folder)