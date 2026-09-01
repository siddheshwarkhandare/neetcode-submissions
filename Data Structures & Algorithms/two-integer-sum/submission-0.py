class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prvemap={}

        for i,n in enumerate(nums):
            diff=target - n
            if diff in prvemap:
                return [prvemap[diff],i]
            prvemap[n]=i
        return[]