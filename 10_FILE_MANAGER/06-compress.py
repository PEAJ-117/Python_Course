from pathlib import Path
from zipfile import ZipFile

# Create
# with ZipFile("10_FILE_MANAGER/compress.zip", "w") as zip:
#     for path in Path().rglob("*.*"):
#         print(path)
#         if str(path) != "10_FILE_MANAGER/compress.zip":
#             zip.write(path)

# Read

with ZipFile("10_FILE_MANAGER/compress.zip") as zip:
    # print(zip.namelist())
    info = zip.getinfo("10_FILE_MANAGER/06-compress.py")
    print(
        info.file_size,
        info.compress_size
    )
    # Decompress zip file
    zip.extractall("10_FILE_MANAGER/decompress")
