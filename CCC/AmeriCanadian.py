# The user should type a word (not to exceed 64 letters) and if the word appears to use American spelling, the program should echo the Canadian spelling for the same word.
# If the word does not appear to use American spelling, it should be output without change.
# When the user types quit! the program should terminate.
#
# The rules for detecting American spelling are quite naive:
# If the word has more than four letters and has a suffix consisting of a consonant followed by or,
# you may assume it is an American spelling, and that the equivalent Canadian spelling replaces
# the or by our. Note: you should treat the letter y as a vowel.

looper = True # using loopers
while looper:
    word = input()
    if word == 'quit!':
        break
    elif len(word) > 3:
        p = len(word)
        for x in range(p):
            if not word[p-3] in 'aeiouy' and word[p-2 : p] == "or":
                print(word.replace("or", "our"))
                break
            else:
                print(word)
                break
        else:
            print(word)
