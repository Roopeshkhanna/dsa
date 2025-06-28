def dfs(node,adj,ans,vis):
    vis[node]=1
    ans.append(node)
    for i in adj[node]:
        if(not vis[i]):
            dfs(i,adj,ans,vis)
    return(ans)

    







nodes = 5
adj = [[] for _ in range(nodes)]


adj[0].append(1)
adj[0].append(4)
adj[1].append(0)
adj[1].append(2)
adj[1].append(3)
adj[2].append(1)
adj[3].append(1)
adj[4].append(0)

vis = [0] * nodes  
ans = []
print(dfs(0,adj,ans,vis))