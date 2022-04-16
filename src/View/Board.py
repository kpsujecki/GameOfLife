import pygame
import pygame.locals


class Board(object):
    def __init__(self, width, height):
        self.surface = pygame.display.set_mode((width, height), 0, 32)
        pygame.display.set_caption("Game of Life", "GoL")

    def draw_board(self, *args):
        background_board = (0, 0, 0)
        self.surface.fill(background_board)
        for drawable in args:
            drawable.draw_on(self.surface)
        pygame.display.update()
