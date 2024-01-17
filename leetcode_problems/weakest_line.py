""" 
Source : LeetCode
Url : https://leetcode.com/problems/the-k-weakest-rows-in-a-matrix/
Algorithm : Heaps 
Author : Dhruv Shah
"""
import logging

from binary_search import binary_search

logging.basicConfig(format="%(name)s:%(levelname)s :: %(message)s", level=logging.INFO)
logger = logging.getLogger(__name__)


class K:
    def __init__(self, val, idx):
        self.val = val
        self.idx = idx

    def __gt__(self, other):
        logger.debug("Compare %s, %s", self, other)
        if self.val > other.val:
            return True
        if self.val == other.val and self.idx > other.idx:
            return True
        return False

    def __eq__(self, other):
        return self.val == other.val and self.idx == other.idx

    def __repr__(self):
        return f"{self.idx}: {self.val}"


class Solution:
    def kWeakestRows(self, mat: list[list[int]], k: int) -> list[int]:
        weakHeap = []
        for idx, row in enumerate(mat):
            logger.debug("=========== %s ===========", idx)
            temp = K(sum(row), idx)
            logger.debug("row -> %s", temp)
            location, _ = binary_search(weakHeap, temp)
            logger.debug("location [%s]", location)
            weakHeap.insert(location, temp)
            logger.debug("==> %s", weakHeap)

        return [weakHeap[i].idx for i in range(k)]


if __name__ == "__main__":
    mat = [
        [1, 1, 0, 0, 0],
        [1, 1, 1, 1, 0],
        [1, 0, 0, 0, 0],
        [1, 1, 0, 0, 0],
        [1, 1, 1, 1, 1],
    ]
    mat = [[1, 0, 0, 0], [1, 1, 1, 1], [1, 0, 0, 0], [1, 0, 0, 0]]
    k = 2
    sol = Solution()
    result = sol.kWeakestRows(mat, k)
    print(result)
