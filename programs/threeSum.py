def threeSum(A, target):
    n = len(A)
    triplets = set()
    for i in range(0, n-1):
        s = set()
        currentSum = target - A[i]
        for j in range(i+1, n):
            if currentSum - A[j] in s:
                triplets.add((A[i], A[j], currentSum-A[j]))
            s.add(A[j])
    return triplets

def threeSumClosest(A, target):
    n = len(A)
    alist = sorted(A)
    closestSum = sum(A[:3])
    closestTriplet = A[:3]
    for i in range(n-2):
        i, j = i+1, n-2
        while j < k:
            temp = alist[i] + alist[j] + alist[k]
            if abs(target - temp) <= abs(target - closestSum):
                closestSum = temp
                closestTriplet = [alist[i], alist[j], alist[k]]
            if temp < target:
                j += 1
            else:
                k -= 1
    return closestSum, closestTriplet

