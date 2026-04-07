class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = {}
        for num in nums:
            if not num in frequency:
                frequency[num] = 1
            else:
                frequency[num] += 1
        heap = [(v, k) for k, v in frequency.items()]
        print(heap)
        heapq.heapify(heap)
        print(heap)
        print(frequency)


        return [v for k, v in heapq.nlargest(k, heap)]