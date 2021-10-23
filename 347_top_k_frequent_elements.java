import java.util.Map;
import java.util.HashMap;
import java.util.PriorityQueue;
import java.util.Comparator;
import java.util.List;
import java.util.ArrayList;

class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        Map<Integer, Integer> map = new HashMap<Integer, Integer>();
        PriorityQueue<Map.Entry<Integer, Integer>> pq = new PriorityQueue<Map.Entry<Integer, Integer>>(Comparator.comparing(info -> info.getValue()));
        for (int n : nums) {
            if ( map.containsKey(n) ) {
                map.replace( n, map.get(n) + 1 );
            } else {
                map.put( n, 1 );
            }
        }
        for ( Map.Entry<Integer, Integer> ele : map.entrySet() ) {
            pq.add( ele );
            
            if ( pq.size() > k ) {
                pq.poll();
            }
        }
        
        int[] result = new int[k];
        for (int i = 0; i < k; i ++) {
            result[i] = pq.poll().getKey();
        }
        
        return result;
    }
}
public class HelloWorld{

     public static void main(String []args){
        int[] nums = new int[] {1,1,1,2,2,3};
        int k = 2;
        
        Solution solution = new Solution();
        int[] result = solution.topKFrequent(nums, k);
        List<Integer> forPrint = new ArrayList<Integer>();
        for (int i = 0; i < result.length; i ++) {
            forPrint.add(result[i]);
        }
        System.out.println(forPrint);
     }
}
