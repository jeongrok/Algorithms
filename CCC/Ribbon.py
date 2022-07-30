lst = [int(value) for value in input().split()]
length = lst[0]
n = lst[1]

strokes = []
for i in range(n):
    stroke = [int(value) for value in input().split()]
    strokes.append(stroke)

strokes.sort()
blue = strokes[0][1] - strokes[0][0]
right_most = strokes[0][0]
left_most = strokes[0][1]
for j in strokes:
    if j[1] > left_most:
        if j[0] > left_most:
            blue += j[1] - j[0]
            right_most = j[0]
            left_most = j[1]
        blue += j[1] - left_most
        left_most = j[1]

print(length - blue, blue)