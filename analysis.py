import players
import banker
import game

if __name__ == "__main__":
    won = []
    # player = players.Player()
    # player = players.MedianDeal()
    player = players.Optimization()
    # banker = banker.Banker()
    b = banker.EmulateRealBanker()
    g = game.Game(player, b)
    for _ in range(100000):
        won.append(g.play())
        g.reset()
    print(sum(won) / len(won))