#include <unordered_map>
#include <vector>
class Solution
{
public:
    std::vector<int> twoSum(std::vector<int> &nums, int target)
    {
        std::unordered_map<int, int> h_map;
        for (int i = 0; i < nums.size(); i++)
        {
            int curr_num = nums[i];
            if (h_map.count(target - curr_num) >= 1)
            {
                return {h_map[target - curr_num], i};
            }
            else
            {
                h_map[curr_num] = i;
            }
        }
    }
};