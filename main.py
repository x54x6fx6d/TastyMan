import pygame
import random
import time


pygame.init()

screen = pygame.display.set_mode([500, 500])

posX = 250
posY = 400

donutPosX = random.randint(0, 500)
donutPosY = 0
donutTime = float(0.1)

fatManImg = pygame.image.load("assets/fatMan.png")
donutImg = pygame.image.load("assets/donut.png")

pygame.display.set_caption("Tasty Man x by Tommy31")

def fatMan(x, y):
    screen.blit(fatManImg, (x, y))

def fallingDonut(x, y):
    global donutPosY
    screen.blit(donutImg, (x, y))

    for x in range(4):
        time.sleep(donutTime)
        donutPosY = donutPosY + 10



running = True
while running:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                if posX <= -20:
                    print("cant go further!")
                else:
                    posX = posX - 15
                    print("Comic Book Guy moved 10px left")

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                if posX >= 430:
                    print("cannot go further!")
                else:
                    posX = posX + 15
                    print("Comic Book Guy moved 10px right")


    screen.fill((255, 255, 255))


    fatMan(posX, posY)
    fallingDonut(donutPosX, donutPosY)
    pygame.display.flip()
    pygame.display.update()

pygame.quit()
