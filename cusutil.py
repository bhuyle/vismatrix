import random
import time
from random import randint
from random import seed
seed(time.time)

def random_color():
    rgbl=[255,0,0]
    random.shuffle(rgbl)
    return tuple(rgbl)

def random_list_color(n):
    colors = []
    for i in range(n):
        r = randint(0, 255)
        g = randint(0, 255)
        b = randint(0, 255)
        colors.append([r,g,b])
    return colors

def gen_list_color(colors, cls):
    R = [x for x in range(255)]#[0, 50 , 100, 150, 200, 250]
    G = [x for x in range(255)]#[0, 50 , 100, 150, 200, 250]
    B = [x for x in range(255)]#[0, 50 , 100, 150, 200, 250]
    k = True
    while(k):
        k = False
        r = random.choice(R)
        g = random.choice(G)
        b = random.choice(B)
        for i in colors.keys():
            if colors[i] == [r,g,b]:
                k = True
    colors[cls] = [r,g,b]
    return colors
