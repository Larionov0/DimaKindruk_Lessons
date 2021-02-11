class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_hi(self):
        print(f"{self.name}: Привіт!")

    def __gt__(self, other):  # >
        return self.age > other.age

    def __call__(self, text):
        print(f"{self.name}: {text}")


h = Human('Sasha', 12)
h2 = Human('Bob', 19)

h('I love pizza')
