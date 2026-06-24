import json
from pathlib import Path

pathfile = "10_FILE_MANAGER/products.json"

# Writer JSON
# products = [
#     {"id": 1, "name": "Ball"},
#     {"id": 2, "name": "glasses"},
#     {"id": 3, "name": "gloves"},
# ]
#
# data = json.dumps(products)
# # print(data)
# Path(pathfile).write_text(data)

# Read
data = Path(pathfile).read_text(encoding="utf-8")
products = json.loads(data)
# print(products)
# Update
products[0]["name"] = "celphone"
Path(pathfile).write_text(json.dumps(products))
