def solveMaze(r, c):
    if r == (size - 1) and c == (size - 1):
        sol[r][c] = 1
        return True
    
    if r >= 0 and c >= 0 and r < size and c < size and sol[r][c] == 0 and maze[r][c] == 0:
        sol[r][c] = 1
        if solveMaze(r + 1, c):
            return True
        if solveMaze(r, c + 1):
            return True
        if solveMaze(r - 1, c):
            return True
        if solveMaze(r, c - 1):
            return True
        sol[r][c] = 0
        return False

size = 5
maze = [
    [0,1,0,1,1],
    [0,0,0,0,0],
    [1,0,1,0,1],
    [0,0,1,0,0],
    [1,0,0,1,0]
]

sol = [[0] * size for _ in range(size)]

if solveMaze(0, 0):
    for i in sol:
        print(i)
else:
    print('No solution')

