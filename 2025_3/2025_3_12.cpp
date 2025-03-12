class Solution {
    public:
        int maximumCount(vector<int>& nums) {
            auto lower = lower_bound(nums.begin(), nums.end(), 0);
            auto upper = upper_bound(nums.begin(), nums.end(), 0);
            return max((lower - nums.begin()), nums.end() - upper);
        }
    };