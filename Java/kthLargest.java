import java.util.PriorityQueue;
public class kthLargest {
    public int findKthLargest(int[] nums, int k) {

        PriorityQueue<Integer> currQueue = new PriorityQueue<>((a, b) -> a-b);

        for (int number: nums) {
            currQueue.add(number);
        }

        for (int i = 0; i < k; i++) {
            currQueue.remove(); 
        }

        

        return currQueue.peek();
    }
}
