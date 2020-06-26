import pygame
import random

# basic configuration
config = {
    'cell_size': 20,
    'cols': 10,
    'rows': 20,
    'maxfps': 30,
    'height' : 500,
    'width' : 500
}

# colors for shapes
colors = [
    (0, 0, 0),
    (255, 0, 0),
    (0, 150, 0),
    (0, 0, 255),
    (255, 120, 0),
    (255, 255, 0),
    (180, 0, 255),
    (0, 220, 220)]

# Define the shapes of the single parts
tetris_shapes = [
    [[1, 1, 1],
     [0, 1, 0]],

    [[0, 2, 2],
     [2, 2, 0]],

    [[3, 3, 0],
     [0, 3, 3]],

    [[4, 0, 0],
     [4, 4, 4]],

    [[0, 0, 5],
     [5, 5, 5]],

    [[6, 6, 6, 6]],

    [[7, 7],
     [7, 7]]]


# class for new pieces
class Pieces:
    def __init__(self,x, y, shape):
        self.x = x
        self.y = y
        self.shape = shape
        self.color = colors[tetris_shapes.index(shape)]

    def get_shape(self):
        return random.choice(tetris_shapes)

    def rotation(self):
        pass

    def move(self,vel):
        new_x = self.x + vel

    def hard_drop(self):
        pass

    def soft_drop(self, level):
        speed = 3 * level
        self.y -= speed

    def new_pieces(self):
        self.shape = random.choice(tetris_shapes)
        self.x = int(config['cols'] / 2 - len(self.stone[0]) / 2)
        self.y = 0


# class for tetris
class TetrisApp:

    row = config['rows']
    col = config['cols']
    border_x = (config['width'] - col * config['cell_size']) / 2
    border_y = (config['height'] - row * config['cell_size'])

    def __init__(self):
        pygame.init()
        self.width = config['width']
        self.height = config['height']
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.event.set_blocked(pygame.MOUSEMOTION)

    def draw_grid(self):

        for x in range(TetrisApp.col):
            for y in range(TetrisApp.row):
                pygame.draw.rect(self.screen, (255,255,255), (TetrisApp.border_x + x * config['cell_size'], TetrisApp.border_y + y * config['cell_size'], config['cell_size'], config['cell_size']),1)

    def draw_shape(self):
        pygame.draw.rect(self.screen, (180, 0, 255), (TetrisApp.border_x + 1 * config['cell_size'], TetrisApp.border_y + 10 * config['cell_size'], config['cell_size'],config['cell_size']), 0)

    def start(self):
        pass

    def score(self):
        pass

    def run(self):
        clock = pygame.time.Clock()
        start = True
        while start:
            self.screen.fill((0,0,0))
            self.draw_grid()
            self.draw_shape()
            pygame.display.update()
            keys = pygame.key.get_pressed()
            pygame.display.set_caption("Tetris")

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if keys[pygame.K_LEFT]:
                    pygame.quit()

            clock.tick(config['maxfps'])


if __name__ == '__main__':
    app = TetrisApp()
    app.run()




