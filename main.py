import pygame
import random

screen_size = [360,600]
screen = pygame.display.set_mode(screen_size)
pygame.font.init()

background = pygame.image.load("background.png")
chicken = pygame.image.load("chicken.png")
user = pygame.image.load("user.png")

def display_score():
    score_font = pygame.font.SysFont("comicsans",30)
    score_img = score_font.render("Score: "+str(score),1,(255,255,255))
    screen.blit(score_img,(20,10))

def random_offset():
    return random.randint(-2000,-100)


chicken_y = [ random_offset(), random_offset(),random_offset()]
user_x = 150
score = 0

def crushed(idx):
    global score
    score -= 50
    chicken_y[idx] = random_offset()

def update_chicken_position(idx):
    if chicken_y[idx] > 600:
        global score
        score += 5
        chicken_y[idx] = random_offset()
    else:
        chicken_y[idx] += 5



keep_alive = True
clock = pygame.time.Clock()
while keep_alive:
    pygame.event.get()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT] and user_x < 280:
        user_x += 5
    if keys[pygame.K_LEFT] and user_x > 0:
        user_x -= 5
        print('pressed left')

    print(score)

    update_chicken_position(0)
    update_chicken_position(1)
    update_chicken_position(2)

    screen.blit(background,[0,0])
    screen.blit(user,[user_x,520])
    screen.blit(chicken,[0,chicken_y[0]])
    screen.blit(chicken,[150,chicken_y[1]])
    screen.blit(chicken,[280,chicken_y[2]])

    if chicken_y[0] > 500 and user_x <70:
        crushed(0)

    if(chicken_y[1] > 500 and user_x > 80 and user_x < 200):
        crushed(1)


    if chicken_y[2]>500 and user_x > 220:
        crushed(2)

    display_score()
    pygame.display.update()
    clock.tick(60)    
