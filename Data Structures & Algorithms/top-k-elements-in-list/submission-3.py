class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #Use counter dictionary to track and increment frequency of elements
        #Then enumerate through dictionary pulling key (that being the unique element in dictionary). 
        #Then only return key using most_common() as a way to get keys up till value k
        count_nums = Counter(nums)
        ans = [key for key, val in count_nums.most_common(k)]
        return ans