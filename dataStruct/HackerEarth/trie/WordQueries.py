class TrieNode:
    def __init__(self):
        self.children = {}
        # self.pr = []
        self.numChildren = 0

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, st):
        temp = self.root
        for i in range(len(st)):
            if temp.children.get(st[i], 0) == 0:
                temp.children[st[i]] = TrieNode()
                # temp.pr.append(p)
            temp.numChildren += 1
            temp = temp.children[st[i]]
        temp.numChildren += 1
    def getPrior(self, st):
        temp = self.root
        for i in range(len(st)):
            if temp.children.get(st[i], 0) == 0:
                return 0
            temp = temp.children[st[i]]
        return temp.numChildren
t = Trie()
n, q = map(int, input().split())
for i in range(n):
    t.insert(input())

for i in range(q):
    print(t.getPrior(input()))
