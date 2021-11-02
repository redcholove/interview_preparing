class Node {
    int i;
    int j;
    int val;
    
    public Node(int i, int j, int val) {
        this.i = i;
        this.j = j;
        this.val = val;
    }
}
class Solution {
    
    public int kthSmallest(int[][] matrix, int k) {
        //priorityQueue
        
        //merge sort -> flow
        //先把所有row的[0] 丟進去 
        //pop 最小的出來 -> 把那個row的下一個col丟進去
        //直到visited.size() == k
        PriorityQueue<Node> pq = new PriorityQueue<Node>((n1, n2) -> n1.val - n2.val);
        List<Integer> visited = new ArrayList<Integer>();
        
        for (int i = 0; i < matrix.length; i ++) {
            Node cur = new Node(i, 0, matrix[i][0]);
            pq.add(cur);
        }
        
        while(visited.size() < k) {
            Node visiting = pq.poll();
            visited.add(visiting.val);
            
            if (visiting.j != matrix[0].length - 1) {
                int newX = visiting.i;
                int newY = visiting.j + 1;
                Node cur = new Node(newX, newY, matrix[newX][newY]);
                pq.add(cur);
            }
        }        
        
        System.out.println(visited);
        return visited.get(visited.size()-1);
        //binary search
        
    }
}
