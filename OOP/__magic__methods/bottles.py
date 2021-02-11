class Bottle:
    def __init__(self, v):
        self.v = v
        self.liquids = {}

    def get_liquids_v(self):
        sum_ = 0
        for liquid in self.liquids:
            sum_ += self.liquids[liquid]
        return sum_

    def get_vilne_misce(self):
        return self.v - self.get_liquids_v()

    def add_liquid(self, liquid, v):
        if self.get_vilne_misce() < v:  # зайве виллється
            vylylosya = v - self.get_vilne_misce()
            print(f"Вилилося {vylylosya} рідини {liquid}!")
            zalylosya = self.get_vilne_misce()
            v = zalylosya

        if v > 0:
            print(f"До пляшки додалося {v} рідини {liquid}")
            if liquid not in self.liquids:
                self.liquids[liquid] = v
            else:
                self.liquids[liquid] += v

    def __getitem__(self, liquid):
        if liquid in self.liquids:
            return self.liquids[liquid]
        else:
            return 0


b1 = Bottle(5)

b1.add_liquid('молоко', 3)
b1.add_liquid('вода', 2)

print(b1['плавлений сир'])
