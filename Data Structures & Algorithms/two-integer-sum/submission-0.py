class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #Use complements 
        #use hashmap
        #Store complments in hashmap so when checking if complement exists search is faster

        complements = {} #Creates hashmap
        for i, n in enumerate(nums): #enumerta
            diff = target - n
            if diff in complements:
                return [complements[diff], i]
            complements[n] = i