# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import pygame, math, random
pygame.init()

def randspot():
    x = random.randint(10,630)
    y = random.randint(10,450)
    return (x, y)

def randup():
    x = random.randint(30, 400)
    return (x, -150)

def dist(w,x,y,z):
    deltaX = w-y
    deltaY = x -z
    X2 = deltaX * deltaX
    Y2 = deltaY * deltaY
    Sum = X2 + Y2
    return math.sqrt(Sum)

def main():
    screen = pygame.display.set_mode((640, 480))
    pygame.display.set_caption("Defend the Earth")

    background = pygame.Surface(screen.get_size())
    NIGHT = (10, 10, 10)
    background.fill(NIGHT)

    square = pygame.Surface((5, 5))
    star = (250, 245, 243)
    square.fill(star)

    laser = pygame.Surface((6, 16))
    RED = (250, 2, 3)
    laser.fill(RED)

    laser2 = pygame.Surface((6, 16))
    GREEN = (2, 245, 3)
    laser2.fill(GREEN)

    heart = pygame.image.load('New Piskel (11).png')
    ship = pygame.image.load('New Piskel (16).png')
    alien = pygame.image.load('New Piskel (15).png')

    h = 3
    t = 0
    f = 200
    s = 200
    l = 0
    laser_bool = 0
    (x,y) = randspot()
    (x1, y1) = randspot()
    (x2, y2) = randspot()
    (x3, y3) = randspot()
    (x4, y4) = randspot()
    (x5, y5) = randspot()
    (x6, y6) = randspot()
    (x7, y7) = randspot()
    (x8, y8) = randspot()
    (x9, y9) = randup()
    n = 0
    score = 0

    myFont = pygame.font.SysFont("Aerial", 48)

    l1 = myFont.render("Day", 1, (0, 0, 0))
    l2 = myFont.render("Night", 1, (0, 0, 0))
    label = l1

    # Action also part of main function
    clock = pygame.time.Clock()
    keepGoing = True
    while keepGoing:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing = False

        l1 = myFont.render(str(score), 1, (255, 255, 255))
        l2 = myFont.render(str(h) + 'x', 1, (255, 255, 255))

        background.fill(NIGHT)
        screen.blit(background, (0, 0))
        screen.blit(square, (x,y))
        screen.blit(square, (x1, y1))
        screen.blit(square, (x2, y2))
        screen.blit(square, (x3, y3))
        screen.blit(square, (x4, y4))
        screen.blit(square, (x5, y5))
        screen.blit(square, (x6, y6))
        screen.blit(square, (x7, y7))
        screen.blit(square, (x8, y8))
        screen.blit(label, (280, 390))
        screen.blit(l1, (15, 15))
        screen.blit(l2, (15, 430))
        screen.blit(heart, (15, 367))
        screen.blit(ship, (f,250))
        screen.blit(alien, (x9,y9))

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            f = f - 1.5
        if keys[pygame.K_SPACE] and laser_bool == 0:
            laser_bool = 1
            n = f + 100
        elif keys[pygame.K_RIGHT]:
            f = f + 1.5

        if (laser_bool == 1):
            screen.blit(laser, (n, 320 + l))
            l = l - 1.25

        if l < -300:
            l = 0
            laser_bool = 0

        if dist(n,320 + l, x9 + 100, y9 + 100) < 30:
            (x9, y9) = randup()
            l = 0
            laser_bool = 0
            score = score + 1
        t = t + .01
        y = y + .25
        y1 = y1 + .25
        y2 = y2 + .25
        y3 = y3 + .25
        y4 = y4 + .25
        y5 = y5 + .25
        y6 = y6 + .25
        y7 = y7 + .25
        y8 = y8 + .25

        if (t/200 > .25):
            y9 = y9 + t/200
        else:
            y9 = y9 + .25

        if h == 0:
            keepGoing = False



        if y > 480:
            (x,y) = randup()
        if y1 > 480:
            (x1,y1) = randup()
        if y2 > 480:
            (x2,y2) = randup()
        if y3 > 480:
            (x3,y3) = randup()
        if y4 > 480:
            (x4,y4) = randup()
        if y5 > 480:
            (x5,y5) = randup()
        if y6 > 480:
            (x6,y6) = randup()
        if y7 > 480:
            (x7,y7) = randup()
        if y8 > 480:
            (x8,y8) = randup()
        if y9 > 480:
            h = h - 1
            t = 0
            (x9,y9) = randup()

        if f < -50:
            f = -50
        if f > 500:
            f = 500

        pygame.display.flip()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
    print("thank you for playing")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
