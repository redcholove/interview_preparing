class Trie:
    def __init__(self):
        self.children = {}
        self.endWord = False

class WordDictionary:
    #直覺兩種方法 trie, hashmap
    def __init__(self):
        self.root = Trie()

    def addWord(self, word):
        cur = self.root
        for w in word:
            if w not in cur.children:
                cur.children[w] = Trie()
            cur = cur.children[w]
        cur.endWord = True

    def search(self, word):
        # . -> 代表任一字母
        cur = self.root

        def dfs(cur, word):
            if len(word) == 0:
                if cur.endWord: return True
                else: return False
            
            res = False

            if word[0] == '.':
                for c in cur.children:
                    res = res or dfs(cur.children[c], word[1:])
            else:
                if word[0] in cur.children:
                    res = dfs(cur.children, word[1:])
            
            return res
        return dfs(cur, word)

if __name__ == '__main__':
    print('success')
