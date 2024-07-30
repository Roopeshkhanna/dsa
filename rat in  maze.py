def solve(row,col,ans,string,vis,n,mapp):
    if(row==n-1 and col==n-1):
        ans.append(string)
        return
    if(row+1<n and mapp[row+1][col]==1 and vis[row+1][col]!=1):
        vis[row][col]=1
        solve(row+1,col,ans,string+'D',vis,n,mapp)
        vis[row][col]=0
    if(col-1>=0 and mapp[row][col-1]==1 and vis[row][col-1]!=1):
        vis[row][col]=1
        solve(row,col-1,ans,string+'L',vis,n,mapp)
        vis[row][col]=0
    if(col+1<n and mapp[row][col+1]==1 and vis[row][col+1]!=1):
        vis[row][col]=1
        solve(row,col+1,ans,string+'R',vis,n,mapp)
        vis[row][col]=0
    if(row-1>=0 and mapp[row-1][col]==1 and vis[row-1][col]!=1):
        vis[row][col]=1
        solve(row-1,col,ans,string+'U',vis,n,mapp)
        vis[row][col]=0
mapp=[[1, 0, 0, 0],
                [1, 1, 0, 1], 
                [1, 1, 0, 0],
                [0, 1, 1, 1]]
vis = [[0] * 4 for _ in range(4)]
ans=[]
n=4
solve(0,0,ans,"",vis,n,mapp)
print(ans)
    


    
    
