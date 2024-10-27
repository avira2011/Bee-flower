import pgzrun
import random
import itertools


WIDTH = 400
HEIGHT = 400


bee = Actor('bee', center = (50,50))
flower = Actor('flower', center = (200,200))

bee_positions = [(50,50), (350,50), (350,350), (50, 350)]
position_bee = itertools.cycle(bee_positions)


def draw():
    screen.clear()
    bee.draw()
    flower.draw()

def move_bee():
    animate(bee, 'bounce_end', duration = 2, pos = next(position_bee))

move_bee()

clock.schedule_interval(move_bee, 2)


pgzrun.go()