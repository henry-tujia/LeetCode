import itertools
import copy
from typing import List

class Solution:
    def solveNQueens(self, n: int):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        if n == 0:
            return []
        # if n == 1:
        #     return [["Q"]]
        res = []
        boards = [[","]*n for _ in range(n)]


        def isInBoard(i,j) -> bool:
            return False if i<0 or i >=n else j >= 0 and j < n

        def isValidBoard(i,j):
            unchecked = set()
            for m in range(n):
                unchecked.add((i,m))
                unchecked.add((m,j))
                unchecked.add((m,-i+j+m))
                unchecked.add((m,i+j-m))
            unchecked = [x for x in unchecked if isInBoard(*x)]
            for pos in unchecked:
                m,f = pos
                if boards[m][f] == "Q":
                    return False
            return True

        def solveNQueens_inner(start):
            if start == n:
                res.append(copy.deepcopy(boards))
                # boards = [[","]*n for _ in range(n)]
                return
            for i, j in itertools.product(range(n), range(start,n)):
                if isValidBoard(i,j):
                    boards[i][j] = "Q"
                    solveNQueens_inner(start+1)
                    boards[i][j] = ","
            return

        solveNQueens_inner(0)
        return res

if __name__ == "__main__":
    solu = Solution()
    print(solu.solveNQueens(4))