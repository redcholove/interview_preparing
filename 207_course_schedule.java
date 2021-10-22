import java.util.*;

class Solution {
	public boolean canFinish(int numCourses, int[][] prerequisites) {
		//directed graph
		//bfs traversal node
		//tarversalNodes, visiting
		//path, degree
		Map<Integer, List<Integer>> path = new HashMap<Integer, List<Integer>>();
		Map<Integer, Integer> degree = new HashMap<Integer, Integer>();
		int visited = 0;
		Queue<Integer> visiting = new LinkedList<Integer>();

		for (int i = 0; i < numCourses; i++) {
			path.put(i, new ArrayList<Integer>());
			degree.put(i, 0);
		}

		for (int[] pre : prerequisites) {
			path.get(pre[1]).add(pre[0]);
			degree.replace(pre[0], degree.get(pre[0]) + 1);
		}
        
        for (Map.Entry<Integer, Integer> d : degree.entrySet()) {
            if (d.getValue() == 0) {
                visiting.add(d.getKey());
            }
        }
        
        while (!visiting.isEmpty()) {
            int cur = visiting.poll();
            visited += 1;
            
            for (int next : path.get(cur)) {
                degree.replace(next, degree.get(next) - 1);
                
                if (degree.get(next) == 0) {
                    visiting.add(next);
                }
            }
        }
        
        return visited == numCourses;
	}
}


public class Interview {
	public static void main(String[] args) {
		int[][] pre = new int[][] { {1,0}, {0, 1} };
		int numCourses = 2;
		
		Solution sol = new Solution();
		boolean result = sol.canFinish(numCourses, pre);
		System.out.println(result);
		System.out.println("success");
		System.out.println("time complexity: O(n)");
		System.out.println("space compelxity: O(n)");
	}
}
