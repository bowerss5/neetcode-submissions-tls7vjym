class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        ROWS, COLS = len(heights), len(heights[0])

        pacific = set()
        atlantic = set()


        def bfs(row, col, ocean):
            q = deque()
            ocean.add((row,col))
            q.append((row,col))

            while q:
                c = q.popleft()

                for d in DIRECTIONS:
                    n = (c[0] + d[0], c[1] + d[1])
                    if n in ocean:
                        continue
                    if n[0] >= ROWS or n[0] < 0 or n[1] >= COLS or n[1] < 0:
                        continue
                    if heights[c[0]][c[1]] > heights[n[0]][n[1]]:
                        continue
                    ocean.add(n)
                    q.append(n)



        for r in range(ROWS):
            c = COLS - 1
            if not (r,0) in pacific:
                bfs(r, 0, pacific)
            if not (r,c) in atlantic:
                bfs(r, c, atlantic)

        for c in range(COLS):
            r = ROWS - 1
            if not (0,c) in pacific:
                bfs(0, c, pacific)
            if not (r,c) in atlantic:
                bfs(r, c, atlantic)

        return [[r, c] for (r, c) in (pacific & atlantic)]