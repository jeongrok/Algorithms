# One day, little Mirko came across a funny looking machine!
# It consisted of a very very large screen and a single button.
# When he found the machine, the screen displayed only the letter A.
# After he pressed the button, the letter changed to B.
# The next few times he pressed the button, the word transformed from B to BA, then to BAB, then to BABBA.
# When he saw this, Mirko realized that the machine alters the word in a way that
# all the letters B get transformed to BA and all the letters A get transformed to B.
#
# Amused by the machine, Mirko asked you a very difficult question!
# After K times of pressing the button, how much letters A and how much letters B will be displayed on the screen?


# my submission using Fibonacci sequence
n = int(input())

a = 0
b = 1
result = 0

if n != 1:
    for i in range(n - 1) :
        result = a + b
        a = b
        b = result

print(a, b)
