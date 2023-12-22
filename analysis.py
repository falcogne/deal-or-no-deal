import players
import game

if __name__ == "__main__":
    won = []
    # player = players.Player()
    # player = players.MedianDeal()
    player = players.Optimization()
    g = game.Game(player)
    for _ in range(100000):
        won.append(g.play())
        g.reset()
    print(sum(won) / len(won))