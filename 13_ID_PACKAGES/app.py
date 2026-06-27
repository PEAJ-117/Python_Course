# import requests

# r = requests.get("https://www.google.com.co")
# print(r)

from testPack.testpack import player

p = player.Player()

# Publicar paquetes en PyPi

# 1.-Registrarse
# 2.-pip3 install setuptools wheel twing --break-system-packages
# 3.-choosealicense.com (Copy the GPL)
# 4.-python3 setup.py sdist bdist_wheel
# 5.-twine upload dist/*
#   Enter your username
#   Enter your password
#   View the rute of publication
