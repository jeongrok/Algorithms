# Luka is fooling around in chemistry class again!
# Instead of balancing equations he is writing coded sentences on a piece of paper.
# Luka modifies every word in a sentence by adding, after each vowel (letters a, e, i, o and u),
# the letter p and then that same vowel again.
#
# For example, the word kemija becomes kepemipijapa and the word paprika becomes papapripikapa.
# The teacher took Luka's paper with the coded sentences and wants to decode them.

sentence = input()

i = 0
result = ""
while i < len(sentence):
    result += sentence[i]
    if sentence[i] in 'aeiou':
        i += 3
    else:
        i += 1

print(result)