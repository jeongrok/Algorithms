sentence = input()

a = "a"
count = 0

for char in sentence:
    if char == "H" and a == "a":
        a = "b"
    if char == "O" and a =="b":
        a = "c"
    if char == "N" and a =="c":
        a = "d"
    if char == "I" and a == "d":
        count += 1
        a = "a"

print(count)

# sentence = input()
# p = ["H", "O", "N", "I"]
# result = 0
#
# h = p[result]
#
# for i in range(len(sentence)):
#     if sentence[i] == h:
#         result += 1
#         h = p[result % 4]
#
# print (result // 4)