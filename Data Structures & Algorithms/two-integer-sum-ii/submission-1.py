class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l,r=0,len(numbers)-1 # for travling the arry revers

        while numbers[l] + numbers[r] != target:
            #s=numbers[l] + numbers[r]  # to compair the total sum to target
            if numbers[l] + numbers[r] > target: # is sum is bigger than the target than decreas the right pointer
                r-=1
            elif numbers[l] + numbers[r]< target: #if sum is less than than the target then increas the left pointer
                l+=1
            
        return[l+1,r+1] # it will return index of element
    

#if array is sorted then we can remove element that are biger than the target 
        