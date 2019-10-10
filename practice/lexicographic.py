def isLexicographicallySorted(words, alpha):
    """
    Time: O(n+m), n -> number of words, m -> length word
    Space: O(n), n -> length of alpha/dictionary
    """
    d = {}
    for index, ch in enumerate(alpha):
        d[ch] = index

    i = 1
    while i < len(words):
        word1, word2 = words[i - 1], words[i]
        for b in zip(word1, word2):
            if not d[b[0]] <= d[b[1]]:
                return False
        i += 1

    return True

words = ["cc", "bc", "ac"]
alpha = ["c", "b", "a"]

print(isLexicographicallySorted(words, alpha))
