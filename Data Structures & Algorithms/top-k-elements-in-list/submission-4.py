class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = {}
        for num in nums:
            frequency[num] = frequency.get(num, 0) + 1
        heap = [(v, k) for k, v in frequency.items()]
        heapq.heapify(heap)


        return [v for k, v in heapq.nlargest(k, heap)]