import pygame
from View.Board import Board


class game_of_life(object):

    def __init__(self, width, height, cell_size=10):
        pygame.init()
        self.board = Board(width * cell_size, height * cell_size)
        self.fps_clock = pygame.time.Clock()

    def run(self):
        while not self.handle_events():
            # działaj w pętli do momentu otrzymania sygnału do wyjścia
            self.board.draw_board()
            self.fps_clock.tick(15)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.locals.QUIT:
                pygame.quit()
                return True
