"""
Leetcode question : https://leetcode.com/problems/ugly-number-ii/submissions/1148179301/
Author : Dhruv Shah
"""

import heapq
import bisect

from commons.utils import timer_random
from merge import K


class Ugly:
    # Алгоритм для расчета всего диапазон чисел заранее, но мало полезен если нужно найти 1 число поскольку вычесляет весь диапазон чисел.
    """
    Solution from leetcode. NOT my code.
    """

    def __init__(self):
        self.nums = nums = []
        seen = {1}

        heap = []
        heapq.heappush(heap, 1)

        for _ in range(1690):
            current_ugly = heapq.heappop(heap)
            nums.append(current_ugly)

            for i in [2, 3, 5]:
                new_ugly = current_ugly * i
                if new_ugly not in seen:
                    seen.add(new_ugly)
                    heapq.heappush(heap, new_ugly)


class Solution:
    """
    Class to try out nthUglyNumber solution. Essentially a wrapper
    """

    def nthUglyNumber(self, n: int) -> int:  # pylint: disable=C0103,C0116
        if n == 1:
            return 1
        i = 0
        op = [1]
        while i < n:
            val = op[i]
            a, b, c = val * 2, val * 3, val * 5
            op = K.merge_without_duplicates(op, [a, b, c])
            i += 1
        return op[n - 1]

    def nthUglyNumber_1(self, n: int) -> int:  # pylint: disable=C0103,C0116
        u = Ugly()
        return u.nums[n - 1]

    def nthUglyNumber_2(self, n: int) -> int:  # pylint: disable=C0103,C0116
        if n == 1:
            return 1
        uglies = []
        op = [1]
        seen = {1}
        for _ in range(n):
            current_ugly = heapq.heappop(op)
            uglies.append(current_ugly)
            for new_ugly in [current_ugly * 2, current_ugly * 3, current_ugly * 5]:
                if new_ugly not in seen:
                    heapq.heappush(op, new_ugly)
                    seen.add(new_ugly)

        return uglies[n - 1]

    def nthUglyNumber_3(self, n: int) -> int:  # pylint: disable=C0103,C0116
        if n == 1:
            return 1
        # uglies = []
        op = [1]
        seen = {1}
        for _ in range(n):
            current_ugly = heapq.heappop(op)
            # uglies.append(current_ugly)
            for new_ugly in [current_ugly * 2, current_ugly * 3, current_ugly * 5]:
                if new_ugly not in seen:
                    heapq.heappush(op, new_ugly)
                    seen.add(new_ugly)

        return sorted(seen)[n - 1]

    def nthUglyNumber_4(self, n: int) -> int:  # pylint: disable=C0103,C0116
        if n == 1:
            return 1
        # uglies = []
        op = [1]
        seen = {1}
        for i in range(n):
            current_ugly = op[i]
            # uglies.append(current_ugly)
            for new_ugly in [current_ugly * 2, current_ugly * 3, current_ugly * 5]:
                if new_ugly not in seen:
                    bisect.insort(op, new_ugly)
                    seen.add(new_ugly)

        return op[n - 1]

    @staticmethod
    def contains(a, x):
        """returns true if sorted sequence `a` contains `x`"""
        i = bisect.bisect_left(a, x)
        return i != len(a) and a[i] == x

    def nthUglyNumber_5(self, n: int) -> int:  # pylint: disable=C0103,C0116
        if n == 1:
            return 1

        op = [1]
        for i in range(n):
            current_ugly = op[i]

            for new_ugly in [current_ugly * 2, current_ugly * 3, current_ugly * 5]:
                if not self.contains(op, new_ugly):
                    bisect.insort(op, new_ugly)

        return op[n - 1]


if __name__ == "__main__":
    sol = Solution()

    print(sol.nthUglyNumber(100))
    print(sol.nthUglyNumber_2(100))
    print(sol.nthUglyNumber_3(100))
    print(sol.nthUglyNumber_4(100))
    timer_random(sol.nthUglyNumber, (200,), times=100)
    timer_random(sol.nthUglyNumber_1, (200,), times=100)
    timer_random(sol.nthUglyNumber_2, (200,), times=100)
    timer_random(sol.nthUglyNumber_3, (200,), times=100)
    timer_random(sol.nthUglyNumber_4, (200,), times=100)
    timer_random(sol.nthUglyNumber_5, (200,), times=100)
