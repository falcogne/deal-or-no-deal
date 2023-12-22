import players
import game

if __name__ == "__main__":
    player = players.Player()
    game = game.Game(player)

    print(f"player wins: ${game.play()}")