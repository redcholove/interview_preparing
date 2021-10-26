class Solution {
    public int[] findOrder(int numCourses, int[][] prerequisites) {
        //topological sort
        
        //build path
        
        //build degree
        
        //find degree 0
        
        //build visiting, build visited
        
        //traversal degree, path
        
        //return visited
        
        ArrayList<Integer> visited = new ArrayList<Integer>();
        HashMap<Integer, List<Integer>> path = new HashMap<Integer, List<Integer>>();
        HashMap<Integer, Integer> degree = new HashMap<Integer, Integer>();
        Queue<Integer> visiting = new LinkedList<Integer>();
        for (int i = 0; i < numCourses; i ++) {
            path.put(i, new ArrayList<Integer>());
            degree.put(i, 0);
        }
        
        for (int[] pre : prerequisites) {
            path.get(pre[1]).add(pre[0]);
            degree.replace(pre[0], degree.get(pre[0]) + 1);
        }
        
        for (Map.Entry<Integer, Integer> d : degree.entrySet()) {
            if (d.getValue() == 0) {
                degree.replace(d.getKey(), degree.get(d.getKey()) - 1);
                visiting.add(d.getKey());
            }
        }
        
        while (!visiting.isEmpty()) {
            Integer cur = visiting.poll();
            visited.add(cur);
            for (Integer p : path.get(cur)) {
                degree.replace(p, degree.get(p) - 1);
                if (degree.get(p) == 0) {
                    visiting.add(p);
                }
            }
        }
        if (visited.size() != numCourses) {
            return new int[0];
        }
        
        int[] result = new int[visited.size()];
        for (int i = 0; i < result.length; i ++) {
            result[i] = visited.get(i);
        }
        return result;
    }
}
