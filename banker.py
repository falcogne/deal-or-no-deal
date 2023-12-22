import board
import random

class Banker():
    def __init__(self):
        self.lowest_percent = 0.05
        self.highest_percent = 0.35
    
    def make_offer(self, vals : list) -> int:
        expected_val = int( float(sum(vals)) / len(vals) )
        lowest_offer = int(expected_val * self.lowest_percent)
        highest_offer = max(1, int(expected_val * self.highest_percent))
        return random.randrange(lowest_offer, highest_offer)
    
if __name__ == "__main__":
    vals = [0.01, 1, 5, 10, 25, 50, 100, 200, 500, 1000, 2000, 5000, 10_000, 20_000, 50_000, 100_000, 200_000, 400_000, 500_000, 750_000, 1_000_000]

    b = Banker()
    print(b.make_offer(vals))