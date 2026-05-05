class Solution:
    def countSeniors(self, details: List[str]) -> int:
        count=0
        for s in details:
            age = int(s[11:13])
            if age > 60:
                count+=1
        return count