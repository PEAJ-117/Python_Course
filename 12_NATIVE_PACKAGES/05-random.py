import random
import string
listx = [1, 2, 3, 4, 5, 6, 7, 8]
list2 = [1, 2, 3, 4, 5, 6, 7, 8]
random.shuffle(listx)
# print(
#    random.random(), "\n",
#    random.randint(1, 10), "\n",
#    listx, "\n",
#    random.choice(list2), "\n",
#    random.choices(list2, k=3), "\n",
#    random.choices("abcdefghi.,123", k=3), "\n",
#    "".join(random.choices("abcdefghi.,123", k=3)), "\n",
# )

charx = string.ascii_letters
digitx = string.digits
selectx = random.choices(charx + digitx, k=16)
print(f'Contraseña: {"".join(selectx)}')
