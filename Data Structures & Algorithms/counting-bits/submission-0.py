class Solution:
    def countBits(self, n: int) -> List[int]:
        output= []
        for i in range(0, n+1):
            binary = bin(i)[2:]
            output.append(binary.count("1"))
        return output
