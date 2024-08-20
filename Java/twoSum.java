import java.util.HashMap; // import the HashMap class


class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> res_to_pos = new HashMap<Integer, Integer>();


        for (int i = 0; i < nums.length; i++) {
            Integer curr = nums[i]; 
            if (res_to_pos.containsKey(target - curr)) {
                int[] ret = {res_to_pos.get(target - curr), i};
                return ret; 
            } else {
                res_to_pos.put(curr, i);
            }
        }

        return null;
    }
}

// public class Main_class {
//     void main() {
//         System.out.println("Hello world");
//     }
// }