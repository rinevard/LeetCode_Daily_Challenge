class Solution {
    public:
        int numberOfSubstrings(string s) {
            int len = s.size();

            // 初始化 the first occurrence of a/b/c on or after idx
            vector<int> nextA(len, -1);
            vector<int> nextB(len, -1);
            vector<int> nextC(len, -1);
            int nextAidx = -1;
            int nextBidx = -1;
            int nextCidx = -1;
            for (int i = len - 1; i >= 0; i--) {
                switch (s[i]) {
                    case 'a':
                        nextAidx = i;
                        break;
                    case 'b':
                        nextBidx = i;
                        break;
                    case 'c':
                        nextCidx = i;
                        break;
                }
                nextA[i] = nextAidx;
                nextB[i] = nextBidx;
                nextC[i] = nextCidx;
            }

            int cnt = 0;
            // 对每个 i, cnt += (以 i 开头的所有包含 abc 的字串的数量)
            for (int i = 0; i < len; i++) {
                // 如果索引 i 之后不再可能构成 abc, break即可
                if (nextA[i] == -1 || nextB[i] == -1 || nextC[i] == -1) {
                    break;
                }
                cnt += (len - max({nextA[i], nextB[i], nextC[i]}));
            }
            return cnt;
        }
    };