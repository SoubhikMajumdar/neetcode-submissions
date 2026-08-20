class Solution {
public:
    void sortColors(vector<int>& nums) {
        unordered_map<int, int> freq;

        for (int n : nums) {
            freq[n]++;
        }

        vector<int> result;

        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < freq[i]; j++) {
                result.push_back(i);
            }
        }

        nums = result;
    }
};