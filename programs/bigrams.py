import pytest

def bigrams(text):

    text = ["this is a sentence", "so is this one"]
    bigrams = [b for l in text for b in zip(l.split(" ")[:-1], l.split(" ")[1:])]

    return(bigrams)

assert(bigrams(["this is a sentence", "so is this one"])) == [('this', 'is'), ('is', 'a'), ('a', 'sentence'), ('so', 'is'), ('is', 'this'), ('this',
'one')]
