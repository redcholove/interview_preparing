class Trie:
    def __init__(self):
        self.children = {}
        self.endWord = False
        self.found = False

class Solution:
    def buildTrie(self, words):
        trie = Trie()

        for w in words:
            cur = trie
            for i in range(len(w)):
                if w[i] not in cur.children:
                    cur.children[w[i]] = Trie()
                cur = cur.children[w[i]]
            cur.endWord = True
        return trie

    def findWords(self, board, words):
        #matrix裡面找符合字串的path
        #直覺 dfs 一個一個找 或是build 一個trie
        #但感覺兩者都很花resource
        #反向思考 做words的trie????
        
        #build words trie
        #for loop board traversal ele
        result = []
        wLen = len(words)

        if wLen == 0:
            return result

        trie = self.buildTrie(words)

        def dfs(board, cur, i, j, path):
            if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]):
                return

            if board[i][j] not in cur.children:
                return
            
            if cur.children[board[i][j]].endWord:
                if not cur.children[board[i][j]].found:
                    result.append(path+board[i][j])
                    cur.children[board[i][j]].found = True

            tmp = board[i][j]
            board[i][j] = '#'
    
            dfs(board, cur.children[tmp], i+1, j, path+tmp)
            dfs(board, cur.children[tmp], i-1, j, path+tmp)
            dfs(board, cur.children[tmp], i, j+1, path+tmp)
            dfs(board, cur.children[tmp], i, j-1, path+tmp)
            board[i][j] = tmp
    
        for i in range(len(board)):
            for j in range(len(board[0])):
                cur = trie
                dfs(board, cur, i, j, '')
        return result
        

if __name__ == '__main__':
    sol = Solution()
    #board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]]
    #words = ["oath","pea","eat","rain"]
    board = [["o","a","b","n"],["o","t","a","e"],["a","h","k","r"],["a","f","l","v"]]
    words = ["oa","oaa"]
    result = sol.findWords(board, words)
    print(result)
    print('success')
    print('time complexity: O(m*n*4^l)')
    print('space complexity: O(sum(l) + l)')
