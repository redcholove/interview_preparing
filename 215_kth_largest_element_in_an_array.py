class Solution {
    public int findKthLargest(int[] nums, int k) {
        //直覺 quick select 但我不會寫
        
        //priority Queue -> minimum tree/ insert O(logn) / get O(1)
        
        PriorityQueue<Integer> pq = new PriorityQueue<Integer>();
        for (int n : nums) {
            pq.add(n);
            
            if (pq.size() > k) {
                pq.poll();
            }
        }
        
        return pq.poll();
    }
}
