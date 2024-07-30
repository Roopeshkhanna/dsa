def solve(i,j,mapp,vis,n,ans,string,mi,mj):
    if(i==n-1 and j==n-1):
        ans.append(string)

        return
    strs="DLRU"
    for k in range(4):
        ni=i+mi[k]
        nj=j+mj[k]
        if(0<=ni<n and 0<=nj<n and vis[ni][nj]!=1 and mapp[ni][nj]==1):
            vis[ni][nj]=1
            solve(ni,nj,mapp,vis,n,ans,string+strs[k],mi,mj) 
            vis[ni][nj]=0

mapp=[[1, 0, 0, 0],
                [1, 1, 0, 1], 
                [1, 1, 0, 0],
                [0, 1, 1, 1]]
vis = [[0] * 4 for _ in range(4)]
ans=[]
n=4
mi=[1,0,0,-1]
mj=[0,-1,1,0]
vis[0][0]=1
solve(0,0,mapp,vis,n,ans,'',mi,mj)
print(ans)