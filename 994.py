import collections


class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        index_0 = len(grid)
        index_1 = len(grid[0])
        dest = [[0] * index_1 for _ in range(index_0)]

        bads = []
        news = []
        res = 0


        for i in range(index_0):
            for j in range(index_1):
                if grid[i][j] == 2:
                    bads.append((i,j))
                elif grid[i][j] ==1:
                    news.append((i,j))


        visit = collections.deque(bads)
        while visit:
            m,n = visit.popleft()
            for row,index in [(m-1,n),(m,n-1),(m+1,n),(m,n+1)]:
                if 0<=row<index_0 and 0<=index<index_1 and (row,index) in news:
                    news.remove((row,index))
                    visit.append((row,index))
                    dest[row][index] += dest[m][n]+1
                    res = max(res,dest[row][index])
        if len(news) >0:
            return  -1
        else:
            return res


class Solution2:
    def orangesRotting(self, grid: List[List[int]]):
        R, C = len(grid), len(grid[0])

        # queue - all starting cells with rotting oranges
        queue = collections.deque()
        for r, row in enumerate(grid):
            for c, val in enumerate(row):
                if val == 2:
                    queue.append((r, c, 0))

        def neighbors(r, c):
            for nr, nc in ((r - 1, c), (r, c - 1), (r + 1, c), (r, c + 1)):
                if 0 <= nr < R and 0 <= nc < C:
                    yield nr, nc

        d = 0
        while queue:
            r, c, d = queue.popleft()
            for nr, nc in neighbors(r, c):
                if grid[nr][nc] == 1:
                    grid[nr][nc] = 2
                    queue.append((nr, nc, d + 1))

        if any(1 in row for row in grid):
            return -1
        return d


if __name__ == '__main__':
    soul = Solution()
    mat = [[2,1,1],[1,1,0],[0,1,1]]
    print(soul.orangesRotting(mat))