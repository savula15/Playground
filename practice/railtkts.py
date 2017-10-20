def max_rev(n, a1, a2, m):

      trev = 0
      i = 0
      while i < m:

            trev













      return trev


if __name__ == '__main__':
      
      n = int(input('enter no of windows:'))
      a1 = int(input('a1 tkts available:'))
      a2 = int(input('a2 tkts available:'))
      m = int(input('tkts sold:'))

      print('no of windows {0}'.format(n))
      print('a1 tkts {0}'.format(a1))
      print('a2 tkts {0}'.format(a2))
      print('tkts sold {0}'.format(m))
 
      rev = max_rev(n, a1, a2, m)
      print(rev)
               
