class Animals:
    def eat(self):
        print("Comiendo")


class Dog(Animals):
    def walk(self):
        print("Paseando")


class BabyDog(Animals):
    def programming(self):
        print("Programando")
# ----------------------------------
# Multi-Inheritance


class Walking:
    def walking(self):
        print("Caminando")


class Flying:
    def flying(self):
        print("Volando")


class Swimming:
    def swimming(self):
        print("Nadando")


class Person(Walking, Flying, Swimming):
    def smiling(self):
        print("Sonriendo")
# ----------------------------------
# Annulment Methods

# CLASS FATHER


class Bird:
    def __init__(self):
        # self.flys = True
        self.flys = "Las aves vuelan"

    def fly(self):
        print("El ave vuela")

# SUBCLASS


class Duck(Bird):
    def __init__(self):
        super().__init__()  # Access the build of the father class
        # self.swimm = True
        self.swimm = "Los patos nadan"

    def fly(self):
        super().fly()  # Access the method of the father class
        print("El pato vuela")


duck = Duck()
duck.fly()  # El pato vuela
print(f"Cuando {duck.flys}, {duck.swimm}...")
