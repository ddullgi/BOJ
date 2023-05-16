def solution(n, costs):
    
    costs.sort(key = lambda x: x[2]) # 간선 가중치 순으로 정렬
    
    p = [i for i in range(n)]
    def find(x):
        if x != p[x]:
            p[x] = find(p[x])
        return p[x]
    
    def union(x,y):
        a = find(x)
        b = find(y)
        if a != b:
            p[a] = b
    
    ans = 0
    mst = []
    for cost in costs:
        u, v, w = cost
        if find(u) != find(v):
            union(u, v)
            ans += w
    
    
    return ans