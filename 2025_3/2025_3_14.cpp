// 我发现在做不出题的时候, 把它变成数学题会更清晰
// 比如这题就是一个优化问题
class Solution {
    public:
        int maximumCandies(vector<int>& candies, long long k) {
            // maximize m
            // s.t. sum(floor(a_i / m) for a_i in candies) >= k
            // 二分?
            // 0 <= m <= sum / k
            // 当 m = 0, 令 lhs = k + 1 即可
            long long  l = 0;
            long long sum = 0;
            for (int candy : candies) {
                sum += candy;
            }
            long long r = sum / k;
    
            while (l <= r) {
                long long mid = (l + r) / 2;
                if (maxPeople(candies, mid) < k) {
                    r = mid - 1;
                }
                else {
                    l = mid + 1;
                }
            }
            return r;
        }
    
        long long maxPeople(vector<int>& candies, long long m) {
            // 该函数返回 sum(floor(a_i / m) for a_i in candies)
            // 即每个人分 m 个糖时最多能分给几个人
            if (m == 0) {
                return LLONG_MAX;
            }
            long long people = 0;
            for (int candy : candies) {
                people += candy / m;
            }
            return people;
        }
    };