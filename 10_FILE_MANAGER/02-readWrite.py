from pathlib import Path

file = Path("10_FILE_MANAGER/test-file.txt")  # Locate the file
text = file.read_text("utf-8").split("\n")  # Read and separate by line breaks
text.insert(0, "Hellow, my friend!")  # Insert new line corresponding
file.write_text("\n".join(text), "utf-8")  # Write the file
