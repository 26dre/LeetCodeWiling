public class twoSumSortedArray {
    public int[] twoSum(int[] numbers, int target) {
        int i = 0; 
        int j = numbers.length - 1; 
        while (i < j && numbers[i] + numbers[j] != target) {
            int sum = numbers[i] + numbers[j];
            if (sum < target) {
                System.out.println("Getting bigger");
                i++;
            } else if (sum > target) {
                System.out.println("Getting smaller");
                j--; 
            } 
       }

        if (i < j) {
            System.gc();
            return new int[] { i + 1, j + 1 };
        }

        System.gc();

       return null;
    } 
}
