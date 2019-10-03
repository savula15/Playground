def anagram1(s1, s2):
    '''Algorithm that uses Checking off technic

    Runtime: n(n+1)/2 which is equal to O(n^2)
    '''

    if len(s1) == 0 or len(s2) == 0 or (len(s1) != len(s2)):
        return -1

    alist = list(s2)

    pos1 = 0
    still_ok = True

    while pos1 < len(s1) and still_ok:
        pos2 = 0
        found = False
        while pos2 < len(alist) and not found:
            if s1[pos1] == alist[pos2]:
                found = True
            else:
                pos2 += 1

        if found:
            alist[pos2] = None
        else:
            still_ok = False

        pos1 += 1

    return still_ok


print(anagram1('abcd', 'cdba'))
print(anagram1('abde', 'cdba'))


def anagram2(s1, s2):
    '''Algorithm that sorts two strings after converting them into lists and then compares to see
    if they are equal and determine if they are indeed are anagrams

    Runtime: Will be same as sort as sort might take O(n^2) or O(nlogn) and be careful not to
    deceive by looking "just" at "while" loop
    '''

    # alist1 = list(s1)
    # alist2 = list(s2)

    # alist1.sort()
    # alist2.sort()

    alist1 = sorted(s1)
    alist2 = sorted(s2)

    pos = 0
    matches = True

    while pos < len(alist1) and matches:
        if alist1[pos] == alist2[pos]:
            pos += 1
        else:
            matches = False

    return matches

print(anagram2('abcd', 'cdba'))
print(anagram2('abde', 'cdba'))


def anagram3(s1, s2):
    ''' Brute force method where in idea is to generate all possible strings from characters in s1
    and then checking if s2 is one of them.

    When generating all possible strings from s1, there are n possible first characters,
    n−1 possible characters for the second position, n−2 for the third, and so on.
    The total number of candidate strings is n∗(n−1)∗(n−2)∗...∗3∗2∗1 which is  "n!"

    It turns out that n! grows even faster than 2^n as n gets large.
    In fact, if s1 were 20 characters long, there would be 20!=2,432,902,008,176,640,000 possible
    candidate strings. If we processed one possibility every second,
    it would still take us 77,146,816,596 years to go through the entire list.

    This is not a good solution et all

    '''

    pass


# def anagram4(s1, s2):
#     ''' Algorithm that takes approach of counting occurances of characters in each string and
#     then compare two count lists if they are equal.

#     If they are equal then s1 and s2 are anagrams else they are not
#     '''

#     c1 = [0] * 26  # This is because there are 26 alphabets
#     c2 = [0] * 26

#     for i in range(len(s1)):
#         pos = ord(s1[i]) - ord('a')
#         c1[pos] += 1

#     for i in range(len(s2)):
#         pos = ord(s2[i]) - ord('a')
#         c2[pos] += 1

#     j = 0
#     still_ok = True

#     while j < 26 and still_ok:
#         if c1[j] == c2[j]:
#             j += 1
#         else:
#             still_ok = False
#     return still_ok

def anagram4(s1, s2):
    ''' O(n) and space O(1) needs for count chars
    also optimizes by using only counter list
    '''

    if not s1 or not s2 or len(s1) != len(s2):
        return False

    c = [0] * 256

    for i in range(len(s1)):
        pos = ord(s1[i]) - ord('a')
        c[pos] += 1
    for j in range(len(s2)):
        pos = ord(s2[j]) - ord('a')
        c[pos] -= 1

    return not any(c)

print(anagram4('abcd', 'cdba'))
print(anagram4('abde', 'cdba'))


def anagram_list(alist):
    """Given a text or list of words, segragate words into anagram buckets

    The  running  time  is  O(n log n)  for  sorting  the  string  (which  is  relatively  small) 
    and  approximately  O(1)  for  the  lookup  in  the  hash table.

    """

    result = {}

    for word in alist:
        temp = ''.join(sorted(word))
        if temp in result.keys():
            result[temp].append(word)
        else:
            result[temp] = [word]
    return result

print(anagram_list(['abets', 'baste', 'betas', 'abut', 'tabu', 'tuba', 'acre', 'care', 'race']))
