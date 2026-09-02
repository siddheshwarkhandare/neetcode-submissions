from collections import Counter
import heapq

class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        # Count frequencies of each number
        count = Counter(nums)
        
        # Return the k most frequent elements
        return heapq.nlargest(k, count.keys(), key=count.get)