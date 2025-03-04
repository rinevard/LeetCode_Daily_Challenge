class Solution {
public:
    bool checkPowersOfThree(int n) {
        // 盲猜和三进制有关, 这可以理解为在问 "n的三进制表达是否有2"
        // 那么 %3 == 0: n /= 3; %3 == 1: n /= 3; %3 == 2: return false 
        while (n != 0) {
            if (n % 3 == 0 || n % 3 == 1) {
                n /= 3;
            }
            else {
                return false;
            }
        }
        return true;
    }
};