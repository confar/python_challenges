from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i = 0
        j = 1
        while i <= len(nums) - 1:
            while j <= len(nums) - 1:
                if nums[i] + nums[j] == target:
                    return [i, j]
                else:
                    j += 1
            i += 1
            j = i + 1


assert Solution().twoSum([3, 2, 4], 6) == [1, 2]
