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

    def getAll(self, ptr, rec, ans):

        for i in sorted(ptr.children.keys()):
            rec[i].append(self.getAll(ptr.children[i], rec, ans + i))



