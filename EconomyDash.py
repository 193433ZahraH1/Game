# Write your code here :-)

from random import randint

WIDTH = 400
HEIGHT = 400
score = 0
game_over = False

man = Actor("small_man")
man.pos = 100, 100

coin = Actor("coin")
coin.scale = 0.01
coin.pos = 200, 200


def draw():
    screen.fill("purple")
    man.draw()
    coin.scale = 0.1
    coin.draw()
    screen.draw.text("Score: " + str(score) , color="pink" , topleft=(10 , 10))

    if game_over:
        screen.fill("black")
        screen.draw.text("Final Score: " + str(score) , topleft=(10, 10), fontsize=80)

def place_coin():
    coin.x = randint(20, (WIDTH - 20))
    coin.y = randint(20, (HEIGHT - 20))

def update():
    global score

    if keyboard.d:
        man.x = man.x - 10
    elif keyboard.a:
        man.x = man.x + 10
    elif keyboard.w:
        man.y = man.y - 10
    elif keyboard.s:
        man.y = man.y + 10

    coin_collected = man.colliderect(coin)

    if coin_collected:
        score = score + 10
        place_coin()
        if score > 200:
            man.image = 'large_man'
        elif score > 70:
            man.image = 'medium_man'

def time_up():
    global game_over
    game_over = True

clock.schedule(time_up, 30.0)

place_coin()
