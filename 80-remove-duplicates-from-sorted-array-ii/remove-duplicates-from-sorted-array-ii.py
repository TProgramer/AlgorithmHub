class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        # index to track new array
        idx = 0

        # dict to track num of elements
        counter = {}

        for i in range(len(nums)):

            # update new array when sequentially same at most twice
            if nums[i] not in counter:
                counter[nums[i]] = 1
            elif counter[nums[i]] < 2:
                counter[nums[i]] += 1
            else:
                continue
            
            nums[idx] = nums[i]
            idx += 1

        return idx