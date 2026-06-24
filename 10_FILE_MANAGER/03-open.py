from io import open

# Write
# text = "Hellow!"
# file = open("10_FILE_MANAGER/hola.txt", "w")
# file.write(text)
# file.close()

# Read
# file = open("10_FILE_MANAGER/hola.txt", "r")
# text = file.read()
# file.close()
# print(text)

# Reas as list
# file = open("10_FILE_MANAGER/hola.txt", "r")
# text = file.readlines()
# file.close()
# print(text)

# Magic method \ WITH and SEEK
# with open("10_FILE_MANAGER/hola.txt", "r") as file:
#     print(file.readlines())
#     file.seek(0)
#     for line in file:
#         print(line)

# Add
# file = open("10_FILE_MANAGER/hola.txt", "a+")
# file.write("\nGoodbye!!")
# file.close

# Read & write
with open("10_FILE_MANAGER/hola.txt", "r+") as file:
    text = file.readlines()
    file.seek(0)
    text[0] = "Hellow, my name is Paul"
    file.writelines(text)
