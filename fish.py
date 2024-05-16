import pygame


class Fish:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.image = pygame.image.load("fish.png")
        self.image_size = self.image.get_size()
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])
        self.delta = 1

    def move_cat(self):
        self.x = self.x + 2
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])
