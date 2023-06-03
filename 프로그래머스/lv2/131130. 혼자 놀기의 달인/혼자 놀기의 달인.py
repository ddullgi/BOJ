# def union(parent, a, b):
#     a = find(parent, a)
#     b = find(parent, b)
#     if a < b:
#         parent[a] = b
#     else:
#         parent[b] = a
        


def solution(cards):
    answer = 0
    parent = [i for i in range(len(cards) + 1)]
    def union(a, b):
        a = find(a)
        b = find(b)
        if a != b:
            parent[a] = b
    
    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]
    
    for i in range(len(cards)):
        boxA = i + 1
        boxB = cards[i]
        union(boxA, boxB)
    
    roots = {}
    for box in range(1, len(cards) + 1):
        root = find(box)
        roots[root] = roots.get(root, 0) + 1
    
    if len(roots) == 1:
        return 0
    
    lis = sorted(list(roots.values()), reverse=True)
    
    return lis[0] * lis[1]