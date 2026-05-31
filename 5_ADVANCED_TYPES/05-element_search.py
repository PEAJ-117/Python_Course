pets = ["Cabo", "Pelusa", "Gofy", "Croqueta",
        "Cabo", "Rabioso", "Perdido", "Grug"]

# Check repeated elements
# With method "count()"
print(pets.count("Cabo"))

# Check if it's found
if "Cabo" in pets:
    # Search with method "index()"
    # If exists, print
    print(pets.index("Cabo"))
