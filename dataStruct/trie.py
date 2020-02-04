class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False
class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, st):
        temp = self.root
        n = len(st)
        for i in range(n):
            if temp.children.get(st[i], 0) == 0:
                temp.children[st[i]] = TrieNode()
            temp = temp.children[st[i]]
        temp.isEnd = True

    def search(self, st):
        temp = self.root
        n = len(st)
        for i in range(n):
            if temp.children.get(st[i], 0) == 0:
                return False
            temp = temp.children[st[i]]

        return temp.isEnd


for _ in range(int(input())):
    n = int(input())
    s = input().split()
    t = list(input())
    tr = Trie()
    for i in t:
        tr.insert(i)
    print(1 if tr.search(input()) else 0)