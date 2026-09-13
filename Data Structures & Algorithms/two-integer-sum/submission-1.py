class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #Use hashmap for quick complement lookup and to track index
        complement_list = {} #hashmap
        for i, num in enumerate(nums): #enumerates with index and number in nums
            complement = target - num #difference between target and num
            if complement in complement_list: #If difference in list then return index of complement and current index
                return [complement_list[complement], i]
            complement_list[num] = i # add complement to list