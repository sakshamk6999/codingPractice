import random

for i in random(1, 11):
    fi = open("input" + str(i) + ".txt", "w")
    fo = open("output" + str(i) + ".txt", "w")

    t = random.randint(i*9, 100)

    c = random.randint(1, t)
    for