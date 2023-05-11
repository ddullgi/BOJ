def solution(elements):
    l = len(elements)
    elements = elements * 2
    arr = set()
    for i in range(l):
        for j in range(1, l):
            arr.add(sum(elements[i:i + j]))
    return len(arr) + 1