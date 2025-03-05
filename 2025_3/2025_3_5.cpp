class Solution {
public:
    long long coloredCells(int n) {
        long long longn = n;
        long long result = 1 + 2 * longn * (longn - 1);
        return result;
    }
};