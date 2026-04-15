class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        median = []
        for i in nums1:
            median.append(i)
        for j in nums2:
            median.append(j)
        
        sorted_median = sorted(median)
        l = 0
        r = len(sorted_median) - 1
        m = (l+r) // 2
        if len(sorted_median) % 2 != 0:
            return float(sorted_median[m])
        else:
            return (sorted_median[m] + sorted_median[m+1]) / 2
