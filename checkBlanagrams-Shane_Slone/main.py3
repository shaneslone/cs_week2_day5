def checkBlanagrams(word1, word2):
    w1 = {}
    diff_total = 0
    for char in word1:
        if char in w1:
            w1[char] += 1
        else:
            w1[char] = 1
    for char in word2:
        if char in w1:
            if w1[char] > 0:
                w1[char] -= 1
    for key in w1:
        diff_total += w1[key]
    return diff_total == 1