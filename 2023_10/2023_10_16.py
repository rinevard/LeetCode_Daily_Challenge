# 2023/10/16 Daily challenge
# https://leetcode.com/problems/pascals-triangle-ii/
from math import comb
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        return [comb(rowIndex, i) for i in range(rowIndex+1)]