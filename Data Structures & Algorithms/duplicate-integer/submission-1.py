from collections import Counter
class Solution:    
    def hasDuplicate(self, nums: List[int]) -> bool:
        s=Counter(nums)
        for i in s.values():
            if i>=2:
                return True
        return False        