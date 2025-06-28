matrix = [[2, 3, 1, 2], [3, 4, 2, 2], [5, 6, 3, 5]]
n = len(matrix)
m = len(matrix[0])
front = [[0] * m for _ in range(m)]
cur = [[0] * m for _ in range(m)]
for j1 in range(m):
    for j2 in range(m):
        if(j1==j2):

          front[j1][j2]=matrix[n-1][j1]
        else:
           front[j1][j2]=matrix[n-1][j1]+matrix[n-1][j2]

for i in range(n-2,-1,-1):
   for j1 in range(m):
      for j2 in range(m):
         maxi=float("-inf")
         for dj1 in range(-1,2):
            for dj2 in range(-1,2):
               ans=0
               if(j1==j2):
                  ans+=matrix[i][j1]
               else:
                  ans+=matrix[i][j1]+matrix[i][j2]
               if(j1+dj1<0 or j1+dj1>=m or j2+dj2<0 or j2+dj2>=m):
                  ans+=-int(1e9)
               else:
                  ans+=front[j1+dj1][j2+dj2]
               maxi=max(maxi,ans)
         cur[j1][j2]=maxi
   front=[m[:]for m in cur]


print(front[0][m-1])

               
      