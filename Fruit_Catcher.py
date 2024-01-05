import pygame
import sys
import random

#Initiate
pygame.init()

#Main variables
w = 1550
h = 800
#Basket dimensions
basketx = w / 2
baskety = h - (h / 8)
basketsize = 75
basketspeed = 50
dis = pygame.display.set_mode((w, h))
pygame.display.set_caption("Fruit Catcher!!!")
#Colors
white = (255, 255, 255)
red = (255, 0, 0)
orange = (255, 122.5, 0)
yellow = (255, 255, 0)
white = (255, 255, 255)
tan = (210, 180, 140)
#Fruit dimensions
fruitw = 50
fruith = 50
fruitspeed = 20
fruits = []
clock = pygame.time.Clock()
score = 0
bg = pygame.image.load("a225dc7237c8da835f17c0d1ca9a8c80.webp")
bg1 = pygame.transform.scale(bg, (w, h))

#Upload the fruit and basket images
apple = pygame.image.load("Apple.png")
banana = pygame.image.load("banana.png")
orange1 = pygame.image.load("orange1.png")
basket = pygame.image.load("basket1.png")
apple1 = pygame.transform.scale(apple, (fruitw, fruith))
banana1 = pygame.transform.scale(banana, (fruitw, fruith))
orange2 = pygame.transform.scale(orange1, (fruitw, fruith))
basket1 = pygame.transform.scale(basket, (basketsize, basketsize))

#Draw the fruits
def fruitdraw():
    fruittype = random.choice(["apple", "banana", "orange"])
    fruitx = random.randint(0, w - fruitw)
    fruity = 0
    return {"type": fruittype, "x": fruitx, "y": fruity}

run = False

#Main loop
while not run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = True

    #Keybinds
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and basketx > 0:
        basketx = basketx - basketspeed
    if keys[pygame.K_RIGHT] and basketx < w - basketsize:
        basketx = basketx + basketspeed
    if random.random() < 0.05:
        fruits.append(fruitdraw())

    #Make the fruits fall
    for fruit in fruits:
        fruit["y"] = fruit["y"] + fruitspeed

        #The condition for if the fruits fall into the basket or to the bottom of the screen
        if (basketx < fruit["x"] < basketx + basketsize and baskety < fruit["y"] < baskety + basketsize):
            score = score + 1
            fruits.remove(fruit)
        elif fruit["y"] > h:
            fruits.remove(fruit)

    #Blit the background and draw the basket and fruits
    dis.blit(bg1, (0, 0))
    dis.blit(basket1, (basketx, baskety))
    for fruit in fruits:
        if fruit["type"] == "apple":
            dis.blit(apple1, (fruit["x"], fruit["y"]))
        if fruit["type"] == "orange":
            dis.blit(orange2, (fruit["x"], fruit["y"]))
        if fruit["type"] == "banana":
            dis.blit(banana1, (fruit["x"], fruit["y"]))

    #Load the score text
    font = pygame.font.SysFont(None, 36)
    score_text = font.render(f"Score: {score}", True, white)
    dis.blit(score_text, (100, 10))

    #Update the screen
    pygame.display.update()
    clock.tick(10)

#Quit
pygame.quit()
quit()