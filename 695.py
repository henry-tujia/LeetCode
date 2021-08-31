import collections

"""
使用visited数组减少循环次数
"""


def search(grid, i, j, visited):
    square = 1
    index_0 = len(grid)
    index_1 = len(grid[0])
    visted_wait = collections.deque()
    visted_wait.append([i, j])
    visited.append([i, j])
    while len(visted_wait) != 0:
        target = visted_wait.popleft()
        for spot in [[target[0] + 1, target[1]], [target[0], target[1] + 1], [target[0] - 1, target[1]],
                     [target[0], target[1] - 1]]:
            if not (0 <= spot[0] < index_0 and 0 <= spot[1] < index_1):
                continue
            if spot in visited: continue
            if grid[spot[0]][spot[1]] == 1:
                visted_wait.append(spot)
                visited.append(spot)
                square += 1
    return square


class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        max_square = 0
        visited = []
        index_0 = len(grid)
        index_1 = len(grid[0])

        for i in range(index_0):
            for j in range(index_1):

                if [i, j] in visited:
                    continue
                if grid[i][j] == 1:
                    max_square = max(search(grid, i, j, visited), max_square)

        return max_square


"""
置零法
"""


def search2(grid, i, j):
    square = 1
    index_0 = len(grid)
    index_1 = len(grid[0])
    visted_wait = collections.deque()
    visted_wait.append([i, j])
    while len(visted_wait) != 0:
        target = visted_wait.popleft()

        grid[target[0]][target[1]] = 0
        for spot in [[target[0] + 1, target[1]], [target[0], target[1] + 1], [target[0] - 1, target[1]],
                     [target[0], target[1] - 1]]:
            if not (0 <= spot[0] < index_0 and 0 <= spot[1] < index_1):
                continue
            if spot in visted_wait:
                continue
            if grid[spot[0]][spot[1]] == 1:
                visted_wait.append(spot)
                square += 1
    return square


class Solution2(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        max_square = 0
        index_0 = len(grid)
        index_1 = len(grid[0])

        for i in range(index_0):
            for j in range(index_1):
                if grid[i][j] == 1:
                    max_square = max(search2(grid, i, j), max_square)
        return max_square


if __name__ == '__main__':
    soul = Solution2()
    grid = [[1, 1, 0, 0, 0], [1, 1, 0, 0, 0], [0, 0, 0, 1, 1], [0, 0, 0, 1, 1]]

    print(soul.maxAreaOfIsland(grid))
