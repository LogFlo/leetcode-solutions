# AUTHOR: LOGAN FLORY
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        # List to set because set actions are faster
        nums = set(nums)
        
        # First check for empty
        if len(nums) == 0:
            return 0
        
        # Longest sequence thus far
        max_length = 0
        
        # Look at each num
        for num in nums:
            # If it doesnt have a predecessor, it isnt already part of a sequence
            if (num - 1) not in nums:
                # So our current length is 0, we're on the first of a new sequence
                cur_length = 0
                # So increment length and add it to this num until we are no longer in our list
                while (num + cur_length) in nums:
                    cur_length += 1
                    # If that length is longer than our previously recorded max length, set our new max length
                    # We update max length in while loop so we dont have to worry about when we get kicked out
                    max_length = max(cur_length, max_length)
                    
        return max_length
                
