class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors

class Solution:
    def cloneGraph(self, node):
        #return a 'deep copy' from the graph
        #他是undirected -> 所以要記錄visited 不然會進入cycle停不下來
        #dfs or bfs
        
        #先try dfs
        visited = {}

        def dfs(node):
            if not node:
                return 
            
            if node in visited:
                return visited[node]
            
            clone = Node(node.val, [])
            visited[node] = clone

            for n in node.neighbors:
                clone.neighbors.append(dfs(n))

            return clone
        return dfs(node)
        


if __name__ == '__main__':
    sol = Solution()
    result = sol.cloneGraph(node)
    print(result)
    print('success')
    print('懶得 寫graph test')
    print('time complexity: O(n)')
    print('space comlexity: O(n)')

