def knapsack(val, wt, W, n)::
    '''https://en.wikipedia.org/wiki/Knapsack_problem

    A Dynamic Programming for 0-1 Knapsack problem
    Returns the maximum value that can be put in a knapsack of capacity W

    varr:   Values (stored in array v)
    wtarr:  Weights (stored in array w)
    n:      Number of distinct items (n)
    W:      Knapsack capacity (W)

    Note: The array "varr" and array "wtarr" are assumed to store all relevant values starting at index 1

    Time Complexity: O(nW) where n is the number of items and W is the capacity of knapsack.

    '''
    K = [[0 for x in range(W+1)] for x in range(n+1)]

    # Build table K[][] in bottom up manner
    for i in range(n+1):
        for w in range(W+1):
            if i == 0 or w == 0:
                K[i][w] = 0
            elif wt[i-1] <= w:
                K[i][w] = max(val[i-1] + K[i-1][w-wt[i-1]], K[i-1][w])
            else:
                K[i][w] = K[i-1][w]

    return K[n][W]


val = [60, 100, 120]
wt = [10, 20, 30]
W = 50
n = len(val)
print(knapsack(val, wt, W, n))




