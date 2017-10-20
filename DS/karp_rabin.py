class RollingHash:

    def __init__(self, s):
        self.HASH_BASE = 7
        self.seqlen = len(s)
        n = self.seqlen - 1
        h = 0
        for c in s:
            h += ord(c) * (self.HASH_BASE ** n)
            n -= 1
        self.currhash = h

    def hash(self):
        return self.currhash

    def slide(self, previtem, nextitem):
        self.currhash = (self.currhash * self.HASH_BASE) + ord(nextitem)
        self.currhash -= ord(previtem) * (self.HASH_BASE ** self.seqlen)
        return self.currhash


def substring(t, s):
    rs = RollingHash(s)
    hs = rs.hash()
    rt = RollingHash(t[:len(s)])
    ht = rt.hash()

    if hs == ht:
        if s == t[:len(s)]:
            return True
        else:
            return False
    else:
        for i in range(len(s), len(t)):
            rt.slide(t[i-len(s)], t[i])
            print(hs, rt.hash())
            if hs == rt.hash():
                if s == t[i-len(s)+1: i+1]:
                    return True
        else:
            return False


def find_prime(n):
    sqrt_n = n ** 0.5

    if n > 1:
        for i in range(2, sqrt_n):
            if n % i == 0:
                return n
            else:
                return 1
    else:
        return n


print(substring("this is awesome", "awe"))
print(substring("\0\A\C", "\0\B"))
