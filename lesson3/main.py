import pgzrun
import random

HEIGHT=400
WIDTH=400
TITLE="ALIEN SHOOTING GAME"

alien=Actor('alien')
alien.pos=50,50
message=" GAME STARTED "

def draw():
    screen.clear()
    screen.fill("blue")
    alien.draw()
    screen.draw.text(message,center=(200,20),fontsize=30,color="black")

def placeAlien():
    alien.x=random.randint(50,350)
    alien.y=random.randint(50,350)

def on_mouse_down(pos):
    print("hi")
    global message
    if alien.collidepoint(pos):
        message="Good Shot!"
        placeAlien()
    else:
        message="You Missed!"
        




    



placeAlien()

pgzrun.go()