from collections import deque

def make_graph(n, wires):
    cnt = 0
    graph = [[] for _ in range(n + 1)]
    
    for s, e in wires:
        graph[s].append(e)
        graph[e].append(s)
        
    return graph

def bfs(graph, s, visited):
    Q = deque([s])
    visited[s] = True
    
    arr = []
    
    while Q:
        v = Q.popleft()
        for i in graph[v]:
            if visited[i] != True:
                Q.append(i)
                visited[i] = True
    
    
    return arr

def solution(n, wires):
    answer = 101
    l = len(wires)
    
    
    for i in range(l):
        wire = wires[:i] + wires[i + 1:]
        
        graph = make_graph(n, wire)
        
        
        visited = [False] * (n + 1)
        bfs(graph, wire[0][0], visited)
        a = sum(visited)
        if abs(a * 2 - n) < answer:
            answer = abs(a * 2 - n)
    
    return answer