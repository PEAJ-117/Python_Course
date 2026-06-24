from pathlib import Path

path = Path("9_ROUTES_&_DIRICTORIES")
# path.exists()
# path.mkdir()
# path.rmdir()  # Remove directory only its empty
# path.rename("Renombre")

# for p in path.iterdir():
#     print(p)

# files = [p for p in path.iterdir() if not p.is_dir()]
# files = [p for p in path.glob("01_*.py")]
# files = [p for p in path.glob("**/*.py")]
files = [p for p in path.rglob("*.py")]  # Recursive
print(files)
