class Solution {
public:
    int pivotIndex(vector<int>& nums) {      
        int *left = &nums[0];
        int *middle =left;
        int *right = &nums[nums.size() - 1];

        long left_sum = accumulate(left, middle, 0);
        long right_sum = accumulate(middle + 1, right + 1, 0);

        while (middle != right)
        {
            if (left_sum == right_sum)
                return middle - left;
            
            else
            {
                left_sum += *middle;
                right_sum -= *(middle+1);
                middle++;
            }
        }
        if (left_sum == right_sum)
                return middle - left;
        return -1;
    }
};