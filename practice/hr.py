n = int(input('enter').strip())
a = []
dsumleft = 0
dsumright = 0
for i in range(n):
    a_t = [int(a_temp) for a_temp in input('enter2').strip().split(' ')]
    a.append(a_t)
    dsumleft += int(a[i][i])
    dsumright += int(a[-(i+1)][-(i+1)])
    if i < n-1:
        continue
    else:
          print(dsumleft, dsumright)
          print(abs(dsumleft - dsumright))
