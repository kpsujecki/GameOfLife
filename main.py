from src.Model.ModelGame import game_of_life
import argparse

parser = argparse.ArgumentParser()

parser.add_argument('-he', dest='height', type=int)
parser.add_argument('-wi', dest='width', type=int)

args = parser.parse_args()

DEAD = 0
ALIVE = 1

if __name__ == "__main__":
    game = game_of_life(args.height, args.width)
    game.run()
