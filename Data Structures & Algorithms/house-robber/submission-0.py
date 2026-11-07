class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        rob_prev2 = 0  # Maximum profit from 2 houses ago
        rob_prev1 = 0  # Maximum profit from 1 house ago
        
        for num in nums:
            # Decide whether to rob the current house or skip it
            current_rob = max(rob_prev1, rob_prev2 + num)
            
            # Slide the window forward
            rob_prev2 = rob_prev1
            rob_prev1 = current_rob
            
        return rob_prev1
