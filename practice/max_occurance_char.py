import operator


def max_occurance(mystr):
      
      r = list(mystr)
      results = {}
      mr = None
      cnt1 = 0
      cnt2 = 0
      for e in r:
        if e == mr:
                cnt1 += 1
                mr = e
        elif e != mr and len(r) > 0:
                if cnt1 > cnt2:
                        results[mr] = cnt1
                elif mr != None:
                        results[mr] = cnt2
                mr = e
                cnt1 = 1
                cnt2 = 1
                continue
      return results

s = 'abcdeeeffghijjjjkeeeee'

stats = max_occurance(s)
print(stats)

print(max(stats.items(), key=operator.itemgetter(1))[0])
