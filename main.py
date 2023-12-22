import players
import banker
import game

if __name__ == "__main__":
    player = players.Player()
    # player = players.MedianDeal()
    # player = players.Optimization()
    # b = banker.Banker()
    b = banker.EmulateRealBanker()
    game = game.Game(player, b)

    print(f"player wins: ${game.play()}")