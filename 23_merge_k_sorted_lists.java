import java.util.*;

class ListNode {
    int val;
    ListNode next;
    
    public ListNode(int val) {
        this.val = val;
    }
}

class Solution {
    public ListNode mergeKLists(ListNode[] lists) {
        ListNode result = new ListNode(0);
        ListNode cur = result;
        
        PriorityQueue<ListNode> pq = new PriorityQueue<ListNode>(Comparator.comparing(info -> info.val));    
        
        for (ListNode cand : lists) {
            if (cand != null) {
                pq.add(cand);
            }
        }
        
        while (!pq.isEmpty()) {
            ListNode cand = pq.poll();
            
            cur.next = new ListNode(cand.val);
            cur = cur.next;
            cand = cand.next;
            
            if (cand != null) {
                pq.add(cand);
            }
        }
        return result.next;
    }
}

public class Interview {
    private static ListNode arrToList(int[] arr) {
        ListNode result = new ListNode(0);
        ListNode cur = result;
        
        for (int a : arr) {
            cur.next = new ListNode(a);
            cur = cur.next;
        }
        return result.next;
    }
    
    private static void printList(ListNode head) {
        ListNode cur = head;
        List<Integer> result = new ArrayList<Integer>();
        
        while (cur != null) {
            result.add(cur.val);
            cur = cur.next;
        }
        System.out.println(result);
    }
    
    public static void main(String[] args) {
        ListNode[] lists = new ListNode[3];
        lists[0] = arrToList(new int[]{1,4,5});
        lists[1] = arrToList(new int[]{1,3,4});
        lists[2] = arrToList(new int[]{2,6});
        Solution sol = new Solution();
        ListNode result = sol.mergeKLists(lists);
        printList(result);
        System.out.println("success");
        System.out.println("time complexity: O(n)");
        System.out.println("space complexity: O(n)");
    }
}


