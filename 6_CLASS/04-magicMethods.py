class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __del__(self):
        print(f"The person {self.name} is dead")

    def __str__(self):  # this a magic method
        return f"Class Person: {self.name}"

    def speak(self):
        print(f"{self.name} talk: Whats up, Bro?!")


person = Person("Barry", 23)
# print(person)  # Printing Equal
# text = str(person)
# print(text)  # Printing Equal
del person
