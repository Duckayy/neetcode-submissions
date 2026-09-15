class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #We need to track the complements and the index of their location then check if the current complement has already been found
        complement_list = {}
        for i, n in enumerate(nums):
            complement = target - n
            if complement in complement_list:
                return [complement_list[complement], i]
            complement_list[n] = i