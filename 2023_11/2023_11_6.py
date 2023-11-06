# 2023/11/6 Daily challenge
# https://leetcode.com/problems/seat-reservation-manager/description/

import heapq
class SeatManager:
    # 用最小堆
    def __init__(self, n: int):
        self.available_seats = []
        for i in range(n):
            heapq.heappush(self.available_seats, (i + 1, None))

    def reserve(self) -> int:
        seat_num, _ = heapq.heappop(self.available_seats)
        return seat_num

    def unreserve(self, seatNumber: int) -> None:
        heapq.heappush(self.available_seats, (seatNumber, None))


# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)