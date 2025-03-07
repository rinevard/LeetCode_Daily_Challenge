// 先用筛法来求素数表再遍历会有更低的时间复杂度, 但实际上我们的方法已经 beat 100% 了.
// 主要在于if (minDiff == 2) return ans, 由于数据范围很小, 存在大量孪生素数.
// 不加这一句排名就掉到 90% 以后了.
class Solution {
public:
    vector<int> closestPrimes(int left, int right) {
        if (left <= 2 && right >= 3) {
            return {2, 3};
        }

        vector<int> ans = {-1, -1};
        int minDiff = INT_MAX;
        int latestLeftPrime = -1;
        int latestRightPrime = -1;

        left = (left % 2 == 0) ? (left + 1) : left; // 素数只可能是奇数(不考虑2)
        for (int num = left; num <= right; num += 2) { // 素数只可能是奇数(不考虑2)
            if (isPrime(num)) {
                latestLeftPrime = latestRightPrime;
                latestRightPrime = num;
            }
            if (latestLeftPrime != -1 && latestRightPrime - latestLeftPrime < minDiff) {
                ans[0] = latestLeftPrime;
                ans[1] = latestRightPrime;
                minDiff = ans[1] - ans[0];
            }
            if (minDiff == 2) {
                return ans;
            }
        }
        if (latestLeftPrime == -1) {
            return {-1, -1};
        }
        return ans;
    }

    bool isPrime(int num) {
        if (num <= 1) {
            return false;
        }
        if (num == 2) {
            return true;
        }
        int sqrtNum = sqrt(num);
        for (int i = 2; i < sqrtNum + 1; i++) {
            if (num % i == 0) {
                return false;
            }
        }
        return true;
    }
};