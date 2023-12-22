import case
import random


class Board():
    def __init__(self):
        # self.VALUES = [0.01, 1, 5, 10, 25, 50, 100, 200, 500, 1000, 2000, 5000, 10_000, 20_000, 50_000, 100_000, 200_000, 400_000, 500_000, 750_000, 1_000_000]
        self.VALUES = [0.01, 1, 5, 10, 25, 50, 75, 100, 200, 300, 400, 500, 750, 1000, 5000, 10_000, 25_000, 50_000, 75_000, 100_000, 200_000, 300_000, 400_000, 500_000, 750_000, 1_000_000]
        self.cases = None
        self.reset()
    
    def reset(self):
        self.cases = [case.Case(val) for val in self.VALUES]
        random.shuffle(self.cases)
        for i, _ in enumerate(self.cases):
            self.cases[i].number = i + 1
    
    def choose_case(self, case_num):
        for c in self.cases:
            if c.number == case_num:
                self.cases.remove(c)
                c.open()
                return c
        else:
            raise ValueError(f"case number must be between {1} and {len(self.VALUES)} (inclusive)")

if __name__ == "__main__":
    print("testing board.py")
    b = Board()
    print(b.cases)
    c = b.choose_case(1)
    print(c)
    print(b.cases)