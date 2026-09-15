class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #DO a counter for each element and return k elements with the most frequency
        count = Counter(nums)
        ans = [key for key, freq in count.most_common(k)]
        return ans