
#include <stdio.h>
int getMinIdx(int* nums, int numsSize) {
    int minIdx = 0; 
    for (int i = 1; i < numsSize; i++) {
        if (nums[i] < nums[minIdx]) {
            minIdx = i; 
        }
    }
    return minIdx; 
}
int getMaxIdx(int* nums, int numsSize) {
    int maxIdx = 0; 
    for (int i = 1; i < numsSize; i++) {
        if (nums[i] > nums[maxIdx]) {
            maxIdx = i; 
        }
    }
    return maxIdx; 
}

int minDifSubroutine(int* nums, int numsSize, int minIdx, int maxIter) {
    for (int curr_iter = 0; curr_iter < maxIter; curr_iter++) {
        int curr_max_idx = getMaxIdx(nums, numsSize);

        nums[curr_max_idx] = nums[minIdx];
    }

    printf("Resulting array\n");
    for (int i = 0; i < numsSize; i++) {
        printf("%d ", nums[i]);
    }


    int resulting_diff = 0; 
    int curr_min = nums[minIdx];
    for (int i = 0; i < numsSize; i++) {
        resulting_diff += nums[i] - curr_min; 
    }

    return resulting_diff; 
}


int minDifference(int* nums, int numsSize) {

    if (numsSize <= 3) {
        return 0; 
    }
    int curr_mind_idx = getMinIdx(nums, numsSize);

    return minDifSubroutine(nums, numsSize, curr_mind_idx, 3);


}

int* get_4_biggest_idx (int* nums, int numsSize) {
    // get 4 biggest
    // get 4 smallest
    // sort those then alter top 3 and bottom 3 and evaluate each result
    // return smallest result
    return NULL;
}

int main() {
    int arr[] = {1, 2, 3, 4};
    int arr_len = 4; 
    minDifference(arr, arr_len);
    return 0; 
}