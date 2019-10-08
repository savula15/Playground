''' Stackrox interview
'''
def genTrie(word, node):
    ''' Recursively builds trie for each word
    Updates trie datastructure using the given word
    '''

    if not word:
        return
    
    if word[0] not in node:
        node[word[0]] = {'valid': len(word) == 1, 'next': {}}

    genTrie(word[1:], node[word[0]])

def buildTrie(words, trie):
    ''' Build a trie datastructure from given words
    '''

    for word in words:
        genTrie(word, trie)
    return trie

def getNeighbors(r, c):
    '''Returns neighbors for given co-ordinates
    '''

    n = []
    for nbr in neighborsDelta:
        newR = r + nbr[0]
        newC = c + nbr[1]

        if newR >= lenr or newC >= lenc or newR < 0 or newC < 0:
            continue
        n.append(newR, newC)

    return n

def dfs(r, c, visited, trie, nowWord):
    if (r, c) in visited:
        return

    letter = boggle[r][c]
    visited.append((r,c))

    if letter in trie:
        nowWord += letter

        if trie[letter]['valid']:
            print(nowWord)
        
        neighbors = getNeighbors(r, c)
        for n in neighbors:
            dfs(n[0], n[1], visited[::], trie[letter], nowWord)
    
def main(trieNode):
    trie = buildTrie(words, trieNode)

    print('Given board')
    for i in range(lenr): print(boggle[i])

    for r in range(lenr):
        for c in range(lenc):
            dfs(r, c, [], trie, '')

if __name__ == '__main__':
    words = ['apple', 'pickle', 'side', 'kick', 'sick', 'mood', 'cat',
                 'cats', 'man', 'super', 'antman', 'godzilla', 'dog', 'dot',
                 'sine', 'cos', 'signal', 'bitcoin', 'cool', 'zapper']
    
    board = "cntss datin oomel siknd picle".split()
    boggle = [list(astr) for astr in board]

    lenr = len(boggle[0])
    lenc = len(boggle)

    neighborsDelta = [
        (-1, -1),
        (-1, 0),
        (-1, 1),
        (0, 1),
        (1, 1),
        (1, 0),
        (1, -1),
        (0, -1)
    ]

    trieNode = {'valid': False, 'next': {}}

    main(trieNode)

    


