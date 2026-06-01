class Solution(object):
    def minimumRecolors(self, blocks, k):
        ans = blocks[:k].count('W')

        for left in range(len(blocks) - k + 1):
            ans = min(ans, blocks[left:left+k].count('W'))

        return ans