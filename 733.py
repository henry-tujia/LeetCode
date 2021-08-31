import collections
import queue

"""
广度优先
"""


class Solution(object):
    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        index_0 = len(image)
        index_1 = len(image[0])

        que = queue.Queue()
        que.put([sr, sc])
        value = image[sr][sc]

        while not que.empty():
            target = que.get()
            image[target[0]][target[1]] = newColor
            new_index_0 = target[0]
            new_index_1 = target[1]
            for spot in [[new_index_0 - 1, new_index_1], [new_index_0, new_index_1 - 1], [new_index_0 + 1, new_index_1],
                         [new_index_0, new_index_1 + 1]]:
                if spot[0] >= index_0 or spot[1] >= index_1:
                    continue
                if image[spot[0]][spot[1]] == value:
                    que.put(spot)
        return image


"""
深度优先
"""

def recsive(image, sr, sc, newColor):
    index_0 = len(image)
    index_1 = len(image[0])

    curColor = image[sr][sc]
    image[sr][sc] = newColor

    for spot in [[sr + 1, sc], [sr, sc + 1], [sr - 1, sc], [sr, sc - 1]]:
        if not (0 <= spot[0] < index_0 and 0 <= spot[1] < index_1):
            continue
        if image[spot[0]][spot[1]] != curColor:
            continue
        recsive(image, spot[0], spot[1], newColor)


class Solution2(object):
    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        if not newColor == image[sr][sc]:
            recsive(image, sr, sc, newColor)

        return image



if __name__ == '__main__':
    soul = Solution2()
    image = [[0,0,0],[0,1,1]]
    sr = 1
    sc = 1
    newColor = 1
    print(soul.floodFill(image, sr, sc, newColor))
    # print(s)
