# LIFO: Last In, First Out

queue = []
queue.append(1)
queue.append(2)
queue.append(3)
print(queue)  # Output: [1, 2, 3]

queueLast = queue.pop()  # Remove the first element (1)
print(queueLast)  # Output: [2, 3]
print(queue)  # Output: [2, 3]
print(queue[-1])  # Output: 3
queue.pop()  # Remove the first element (2)
queue.pop()  # Remove the first element (3)

if not queue:
    print("Queue is empty")
