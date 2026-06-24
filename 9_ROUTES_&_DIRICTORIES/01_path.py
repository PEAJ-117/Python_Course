from pathlib import Path  # Refrence a route inside PC

# Path(r"C:\Program Files\HaloTMCC")  # In Windows
# Path("/usr/bin")  # In Linux | Route absolute
# Path()
# Path.home()
# Path("one/__init__.py")  # Route relative | Inside project

path = Path("hellow/file.py")
path.is_file()  # File?
path.is_dir()  # Directory?
path.exists()  # Exist?

print(
    path.name,
    path.stem,
    path.suffix,
    path.parent,
    path.absolute()
)

p = path.with_name("Bugs.py")  # Change name with suffix of file
print(p)
p = path.with_suffix(".bat")
print(p)
p = path.with_stem("Bunny")
print(p)
