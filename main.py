import pygame
import random
from bird import Bird
from cloud import Cloud
from fish import Fish

# set up pygame modules
pygame.init()
pygame.font.init()
my_font = pygame.font.SysFont('Arial', 20)
title_font = pygame.font.SysFont('Arial', 40)
pygame.display.set_caption("Flappy Goose")
title_mg = title_font.render("FLAPPY GOOSE", True, (61, 76, 125))
howto_st = my_font.render("Click to begin", True, (61, 76, 125))
howto_move = my_font.render("Press space to move up and down to dodge the cloud and flying fish", True, (61, 76, 125))
score_show = my_font.render("Score: 0", True, (61, 76, 125))
game_over_hit_fish = title_font.render("Game over you hit the fish.", True, (61, 76, 125))
game_over_hit_cloud = title_font.render("Game over you hit the cloud.", True, (61, 76, 125))
final_score = my_font.render("Final Score: 0", True, (61, 76,125))



# set up variables for the display
size = (800, 450)
screen = pygame.display.set_mode(size)
bird_x = 370
bird_y = 200
fish_x = 10
fish_y = 40
cloud_x = 40
cloud_y = 200



bg = pygame.image.load("background.png")
b = Bird(bird_x, bird_y)
c = Cloud(cloud_x, cloud_y)
f = Fish(fish_x, fish_y)

st_msg_show = True
score = 0
add_score = False
fish_hit = False
cloud_hit = False
pygame.mixer.init()
pygame.mixer.music.load("gameover.mp3")
#pygame.mixer.music.play()
played = False

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
            st_msg_show = False

    c.move_cat()
    f.move_fish()

    if f.x >= 870:
        f.x = -70
        f.y = random.randint(70, 390)

    f.move_fish()

    if c.x >= 890:
        c.x = -140
        c.y = random.randint(125, 325)

    if b.rect.colliderect(c.rect) and st_msg_show == False:
        cloud_hit = True
    if b.rect.colliderect(f.rect) and st_msg_show == False:
        fish_hit = True

    if c.x > 888 and fish_hit == False and cloud_hit == False:
        add_score = True


    if cloud_hit == False and add_score == True:
        score += 1
        add_score = False
        score_show = my_font.render("Score: " + str(score), True, (255, 255, 255))


    screen.blit(bg, (0, 0))
    if st_msg_show == True:
        screen.blit(title_mg, (230, 160))
        screen.blit(howto_move, (100, 210))
        screen.blit(howto_st, (320, 240))

    if st_msg_show == False and fish_hit == False and cloud_hit == False:
        screen.blit(b.image, b.rect)
        screen.blit(c.image, c.rect)
        screen.blit(f.image, f.rect)
        screen.blit(score_show, (0,0))

    if fish_hit == True:
        if not played:
            pygame.mixer.music.play()
        played = True
        screen.blit(game_over_hit_fish, (160, 180))
        final_score = my_font.render("Final Score: " + str(score), True, (61, 76, 125))
        screen.blit(final_score, (330, 230))

    if cloud_hit == True:
        if not played:
            pygame.mixer.music.play()
        played = True
        screen.blit(game_over_hit_cloud, (160, 180))
        final_score = my_font.render("Final Score: " + str(score), True, (61, 76, 125))
        screen.blit(final_score, (330, 230))

    pygame.display.update()

    frame += 1


# Once we have exited the main program loop we can stop the game engine:
pygame.quit()