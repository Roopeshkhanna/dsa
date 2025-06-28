def dfs(node, adj, vis):
    vis[node] = 1
    for i in adj[node]:
        if not vis[i]:
            dfs(i, adj, vis)

nodes = 8
adj = [
    [1, 2],
    [0],
    [0],
    [4],
    [3],
    [],
    [7],
    [6]
]

vis = [0] * nodes
cnt = 0

for i in range(nodes):
    if not vis[i]: 
        cnt += 1
        dfs(i, adj, vis)

print(cnt)
