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
    

class EmulateRealBanker(Banker):
    def make_offer(self, vals : list) -> int:
        self.lowest_percent = 0.05 + 0.5 * (21 - len(vals))/20
        self.highest_percent = 0.35 + 0.8 * (21 - len(vals))/20
        # print((21 - len(vals))/20) # 0.05 0.3 0.5 0.65 0.75 0.8 0.85 0.9 0.95
        # print(self.lowest_percent, self.highest_percent)
        expected_val = int( float(sum(vals)) / len(vals) )
        lowest_offer = int(expected_val * self.lowest_percent)
        highest_offer = max(1, int(expected_val * self.highest_percent))
        actual_offer = random.randrange(lowest_offer, highest_offer)
        return actual_offer


if __name__ == "__main__":
    vals = [0.01, 1, 5, 10, 25, 50, 100, 200, 500, 1000, 2000, 5000, 10_000, 20_000, 50_000, 100_000, 200_000, 400_000, 500_000, 750_000, 1_000_000]

    b = Banker()
    print(b.make_offer(vals))