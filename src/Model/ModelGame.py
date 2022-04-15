import pygame
import pygame.locals
from pygame.locals import MOUSEMOTION, MOUSEBUTTONDOWN
from pygame.locals import KEYDOWN, K_RETURN
from src.View.Board import Board
from src.Controller.Population import Population


class game_of_life(object):

    def __init__(self, width, height, cell_size=10):
        pygame.init()
        self.board = Board(width * cell_size, height * cell_size)
        self.fps_clock = pygame.time.Clock()
        self.population = Population(width, height, cell_size)

    def run(self):
        while not self.handle_events():
            self.board.draw_board(
                self.population,
            )
            if getattr(self, "started", None):
                self.population.cycle_generation()
            self.fps_clock.tick(15)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.locals.QUIT:
                pygame.quit()
                return True
            if event.type == MOUSEMOTION or event.type == MOUSEBUTTONDOWN:
                self.population.handle_mouse()
            if event.type == KEYDOWN and event.key == K_RETURN:
                self.started = True