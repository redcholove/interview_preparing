class TrieNode:
    def __init__(self):
        self.children = {}
        self.endWord = False

class Trie:

    def __init__(self):
        #treenode + endWord flag
        self.root = TrieNode()

    def insert(self, word):
        cur = self.root
        for w in word:
            if w not in cur.children:
                newWord = TrieNode()
                cur.children[w] = newWord
            cur = cur.children[w]
    
        cur.endWord = True

    def search(self, word):
        cur = self.root

        for w in word:
            if w not in cur.children:
                return False
            
            cur = cur.children[w]
        if cur.endWord:
            return True
        return False

    def startsWith(self, prefix):
        cur = self.root
        
        for p in prefix:
            if p not in cur.children:
                return False
            cur = cur.children[p]
        return True

if __name__ == '__main__':
    trie = Trie()
    print(trie.insert('fuck'), trie.insert('fuckyou'), trie.insert('test'), trie.search('fuck'), trie.search('fu'), trie.startsWith('f'))
