# cco99p2

def inverted_dict(d):
    inverted = {}
    for key in d:
        num = d[key]
        if not num in inverted:
            inverted[num] = [key]
        else:
            inverted[num].append(key)
    return inverted


def add_suffix(num):
    s = str(num)
    if s[-1] == '1' and s[-2:] != '11':
        return s + 'st'
    elif s[-1] == '2' and s[-2:] != '12':
        return s + 'nd'
    elif s[-1] == '3' and s[-2:] != '13':
        return s + 'rd'
    else:
        return s + 'th'


def most_commonwords(num_to_words, k):
    nums = list(num_to_words.keys())
    nums.sort(reverse=True)
    total = 0
    i = 0
    done = False
    while i < len(nums) and not done:
        num = nums[i]
        if total + len(num_to_words[num]) >= k:
            done = True
        else:
            total = total + len(num_to_words[num])
            i += 1
    if total == k - 1 and i < len(nums):
        return num_to_words[nums[i]]
    else:
        return []


n = int(input())
for i in range(n):
    index = [int(value) for value in input().split()]
    m, k = index[0], index[1]

    word_to_num = {}
    for i in range(m):
        word = input()
        if not word in word_to_num:
            word_to_num[word] = 1
        else:
            word_to_num[word] += 1
    num_to_words = inverted_dict(word_to_num)
    ordinal = add_suffix(k)
    words = most_commonwords(num_to_words, k)

    print(f'{ordinal} most common word(s):')
    for word in words:
        print(word)

    print()
