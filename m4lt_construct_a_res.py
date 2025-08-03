Python
import pygame
import sys

# Game Settings
GAME_WIDTH, GAME_HEIGHT = 800, 600
FPS = 60

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Game Prototype Simulator Data Model
class Simulator:
    def __init__(self):
        self.entities = []

    def add_entity(self, entity):
        self.entities.append(entity)

    def update(self):
        for entity in self.entities:
            entity.update()

    def draw(self, screen):
        screen.fill(BLACK)
        for entity in self.entities:
            entity.draw(screen)

class Entity:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.speed = 2

    def update(self):
        self.x += self.speed
        if self.x > GAME_WIDTH or self.x < 0:
            self.speed *= -1

    def draw(self, screen):
        pygame.draw.rect(screen, WHITE, (self.x, self.y, self.width, self.height))

def main():
    pygame.init()
    screen = pygame.display.set_mode((GAME_WIDTH, GAME_HEIGHT))
    clock = pygame.time.Clock()
    simulator = Simulator()

    entity = Entity(100, 100, 50, 50)
    simulator.add_entity(entity)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        simulator.update()
        simulator.draw(screen)
        pygame.display.flip()
        clock.tick(FPS)

if __name__ == "__main__":
    main()