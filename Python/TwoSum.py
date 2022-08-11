# AUTHOR: LOGAN FLORY
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:       
        
        # Two Pointers
        left, right = 0, len(numbers) - 1
        
        # Start at both ends, and work until we get a solution
        # We are guaranteed a solution in our constraints
        while left < right:
            
            # First case: Under target
            if numbers[left] + numbers[right] < target:
                left += 1
            
            # Second case: Over target
            elif numbers[left] + numbers[right] > target:
                right -= 1
            
            # Third case: we have target
            else:
                return [left + 1, right + 1]
