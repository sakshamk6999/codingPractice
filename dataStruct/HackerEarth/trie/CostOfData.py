class TrieNode:
    def __init__(self):
        self.children = [None for i in range(26)]

class Trie:
    def __init__(self):
        self.root = TrieNode()
        self.nodes = 1

    def insert(self, st):
        temp = self.root
        n = len(st)
        for i in range(n):
            if temp.children[ord(st[i])-ord('a')] == None:
                self.nodes += 1
                temp.children[ord(st[i])-ord('a')] = TrieNode()
            temp = temp.children[ord(st[i])-ord('a')]
t = Trie()
for _ in range(int(input())):
    t.insert(input())

print(t.nodes)


