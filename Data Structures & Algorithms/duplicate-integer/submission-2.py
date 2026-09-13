class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #Create hashmap for quick lookup 
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False