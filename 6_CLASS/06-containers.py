class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"Producto: {self.name} - Precio: ${self.price}"


class Categories:
    products = []

    def __init__(self, name, products):
        self.name = name
        self.products = products

    def added(self, product):
        self.products.append(product)

    def printer(self):
        for product in self.products:
            print(product)


ball = Product("Balón de fútbol", 29.99)
tShirt = Product("Camiseta deportiva", 19.99)
bat = Product("Bate de béisbol", 49.99)
helmetBiker = Product("Casco de ciclismo", 89.99)
bicycle = Product("Bicicleta", 499.99)

sport = Categories("Deportes", [ball, bat])
sport.added(helmetBiker)
sport.added(tShirt)

sport.printer()
