def isok(graph, node, color, val, n):
    for i in range(n):
        if node != i and graph[i][node] == 1 and color[i] == val:
            return False
    return True

def solve(node, graph, color, m, n):
    if node == n:
        return True
    for i in range(1, m + 1):
        if isok(graph, node, color, i, n):
            color[node] = i
            if solve(node + 1, graph, color, m, n):
                return True
            color[node] = 0
    return False

n = 4
color = [0] * n
m = 3
graph = [
    [0, 1, 1, 1],  
    [1, 0, 1, 0],  
    [1, 1, 0, 1],  
    [1, 0, 1, 0]
]

if solve(0, graph, color, m, n):
    print("Solution exists:", color)
else:
    print("No solution exists")
#T.C O(n^m)