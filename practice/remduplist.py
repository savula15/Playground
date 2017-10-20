import time

t0 = time.clock()
l = [1, 2, 3, 4, 5, 5, 6, 7, 7, 8, 8, 9]
s = []
for i in l:
      if i not in s:
            s.append(i)

t1 = time.clock()
print('time:{0}'.format(t1-t0))


t2 = time.clock()
l = [1, 2, 3, 4, 5, 5, 6, 7, 7, 8, 8, 9]
d = {t:m for t, m in enumerate(l)}

result = {}
for key, v in d.items():
      if v not in result.values():
            result[key] = v

s =[]
for j, k in result.items():
      s.append(k)
t3 = time.clock()
print('time:{0}'.format(t3-t2))


