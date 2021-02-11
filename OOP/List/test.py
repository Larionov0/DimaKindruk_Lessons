class Mouse:
    l = 20
    color = 'black'

    def __eq__(self, other):  # ==
        if self.l == other.l and self.color == other.color:
            return True
        else:
            return False


m1 = Mouse()
m1.color = 'white'

m2 = m1

print(m1 is m2)
