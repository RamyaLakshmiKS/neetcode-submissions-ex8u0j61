class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        running_max_l = [0] * n
        running_max_r = [0] * n

        curr_l = 0
        curr_r = 0
        for i, h in enumerate(height):
            running_max_l[i] = max(curr_l, h)
            curr_l = running_max_l[i]
        
        for j in range(n-1, -1, -1):
            running_max_r[j] = max(height[j], curr_r)
            curr_r = running_max_r[j]
        
        total_water = 0
        for i in range(n):
            total_water += min(running_max_l[i], running_max_r[i]) - height[i] 
        
        return total_water