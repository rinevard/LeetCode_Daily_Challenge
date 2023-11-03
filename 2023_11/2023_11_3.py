# 2023/11/3 Daily challenge
# https://leetcode.com/problems/build-an-array-with-stack-operations/

class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        ans = ['Push', 'Pop'] * (target[0] - 1)
        ans.append('Push')
        for i in range(1, len(target)):
            ans.extend(['Push', 'Pop'] * (target[i] - target[i - 1] - 1))
            ans.append('Push')

        return ans