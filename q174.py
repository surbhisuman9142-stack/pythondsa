def degree(graph, node):
    if node not in graph:
        return 0
    return len(graph[node])
graph = {
    1: [2,3],
    2: [1,4],
    3: [1],
    4: [2]
}
print(degree(graph,1))
print(degree(graph,3))
print(degree(graph,5))