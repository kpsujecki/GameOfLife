import argparse
import pygame
import pygame_menu
from src.Model.ModelGame import game_of_life
from src.const.variables import HELP

parser = argparse.ArgumentParser()

parser.add_argument('-he', dest='height', type=int)
parser.add_argument('-wi', dest='width', type=int)

args = parser.parse_args()

def draw_menu():
    pygame.init()
    surface = pygame.display.set_mode((1200, 1000))

    menu = pygame_menu.Menu('Welcome', 800, 600,
                            theme=pygame_menu.themes.THEME_BLUE)

    menu.add.button('Play', start_the_game)
    menu.add.button('Quit', pygame_menu.events.EXIT)
    for m in HELP:
        menu.add.label(m, align=pygame_menu.locals.ALIGN_CENTER)
    menu.mainloop(surface)


def make_popup():
    print("TEST")

def start_the_game():
    game = game_of_life(args.height, args.width)
    game.run()
    pygame.quit()

if __name__ == "__main__":
    draw_menu()

