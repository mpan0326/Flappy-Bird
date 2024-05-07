import pygame
import random
from playsound import playsound
from birdie import Bird

# set up pygame modules
pygame.init()
pygame.font.init()
my_font = pygame.font.SysFont('Arial', 20)
pygame.display.set_caption("Flappy Crow")


# set up variables for the display
size = (800, 600)
screen = pygame.display.set_mode(size)
BIRD_START_X = 500

bg = pygame.image.load("background.png")
pipe1 = pygame.image.load()
telephone_pole = pygame.image.load()

b = Bird(300, 200)


INITIAL_HOUSE_X = random.randint(0,600)
INITIAL_TREE_X = random.randint(0,600)
house_x = INITIAL_HOUSE_X
tree_x = INITIAL_TREE_X


# render the text for later

# The loop will carry on until the user exits the game (e.g. clicks the close button).
run = True
# -------- Main Program Loop -----------
clock = pygame.time.Clock()
frame = 0
while run:
    # --- Main event loop
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        b.move_bird("UP")
    else:
        b.move_bird("DOWN")

    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            run = False

    screen.blit(bg, (0, 0))
    screen.blit(house, (house_x, 360))
    screen.blit(tree, (tree_x, 360))
    screen.blit(bird.image, bird.rect)
    screen.blit(b.image, b.rect)
    pygame.display.update()

    frame += 1

# Once we have exited the main program loop we can stop the game engine:
pygame.quit()