class Solution {
public:
    bool isHappy(int n) {
        unordered_set<int> visit;
        while (visit.find(n) == visit.end()){
            visit.insert(n);
            n = sumOfSquares(n);
            if(n==1){
                return true;
            }
        }
        return false;
        
    }

private:
    int sumOfSquares(int n){
        int output = 0;

        while(n>0){
            int digit = n%10;
            digit = digit*digit;
            output+= digit;
            n/=10;
        }
        return output;
    }

};
