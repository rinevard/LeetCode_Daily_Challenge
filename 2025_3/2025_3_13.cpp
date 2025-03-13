// 我们用类似扫描线算法的思路, 将所有区间的起点和终点标记为事件
// O(nlogn)
/*
趣事一则:
在 iskZeroArray 的第一个 for 循环中, 我写的原本是
vector<int> query = queries[i];
int l = query[0];
int r = query[1];
int val = query[2];
过了, 但是 1000 ms.

换成
int l = queries[i][0];
int r = queries[i][1];
int val = queries[i][2];
以后, 50ms

编译器明显是能优化后者的, 而前者之所以如此慢应该是因为不断分配内存给 query 吧.
*/
class Solution {
    public:
        int minZeroArray(vector<int> &nums, vector<vector<int>> &queries) {
            if (!iskZeroArray(nums, queries, queries.size())) {
                return -1;
            }
            int l = 0;
            int r = queries.size();
            while (l <= r) {
                int mid = (l + r) / 2;
                if (iskZeroArray(nums, queries, mid)) {
                    r = mid - 1;
                }
                else {
                    l = mid + 1;
                }
            }
            return l;
        }
        bool iskZeroArray(vector<int> &nums, vector<vector<int>> &queries, int k) {
            // ops 是操作列表
            // 如果我们想在区间[l,r]上统一执行某个操作, 可以在l位置和r+1位置标记, 然后通过前缀和得到每个位置的实际变化值。
            vector<int> ops(nums.size() + 1, 0);
            for (int i = 0; i < k; i++) {
                int l = queries[i][0];
                int r = queries[i][1];
                int val = queries[i][2];
                ops[l] += val;
                ops[r + 1] -= val;
            }

            int n = nums.size();
            int op = 0;
            for (int i = 0; i < n; i++) {
                op += ops[i];
                if (op < nums[i]) {
                    return false;
                }
            }
            return true;
        }
    };
