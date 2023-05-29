import itertools
class Solution():
    def rotation_matrix(self, matrix):
        col= row = len(matrix)
        for i in range(col):
            for j in range(i+1,row):
                matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]

        for i, j in itertools.product(range(col), range(col//2)):
            matrix[i][j],matrix[i][col-1-j] = matrix[i][col-1-j],matrix[i][j]


if __name__ == '__main__':
    solu = Solution()
    matrix = [[1,2,3],[5,6,7],[9,10,11]]

    solu.rotation_matrix(matrix)

    print( matrix)