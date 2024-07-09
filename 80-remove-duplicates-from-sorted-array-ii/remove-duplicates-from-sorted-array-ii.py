class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        # index to track new array
        idx = 1

        # value to track num of duplicated elements
        counter = 1

        for i in range(1, len(nums)):

            # update new array when sequentially same at most twice
            if nums[i] == nums[i - 1]:
                counter += 1
            else:
                counter = 1
            
            if counter <= 2:
                nums[idx] = nums[i]
                idx += 1

        return idx