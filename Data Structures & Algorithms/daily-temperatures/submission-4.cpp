class Solution {
public:
    std::vector<int> dailyTemperatures(std::vector<int>& temperatures) {
        std::vector<int> res(temperatures.size(), 0);
        std::stack<std::pair<int, int>> st; // (temp, i)

        for (int i = 0; i < temperatures.size(); ++i) {
            int temp = temperatures[i];
            while (!st.empty() && temp > st.top().first) {
                auto [stackT, stackIdx] = st.top();
                st.pop();
                res[stackIdx] = i - stackIdx;
            }
            st.push({temp, i});
        }

        return res;
    }
};
