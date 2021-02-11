class Slime():
    name = ""
    weight = 0

    def prilipat(self, other):
        """
        Этот метод принимает self, а также other - другого слизня.
        И он прилепляет второго слизня к себе,
        таким образом вес self увеличивается на величину,
        равную весу второго слизня

        :param other: другий слимак
        """
        self.weight += other.weight
        other.weight = 0


s1 = Slime()
s1.name = "lol"
s1.weight = 15

s2 = Slime()
s2.name = "kek"
s2.weight = 35

s1.prilipat(s2)
