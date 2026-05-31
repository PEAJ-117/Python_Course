pets = ["Cabo", "Pelusa", "Gofy", "Croqueta",
        "Cabo", "Rabioso", "Perdido", "Grug"]

# Add a new
pets.insert(1, "Melven")
# Add to last
pets.append("Loba")
# Remove found first form left to right
pets.remove("Cabo")
# Remove the last
pets.pop(1)
# Reserved word
del pets[0]
# Clean
pets.clear()

print(pets)
