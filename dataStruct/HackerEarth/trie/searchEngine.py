class TrieNode:
    def __init__(self):
        self.children = {}
        # self.pr = []
        self.maxChildren = 0

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, st, p):
        temp = self.root
        for i in range(len(st)):
            if temp.children.get(st[i], 0) == 0:
                temp.children[st[i]] = TrieNode()
                # temp.pr.append(p)
                temp.maxChildren = max(temp.maxChildren, p)
            temp = temp.children[st[i]]

    def getPrior(self, st):
        temp = self.root
        for i in range(len(st)):
            if temp.children.get(st[i], 0) == 0:
                return -1
            temp = temp.children[st[i]]
        return temp.maxChildren

t = Trie()
n, q = map(int, input().split())
for i in range(n):
    st, p = input().split()
    t.insert(st, int(p))

for i in range(q):
    s = input()
    print(t.getPrior(s))