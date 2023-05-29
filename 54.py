class Solution():
    def visit_matrix(self,matrix):
        bounds = [0,len(matrix)-1,0,len(matrix[0])-1]

        res = []

        while len(res) < len(matrix)*len(matrix[0]):
            self._extracted_from_visit_matrix_7(res, bounds, matrix)
            bounds[0] += 1
            bounds[1] -= 1
            bounds[2] += 1
            bounds[3] -= 1
        return res

    # TODO Rename this here and in `visit_matrix`
    def _extracted_from_visit_matrix_7(self, res, bounds, matrix):
        res.extend(matrix[bounds[0]][j] for j in range(bounds[2],bounds[3]+1))
        res.extend(matrix[i][bounds[3]] for i in range(bounds[0]+1,bounds[1]+1))
        res.extend(matrix[bounds[1]][i] for i in range(bounds[3]-1,bounds[2],-1))
        res.extend(matrix[j][bounds[2]] for j in range(bounds[1],bounds[0],-1))


if __name__ == '__main__':
    solu = Solution()
    matrix = [[1,2,3,4,5],[5,6,7,8,10],[9,10,11,12,14]]

    print(solu.visit_matrix(matrix))


