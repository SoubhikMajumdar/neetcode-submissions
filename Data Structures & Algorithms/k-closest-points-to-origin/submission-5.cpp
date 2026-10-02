class Solution {
public:
    vector<vector<int>> kClosest(vector<vector<int>>& points, int k) {
        // {distance, point}
        priority_queue<pair<int, vector<int>>> heap;

        for (auto& point : points) {
            int x = point[0];
            int y = point[1];

            int distance = x * x + y * y;

            heap.push({distance, point});

            if (heap.size() > k) {
                heap.pop();
            }
        }

        vector<vector<int>> result;

        while (!heap.empty()) {
            result.push_back(heap.top().second);
            heap.pop();
        }

        return result;
    }
};
