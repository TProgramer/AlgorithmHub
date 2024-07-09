class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:

        k = 0
        for i in range(len(nums)):
            if nums[i] == val:
                nums[i] = -1
                k += 1
        
        nums.sort(reverse = True)

        return len(nums) - k