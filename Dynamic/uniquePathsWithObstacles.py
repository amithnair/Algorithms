class uniquePathsWithObstacles:
    # @param A : list of list of integers
    # @return an integer
    def uniquePathsWithObstacles(self, A):
        m, n = len(A), len(A[0])
        #print m
        #print n
        cut  = False
        path = []
        for i in range(m):
            path.append([])
            for j in range(n):
                path[i].insert(j, 0)
                
        
        #print path
        for j in range(n):
            if(A[0][j] == 1 or cut):
                path[0][j] =  0
                cut = True
            else:
                path[0][j] = 1
            #print path
        #print '*******'    
        #print path
        cut = False
        for i in range(m):
            if(A[i][0] == 1 or cut):
                path[i][0] =  0
                cut = True
            else:
                path[i][0] =  1
            #print path
        #print '*******'
        #print path    
        #print path
        for x in range(1,m):
            for y in range(1,n):
                if(A[x][y] == 1):
                    path[x][y] = 0
                else:
                    path[x][y] = path[x-1][y] + path[x][y-1]
        
        #print path
        #print m, n
        return path[m-1][n-1]
        
    
    
    