class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range (len(nums)):
            t=target-nums[i]
            if t in nums:
                j = nums.index(t)
                if i != j:
                    return sorted([i, j])