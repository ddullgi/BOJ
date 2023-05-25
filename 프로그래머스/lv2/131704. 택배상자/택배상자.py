def solution(order):
    container = []
    idx = 1
    cnt = 0
    while idx <= len(order):
        container.append(idx)
        while container and container[-1] == order[cnt]:
            cnt += 1
            container.pop()
        idx += 1
    return cnt