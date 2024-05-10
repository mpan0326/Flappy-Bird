import pygame

class Cat:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.image = pygame.image.load("cat.png")
        self.image_size = self.image.get_size()
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])
        self.delta = 3

    def move_cat(self):
        self.x = self.x - 30
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])