import pygame


class Bird:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.image = pygame.image.load("bird.png")
        self.image_size = self.image.get_size()
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])
        self.delta = 2



    def move_bird(self, direction):
        if direction == "UP":
            if self.y >= 10:
                self.y = int(self.y) - self.delta
        if direction == "DOWN":
            if self.y <= 400:
                self.y = int(self.y) + self.delta
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])
