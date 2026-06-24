from pathlib import Path
from time import ctime

file = Path("10_FILE_MANAGER/test-file.txt")
# file.exists()
# file.rename()
# file.unlink()

# print(file.stat())

print("acceso", ctime(file.stat().st_atime))
print("creado", ctime(file.stat().st_ctime))
print("modificado", ctime(file.stat().st_mtime))
