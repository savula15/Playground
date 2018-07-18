def longest_increasing_seq(A):

  '''Returns the max size of LIS
  '''
  n = len(A)
  li = [1] * n

  for i in range(1, n):
    for j in range(0, i):
      if A[i] > A[j] and li[i] < li[j] + 1:
        li[i] = li[j] + 1

  maximum = 0

  for i in range(n):
    maximum = max(maximum, li[i])

  return maximum

def longest_increasing_seq2(A):
  '''Returns the actual LIS list
  '''

  l = []

  for i in range(len(A)):
    l.append(max([l[j] for j in range(i) if l[j][-1] < A[i]] or [[]], key=len) + [A[i]])

  return max(l, key=len)

