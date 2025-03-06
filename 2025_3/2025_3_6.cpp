class Solution {
public:
    vector<int> findMissingAndRepeatedValues(vector<vector<int>>& grid) {
        int n = grid.size();
        int numValues = n * n;
        vector<int> ans = {-1, -1};
        vector<int> mat(numValues, 0);

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (mat[grid[i][j] - 1] == 1) {
                    ans[0] = grid[i][j];
                }
                mat[grid[i][j] - 1] = 1;
            }
        }

        for (int i = 0; i < numValues; i++) {
            if (mat[i] == 0) {
                ans[1] = i + 1;
                return ans;
            }
        }
        return ans;
    }
};