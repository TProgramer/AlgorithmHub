class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        # index to track new array
        idx = 1
        for i in range(1, len(nums)):
            if nums[i - 1] != nums[i]:
                nums[idx] = nums[i]
                idx += 1

        return idx