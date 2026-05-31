# Keywords Arguments
# Packages all parameters in only parameter

def get_product(**dates):
    print(dates["name"],
          dates["no"])


get_product(id="id",
            name="column",
            no=23)
