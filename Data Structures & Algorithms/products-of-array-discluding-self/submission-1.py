class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod = nums[0]
        zeroes = 0
        result = [0] * len(nums)
        for num in nums: #tracks how many zeroes
            if num == 0:
                zeroes += 1
        if zeroes > 1: #solves more than 2 zeroes edge case
            return result
        for i in range(1,len(nums)):
            if prod == 0:
                prod = nums[i]
                continue
            if nums[i] == 0:
                continue
            prod *= nums[i]
            
        for j in range(len(nums)):
            if nums[j] == 0:
                result[j] = prod
                break
            if zeroes < 1:
                result[j] = prod // nums[j]
        return result
