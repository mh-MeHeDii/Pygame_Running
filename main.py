import pygame
import random
from pygame import mixer

pygame.init()

# Window settings
window_x = 1200
window_y = 800
screen = pygame.display.set_mode((window_x, window_y))
pygame.display.set_caption("Running for Living")

# Background and icon
background = pygame.image.load("jungle.jpg")
background = pygame.transform.scale(background, (window_x, window_y))
icon = pygame.image.load("cat2.png")
pygame.display.set_icon(icon)

# Running Human images
'''runner_xsize = 300
runner_ysize = 300

image1 = pygame.image.load("run1.png")
image1 = pygame.transform.scale(image1, (runner_xsize, runner_ysize))
image2 = pygame.image.load("run2.png")
image2 = pygame.transform.scale(image2, (runner_xsize, runner_ysize))
image3 = pygame.image.load("run3.png")
image3 = pygame.transform.scale(image3, (runner_xsize, runner_ysize))

images = [image1, image2, image3]
image_x = 300
image_y = 300'''

#Mouse Runner
mouse_xsize = 200
mouse_ysize = 200

image1 = pygame.image.load("mouse1.png")
image1 = pygame.transform.scale(image1, (mouse_xsize, mouse_ysize))
image2 = pygame.image.load("mouse2.png")
image2 = pygame.transform.scale(image2, (mouse_xsize, mouse_ysize))

images = [image1, image2]
image_x = 500
image_y = 400

clock = pygame.time.Clock()

#Big Bird
bird_xsize = 220
bird_ysize = 220

bird1 = pygame.image.load("bird1.png")
bird1 = pygame.transform.scale(bird1, (bird_xsize, bird_ysize))
bird2 = pygame.image.load("bird2.png")
bird2 = pygame.transform.scale(bird2, (bird_xsize, bird_ysize))
bird3 = pygame.image.load("bird3.png")
bird3 = pygame.transform.scale(bird3, (bird_xsize, bird_ysize))

bird_xx = random.randint(0, window_x)
bird_yy = random.randint(0, 300)
birds_golanai = [bird1, bird2, bird3]

#Eagle
bird_xsize = 200
bird_ysize = 200

bird1 = pygame.image.load("1.png")
bird1 = pygame.transform.scale(bird1, (bird_xsize, bird_ysize))
bird2 = pygame.image.load("2.png")
bird2 = pygame.transform.scale(bird2, (bird_xsize, bird_ysize))
bird3 = pygame.image.load("3.png")
bird3 = pygame.transform.scale(bird3, (bird_xsize, bird_ysize))
bird4 = pygame.image.load("4.png")
bird4 = pygame.transform.scale(bird3, (bird_xsize, bird_ysize))
bird5 = pygame.image.load("5.png")
bird5 = pygame.transform.scale(bird3, (bird_xsize, bird_ysize))

bird_x = 300
bird_y = 15
birds = [bird1, bird2, bird3, bird4, bird5]

#Chasing Cat
cat_xsize = 300
cat_ysize = 300

image1 = pygame.image.load("cat1.png")
image1 = pygame.transform.scale(image1, (cat_xsize, cat_ysize))
image2 = pygame.image.load("cat2.png")
image2 = pygame.transform.scale(image2, (cat_xsize, cat_ysize))

images_cat = [image1, image2]
image_xcat = 50
image_ycat = 340

#functions
def run(x, y, image):
    screen.blit(image, (x, y))

def bird_eagle(x, y, image):
    screen.blit(image, (x, y)) 

def bird_golanai(x, y, image):
    screen.blit(image, (x, y))

def cat(x, y, image):
    screen.blit(image, (x, y))            

current_image_index = 0
image_display_time = 100 #koto mili seconds image thakbe seta
last_image_switch_time = pygame.time.get_ticks()

run_game = True
while run_game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run_game = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if image_y > 0:
                    image_y -= 130

            if event.key == pygame.K_DOWN:
                if image_y < window_y-320:
                    image_y += 130    
      

    screen.fill((0, 0, 0))
    screen.blit(background, (0, 0))

    current_time = pygame.time.get_ticks()

    if current_time - last_image_switch_time > image_display_time:
        current_image_index = (current_image_index + 1) % len(images)
        last_image_switch_time = current_time

    run(image_x, image_y, images[current_image_index])
    image_x += 6
    if image_x > window_x:
        image_x = -320

    bird_eagle(bird_x, bird_y, birds[current_image_index])
    bird_x -= 10
    if(bird_x < -320):
        bird_x = window_x + 50

    bird_golanai(bird_xx, bird_yy, birds_golanai[current_image_index])
    bird_xx -= 10
    #bird_yy = random.randint(0, 300)
    if(bird_xx < -320):
        bird_xx = window_x + 50

    cat(image_xcat, image_ycat, images_cat[current_image_index])
    image_xcat += 6
    if(image_xcat > window_x):
        image_xcat = -320        

    pygame.display.update()

    clock.tick(50)

pygame.quit()
   