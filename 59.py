class Solution():
    def generate_matrix(self,n):
        matrix = [[0]*n for _ in range(n)]

        bounds = [0,n-1,0,n-1]

        number = 1
        while number < n**2:
            if bounds[0] <= bounds[1]:
                for i in range(bounds[2],bounds[3]+1):
                    matrix[bounds[0]][i] = number
                    number += 1
                bounds[0] += 1
            if bounds[2] <= bounds[3]:
                for i in range(bounds[0],bounds[1]+1):
                    matrix[i][bounds[3]] = number
                    number += 1
                bounds[3] -= 1
            if bounds[0] <= bounds[1]:
                for i in range(bounds[3],bounds[2]-1,-1):
                    matrix[bounds[1]][i] = number
                    number += 1
                bounds[2] += 1
            if bounds[2] <= bounds[3]:
                for i in range(bounds[1],bounds[0]-1,-1):
                    matrix[i][bounds[2]] = number
                    number += 1
                bounds[1] -= 1
            

        return matrix

if __name__ == '__main__':
    solu = Solution()

    print(solu.generate_matrix(3))