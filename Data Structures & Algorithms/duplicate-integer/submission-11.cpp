class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        unordered_set<int> hashset;

        for (int n : nums) {
            if (hashset.count(n)) {
                return true;
            }
            hashset.insert(n);
        }

        return false;
    }
};