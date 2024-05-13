import pygame
import random
#from playsound import playsound
from bird import Bird
from cat import Cat

# set up pygame modules
pygame.init()
pygame.font.init()
my_font = pygame.font.SysFont('Arial', 20)
title_font = pygame.font.SysFont('Arial', 40)
pygame.display.set_caption("Flappy Goose")
title_mg = title_font.render("FLAPPY GOOSE", True, (61, 76, 125))
howto_st = my_font.render("Click to begin", True, (61, 76, 125))
howto_move = my_font.render("Press space to move up and down to dodge the cat", True, (61, 76, 125))



# set up variables for the display
size = (800, 450)
screen = pygame.display.set_mode(size)
bird_x = 370
bird_y = 200
cat_x = 20
cat_y = 200


bg = pygame.image.load("background.png")
#pipe1 = pygame.image.load()
#telephone_pole = pygame.image.load()

b = Bird(bird_x, bird_y)
c = Cat(cat_x, cat_y)

st_msg_show = True


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
        if event.type == pygame.MOUSEBUTTONUP:
            start_msg_show = False

    c.move_cat()

    if c.x >= 930:
        c.x = -150
        c.y = random.randint(125, 325)



    screen.blit(bg, (0, 0))
    if st_msg_show == True:
        screen.blit(title_mg, (230, 160))
        screen.blit(howto_move, (160, 210))
        screen.blit(howto_st, (320, 240))

    if st_msg_show == False:
        screen.blit(b.image, b.rect)
        screen.blit(c.image, c.rect)
    pygame.display.update()

    frame += 1


# Once we have exited the main program loop we can stop the game engine:
pygame.quit()