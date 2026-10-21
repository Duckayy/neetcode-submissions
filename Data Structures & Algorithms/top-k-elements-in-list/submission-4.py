class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numCount = Counter(nums)
        mostCommon = [key for key, value in numCount.most_common(k)]
        return mostCommon