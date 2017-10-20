import os
os.chdir("/Users/saavula/Documents/Python/practice")

with open("alice.txt") as fh:
      count = sum(character.isupper() for line in fh for character in line)
      print(count)
      
