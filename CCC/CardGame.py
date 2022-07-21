cards = []
for i in range(52):
    cards.append(input())

scoreA = 0
scoreB = 0
player = "A"


def no_high(lst):
    if 'jack' in lst:
        return False
    if 'queen' in lst:
        return False
    if 'king' in lst:
        return False
    if 'ace' in lst:
        return False
    return True


for i in range(52):
    card = cards[i]
    points = 0
    if card == "jack" and i < 51 and no_high(cards[i+1:i+2]):
        points = 1
    elif card == "queen" and i < 50 and no_high(cards[i+1:i+3]):
        points = 2
    elif card == "king" and i < 49 and no_high(cards[i+1:i+4]):
        points = 3
    elif card == "ace" and i < 48 and no_high(cards[i+1:i+5]):
        points = 4

    if points > 0:
        print(f"Player {player} scores {points} point(s).")

    if player == "A":
        scoreA += points
        player = "B"
    else:
        scoreB += points
        player = "A"

print(f"Player A: {scoreA} point(s).")
print(f"Player B: {scoreB} point(s).")