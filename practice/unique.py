from collections import Counter

c = Counter()


def unique_num(mylist):

    l = len(mylist)

    while l > 0:
        for i in mylist:
            c[i] += 1
            l -= 1

            uniques = []
            for k, v in c.items():
                if v == 1:
                    uniques.append(k)

    return uniques
