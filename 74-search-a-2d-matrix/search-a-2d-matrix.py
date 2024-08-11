from itertools import chain
from bisect import bisect_left

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # flatten 2d array into 1d array
        # and search target with binary search
        flatten_array = list(chain(*matrix))

        left = 0
        right = len(flatten_array) - 1
        while left <= right:
          mid = (left + right) // 2
          nowTarget = flatten_array[mid]
          if nowTarget == target:
            return True
          elif nowTarget > target:
            right = mid - 1
          else:
            left = mid + 1
        return False
        