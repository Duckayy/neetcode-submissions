class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        complement_list = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in complement_list:
                return [complement_list[complement],i]
            complement_list[num] = i
        