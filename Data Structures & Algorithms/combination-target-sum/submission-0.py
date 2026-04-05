class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        results = []
        def backtrack(index, path):
            if sum(path) == target:
                results.append(path[:]) 
                
            for i in range(index, len(nums)):
                if nums[i] > target - sum(path):
                    continue
                path.append(nums[i])
                backtrack(i, path)
                path.pop()
        backtrack(0, [])

        return results