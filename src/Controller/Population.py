import pygame
import pygame.locals
from past.builtins import xrange
from ..const.variables import DEAD, ALIVE


class Population(object):

    def __init__(self, width, height, cell_size=10):
        self.box_size = cell_size
        self.height = height
        self.width = width
        self.generation = self.reset_generation()

    def reset_generation(self):
        return [[DEAD for y in xrange(self.height)] for x in xrange(self.width)]

    def clear_population(self):
        self.generation = [[DEAD for y in xrange(self.height)] for x in xrange(self.width)]

    def handle_mouse(self):
        buttons = pygame.mouse.get_pressed()
        if not any(buttons):
            return
        alive = True if buttons[0] else False
        x, y = pygame.mouse.get_pos()
        x /= self.box_size
        y /= self.box_size

        self.generation[int(x)][int(y)] = int(ALIVE if alive else DEAD)

    def draw_on(self, surface):
        for x, y in self.alive_cells():
            size = (self.box_size, self.box_size)
            position = (x * self.box_size, y * self.box_size)
            color = (0, 128, 0)
            pygame.draw.rect(surface, color, pygame.locals.Rect(position, size), width=0, border_radius=5, border_top_left_radius=-1, border_top_right_radius=-1, border_bottom_left_radius=-1, border_bottom_right_radius=-1)

    def alive_cells(self):
        for x in range(len(self.generation)):
            column = self.generation[x]
            for y in range(len(column)):
                if column[y] == ALIVE:
                    yield x, y

    def neighbours(self, x, y):
        for nx in range(x - 1, x + 2):
            for ny in range(y - 1, y + 2):
                if nx == x and ny == y:
                    continue
                if nx >= self.width:
                    nx = 0
                elif nx < 0:
                    nx = self.width - 1
                if ny >= self.height:
                    ny = 0
                elif ny < 0:
                    ny = self.height - 1
                yield self.generation[nx][ny]

    def cycle_generation(self):
        next_gen = self.reset_generation()
        for x in range(len(self.generation)):
            column = self.generation[x]
            for y in range(len(column)):
                count = sum(self.neighbours(x, y))
                if count == 3:
                    next_gen[x][y] = ALIVE
                elif count == 2:
                    next_gen[x][y] = column[y]
                else:
                    next_gen[x][y] = DEAD

        self.generation = next_gen
