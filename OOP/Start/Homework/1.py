class Child():
    name = "lol"
    age = 0

    def information(self):
        print("Мене звати:" + self.name.title())
        print(f"Мені {self.age} років")

    def do_18_rokiv(self):
        return 18 - self.age


c1 = Child()
c1.name = "kek"
c1.age = 10

c1.information()
