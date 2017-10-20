def DFS(matrix,m,n):
      
      if (matrix[m][n] == 0 or (m > len(matrix) - 1) or (n > len(matrix[0]) - 1)):
            return
      if ((m == len(matrix) - 1) and (n == len(matrix[0]) - 1)):
            count += 1
            return
      DFS(matrix, m, n+1)
      DFS(matrix, m+1, n)
      
if __name__ == '__main__':

      matrix = [[1,1,1,1],
                [0,0,0,0],
                [1,0,0,1],
                [1,1,1,1]]

      print(DFS(matrix,0,0))
