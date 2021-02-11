class Cup:
    seria = 'AWCF23'
    v = 4
    color = 'blue'
    liquids = {}

    def count_v_of_liquids(self):
        sum_ = 0
        for liquid in self.liquids:
            sum_ += self.liquids[liquid]
        return sum_

    def add_liquid(self, liquid, v):
        count = self.count_v_of_liquids()
        if count + v > self.v:
            old_v = v
            v = self.v - count
            vylylosya = old_v - v
            print(f'З чашки вилилося {vylylosya} л рідини {liquid}')

        if v == 0:
            return

        if liquid in self.liquids:
            self.liquids[liquid] += v
        else:
            self.liquids[liquid] = v

    def drop_liquid(self, v):
        total_v = self.count_v_of_liquids()
        result_v = total_v - v
        m = result_v / total_v

        for liquid in self.liquids:
            self.liquids[liquid] = round(self.liquids[liquid] * m, 2)


c = Cup()
c.v = 5
c.color = 'red'

# c.liquids = {}
# c.add_liquid('вода', 2)
# c.add_liquid('молоко', 1)
# c.add_liquid('вода', 4)
# c.add_liquid('трава', 3)
# print(c.liquids)
#
# c.drop_liquid(3)
# print(c.liquids)

c2 = Cup()
c2.v = 10
c2.liquids = {}

c2.add_liquid('малинове желе', 2)
c2.add_liquid('ананасове желе', 5)
c2.add_liquid('травяне желе', 6)

print(c2.liquids)
c2.drop_liquid(4)
print(c2.liquids)
