# Functions
# print() it's a display or console print

# Create a function
# def: word reserved ... name

def hellow(name, last_name="Default"):  # Parameters, Optional parameters
    print("Hola Mundo!")
    print(f"Bienvenido {name} {last_name}!")


# Call function
# Arguments & Parameters-------------------
hellow("Paul", "Edwin")  # Arguments
hellow("Walker")

hellow(last_name="Antonio", name="Paul")  # Arguments named
