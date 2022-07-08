import math
for i in range(10):

    looper = True
    orange, blue, green, yellow, pink, violet, brown, red = 0, 0, 0, 0, 0, 0, 0, 0

    while looper:
        word = input()
        if word == "end of box":
            break
        elif word == "orange":
            orange += 1
        elif word == "blue":
            blue += 1
        elif word == "green":
            green += 1
        elif word == "yellow":
            yellow += 1
        elif word == "pink":
            pink += 1
        elif word == "violet":
            violet += 1
        elif word == "brown":
            brown += 1
        elif word == "red":
            red += 1
    result = (math.ceil(orange / 7)) * 13 + (math.ceil(blue / 7)) * 13 + (math.ceil(green / 7)) * 13 + (math.ceil(yellow / 7)) * 13 + (math.ceil(pink / 7)) * 13 + (math.ceil(violet / 7)) * 13 + (math.ceil(brown / 7)) * 13 + red  * 16
    print(result)