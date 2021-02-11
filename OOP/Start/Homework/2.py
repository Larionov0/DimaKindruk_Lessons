class Rectangle():
    width = 0
    length = 0

    def plosha(self):
        return self.width * self.length

    def perimetr(self):
        return (self.width + self.length) * 2


r1 = Rectangle()
r1.width = 10
r1.length = 15

a = r1.perimetr()
print(a)
