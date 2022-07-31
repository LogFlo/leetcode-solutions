# AUTHOR: LOGAN FLORY
# METRICS:
# Runtime: 638 ms, faster than 59.06% online submissions
# Memory Usage: 25.9 MB, less than 72.78% online submissions
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for n in nums:
            if n in seen:
                return True
            seen.add(n)
        return False
