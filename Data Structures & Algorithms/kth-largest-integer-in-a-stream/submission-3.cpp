#include <vector>
#include <queue>

class KthLargest {
private:
    // Min-heap to store the k largest elements
    std::priority_queue<int, std::vector<int>, std::greater<int>> minHeap;
    int kSize;

public:
    KthLargest(int k, std::vector<int>& nums) {
        kSize = k;
        // Add all initial numbers to the stream
        for (int num : nums) {
            add(num);
        }
    }
    
    int add(int val) {
        // Push the new value into the min-heap
        minHeap.push(val);
        
        // If the heap exceeds size k, pop the smallest element
        if (minHeap.size() > kSize) {
            minHeap.pop();
        }
        
        // The top of the min-heap is now the k-th largest element
        return minHeap.top();
    }
};
