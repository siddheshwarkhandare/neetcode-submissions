class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        odd=[]
        evan=[]

        for i in range(len(nums)):
            if nums[i] % 2== 0:
                evan.append(nums[i])
            else:
                odd.append(nums[i])
        return evan + odd
