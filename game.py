import players
import board
import banker

class Game():
    def __init__(self, player : players.Player, banker : banker.Banker):
        self.player = player
        self.reset()
    
    def reset(self):
        self.NUMBER_TO_CHOOSE = [6,5,4,3,2,1,1,1,1]
        self.board = board.Board()
        self.banker = banker.EmulateRealBanker()
        self.player.my_case = None
        self.values_unopened = [v for v in self.board.VALUES]
        assert sum(self.NUMBER_TO_CHOOSE) == len(self.board.VALUES)-2
        assert len(self.board.cases) > 2
        assert len(self.values_unopened) > 2

    def play(self):
        self.choose_player_case()
        # print(f"player chose case number {self.player.my_case.number}")

        for num_choices in self.NUMBER_TO_CHOOSE:
            # choose n cases now
            for _ in range(num_choices):
                elim = self.eliminate_case()
                # print(f"player eliminated case number {elim} with value {elim}")
                # print(f"case values remaining: {self.values_unopened}")
                # print()
            
            offer = self.banker.make_offer(self.values_unopened)
            # print(f"there are {self.values_unopened} values remaining in cases and the banker offers ${offer}")

            deal_taken = self.player.take_deal(self.values_unopened, offer)
            if deal_taken:
                # print(f"DEAL, player wins {offer}")
                return offer
            
            # print("NO DEAL")
            # print("\n-------next round of elimination------\n")
        
        switched = self.player.choose_switch(self.board.cases[0])

        if switched:
            # print("player swiched cases")
            self.player.my_case, self.board.cases[0] = self.board.cases[0], self.player.my_case
        
        winning_value = self.player.my_case.open()

        # print(f"player won ${winning_value}")
        return winning_value
            
    def choose_player_case(self):
        self.player.choose_my_case(self.board.cases)
        self.board.choose_case(self.player.my_case.number)
    
    def eliminate_case(self):
        e = self.player.choose_elim_case(self.board.cases)
        self.values_unopened.remove(e.value)
        self.board.choose_case(e.number)
        return e


