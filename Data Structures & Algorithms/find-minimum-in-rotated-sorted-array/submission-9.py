class Solution:
    def findMin(self, nums: List[int]) -> int:
        # TC: O(logn)
        # SC: O(1)
        # l = 0
        # r = len(nums) - 1
        
        # while l < r:
        #     m = (l+r)//2
        #     if nums[m] > nums[r]:
        #         l = m + 1
        #     else:
        #         r = m
        # return nums[l]

        res = nums[0]
        l = 0
        r = len(nums) - 1
        while l <= r:
            if nums[l] < nums[r]:
                res = min(res, nums[l])
                break
            
            m = (l+r)//2
            res = min(res, nums[m])
            if nums[m] > nums[r]:
                l = m+1
            else:
                r = m-1
        return res




