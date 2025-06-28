def bfs(nodes, adj, vis, ans):
    q=[]
    q.append(nodes)
    vis[nodes]=1
    while(q):
        node=q.pop(0)
        ans.append(node)
        
        for i in adj[node]:
            if(vis[i]==0):
                q.append(i)
                vis[i]=1
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


for i in range(nodes):
    if not vis[i]:
        bfs(i, adj, vis, ans)

print(ans)
