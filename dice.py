import random
from typing import List


class Dice:
    count: int
    max_val: int
    min_val: int

    def __init__(self, count=1, min_val=1, max_val=6):
        self.count = count
        self.max_val = max_val
        self.min_val = min_val

    def rollDice(self) -> List:
        values = []
        for _ in range(self.count):
            values.append(random.randint(self.min_val, self.max_val))
        
        return values
    
# dice = Dice(50)
# print(dice.rollDice())
