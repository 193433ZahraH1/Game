blob = Actor('charecter')
blob.pos = 100,100

WIDTH = 500
HEIGHT = 300

def draw():
    screen.fill((255,0,0))
    blob.draw()

def update():
    blob.left = blob.left + 2
    if blob.left > 500:
        blob.right = 0
