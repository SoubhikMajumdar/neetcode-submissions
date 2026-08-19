class Solution {
public:
    bool isMonotonic(vector<int>& nums) {
        bool decreasing = true;
        bool increasing = true;
        for (int i = 1; i < nums.size(); i++) {
            if (nums[i] > nums[i-1]){
                decreasing = false;
            }
            if (nums[i] < nums[i-1]){
                increasing = false;
            }
        }
        return increasing or decreasing;
    }
};