# AUTHOR: LOGAN FLORY
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:       
        
        # Return list to update
        ret = [0, 0]
        
        # For every number
        for i in range(len(numbers)):
          
          # Find the number that we would need to add to reach our target
          seek = target - numbers[i]
          
          # If it exists, then our problem is solved and we update accordingly
          # Being sure to account for duplicates
          if seek in numbers and seek in numbers[:i:]:
            ret[0] = i + 1
            ret[1] = numbers.index(seek) + 1
            return ret
         
        # If it doesn't exist, just return [0,0]
