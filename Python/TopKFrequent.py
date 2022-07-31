# AUTHOR: LOGAN FLORY
# METRICS:
# Runtime: 111ms, faster than 96.46% online submissions
# Memory Usage: 18.7MB, smaller than 47.47% online submissions
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        # Get a dictionary to store key value pairs
        hashmap = {}
        
        # Iterate through each number once to count all instances
        for num in nums:
            hashmap[num] = 1 + hashmap.get(num, 0)
        
        # Reverse sort our hashmap items based on the frequency (dictionary value) instead of
        # the number that occured (dictionary key)
        hashlist = sorted(list(hashmap.items()), key = lambda x: x[1], reverse=True)
        
        # Now we have to get the k tuples we want
        temp = hashlist[0:k]
        
        # And then the first element of each of those tuples
        # Definitely a better way to do this
        topK = []
        for data in temp:
            topK.append(data[0])
        return topK
            
