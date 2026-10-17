class Solution {
public:
    vector<vector<int>> merge(vector<vector<int>>& intervals) {
        sort(intervals.begin(), intervals.end());
        vector<vector<int>> result;

        for (auto& interval: intervals){
            int start = interval[0];
            int end = interval[1];

            if (result.empty() || start > result.back()[1]){
                result.push_back({start, end});
            }else{
                result.back()[1] = max(result.back()[1], end);
            }
        }

        return result;
    }
};
