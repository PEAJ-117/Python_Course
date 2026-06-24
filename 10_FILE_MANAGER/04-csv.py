import csv
import os

# Write
# with open("10_FILE_MANAGER/file.csv", "w") as file:
#    writer = csv.writer(file)
#    writer.writerow(["twit_id", "user_id", "text"])
#    writer.writerow([1000, 1, "TWIT"])
#    writer.writerow([1001, 2, "TWIT2"])

# Read
# with open("10_FILE_MANAGER/file.csv") as file:
#    reader = csv.reader(file)
#    print(list(reader))
#    file.seek(0)
#    for line in reader:
#        print(line)

# Update
with open("10_FILE_MANAGER/file.csv") as r, open("10_FILE_MANAGER/file_temp.csv", "w") as w:
    reader = csv.reader(r)
    writer = csv.writer(w)
    # Iteration
    for line in reader:
        if line[0] == "1000":
            writer.writerow([1000, 1, "Update Text"])
        else:
            writer.writerow(line)

    os.remove("10_FILE_MANAGER/file.csv")
    os.rename("10_FILE_MANAGER/file_temp.csv", "10_FILE_MANAGER/file.csv")
