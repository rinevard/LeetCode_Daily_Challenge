# 2023/10/29 Daily challenge
# https://leetcode.com/problems/poor-pigs/

# 一只猪可能在第i次实验中死掉，也可能一次都不死，因此我们一共能用n只猪和k次实验创造出(k + 1)^n种结果。
# 使(k + 1)^n > buckets即可。（因为只有一个有毒，共有buckets种可能情况）
from math import log
from math import ceil
class Solution:
    def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        tests = minutesToTest // minutesToDie
        base = tests + 1
        
        # 精度误差要做一点点小处理
        return ceil(log(buckets)/log(base + 0.00001))