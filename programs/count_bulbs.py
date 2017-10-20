def count_bulbs(a):
    turnon = 0

    for i in a:
        if i == 0 and turnon % 2 == 0:
            turnon += 1
        elif i == 1 and turnon % 2 == 1:
            turnon += 1
    return turnon

print(count_bulbs([0, 1, 0, 1, 0, 0, 0, 1, 1, 1, 0]))
