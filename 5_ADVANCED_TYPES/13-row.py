# FIFO (First In, First Out)
from collections import deque

row = deque([1, 2])
# row.append(3)
# row.append(4)
# row.append(5)
print(row)

# Remove the first element
row.popleft()
row.popleft()
print(row)

if not row:
    print("The row is empty")
