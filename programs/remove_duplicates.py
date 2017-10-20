def remove_duplicates(l):
    seen = set()
    seen_add = seen.add
    return [x for x in l if not (x in seen or seen_add(x))]


l = [1, 2, 1, 2, 3, 4, 4, 5, 6, 3]
print(remove_duplicates(l))
