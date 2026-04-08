class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def neighbors(row, col):
            ret = []

            if row + 1 < len(grid):
                ret.append((row + 1, col))
            if col + 1 < len(grid[0]):
                ret.append((row, col + 1))
            if row - 1 >= 0:
                ret.append((row - 1, col))
            if col - 1 >= 0:
                ret.append((row, col - 1))

            return ret

        def bfs(row, col):
            queue = deque()
            queue.append((row, col))
            while len(queue) > 0:
                v = queue.pop()
                if not grid[v[0]][v[1]] == "0":
                    # seen.add(v)
                    grid[v[0]][v[1]] = "0"
                    for w in neighbors(*v):
                        queue.append(w)

        count = 0

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == "0":
                    continue
                count += 1
                bfs(row, col)
                
        return count
