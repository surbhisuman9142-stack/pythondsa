def build_graphs(edges):
    graph = {}
    for u,v in edges:
        if u not in graph:
            graph[u] = []
        if v not in graph:
            graph[v]  = []
        graph[u].append(v)
        graph[v].append(u)
    return graph
edges = [[1,2],[1,3],[2,4]]
print(build_graphs(edges))