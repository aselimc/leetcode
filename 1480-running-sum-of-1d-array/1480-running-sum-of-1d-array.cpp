class Solution {
public:
    vector<int> runningSum(vector<int>& nums) {
        vector<int> output(nums.size());
        for (int i=0; i<nums.size(); i++)
        {
            int sum = accumulate(nums.begin(), next(nums.begin(), i+1), 0);
            output[i] = sum;
        }
        return output;
    }
};