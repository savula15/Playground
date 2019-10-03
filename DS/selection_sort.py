def selection_sort(A):
    '''Runtime: O(n**2) performs better when compared to bubble sort
    This is due to the reduction in the number of exchanges'''

    for fillslot in range(len(A)-1, 0, -1):
        position_of_max = 0
        for location in range(1, fillslot+1):
            if A[location] > A[position_of_max]:
                position_of_max = location

            A[fillslot], A[position_of_max] = A[position_of_max], A[fillslot]

    return A

print(selection_sort([54, 26, 93, 17, 77, 31, 44, 55, 20]))
