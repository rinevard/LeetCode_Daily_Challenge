# 2023/11/5 Daily challenge
# https://leetcode.com/problems/find-the-winner-of-an-array-game/

class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        maxnum = max(arr)
        if len(arr) <= k:
            return maxnum

        winner = 0
        cnt = 0
        # 如果遍历完了一次数组，那么winner一定是maxnum
        for i in range(1, len(arr)):
            if arr[i] > arr[winner]:
                winner = i
                cnt = 1
            else:
                cnt += 1

            if cnt == k:
                return arr[winner]

        return maxnum