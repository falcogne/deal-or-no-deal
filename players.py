import random
import statistics

class Player():
    """abstract class for player objects, but also functions as random player"""
    def __init__(self):
        self.my_case = None
    
    def choose_elim_case(self, options : list):
        """choose a case to elimate from the options"""
        return random.choice(options)
    
    def choose_my_case(self, options : list):
        """choose the case to have at the start of the game"""
        self.my_case = self.choose_elim_case(options)
        return self.my_case
    
    def take_deal(self, values_left : list[int], banker_offer : int) -> bool:
        """Take the banker offer or not - this player always rejects it"""
        return False

    def choose_switch(self, other_case) -> bool:
        return True
    
class MedianDeal(Player):
    def take_deal(self, values_left : list[int], banker_offer : int) -> bool:
        """Take the banker offer or not - takes the deal if its greater than the medain"""
        if banker_offer > statistics.median(values_left):
            return True
        else:
            return False


class Optimization(Player):
    def take_deal(self, values_left : list[int], banker_offer : int) -> bool:
        """Take the banker offer or not - takes the deal if its greater than the expected value of playing it out"""
        if banker_offer > float(sum(values_left)) / len(values_left):
            return True
        else:
            return False
