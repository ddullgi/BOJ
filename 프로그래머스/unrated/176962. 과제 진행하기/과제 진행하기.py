from heapq import heappush, heappop

def solution(plans):
    answer = []
    Q = []
    for name, start, playtime in plans:
        heappush(Q, (int(start[:2]) * 60 + int(start[3:]), int(playtime), name))
    heappush(Q, (99999, 99999, "last"))
    keep = []
    while len(Q) >= 2:
        start, playtime, name = heappop(Q)
        if Q[0][0] == 99999 or start + playtime <= Q[0][0]:
            left_time = Q[0][0] - (start + playtime)
            answer.append(name)
            while keep and left_time > 0:
                keep_start, keep_playtime, keep_name = keep.pop()
                if left_time >= keep_playtime:
                    answer.append(keep_name)
                    left_time -= keep_playtime
                else:
                    keep.append((keep_start, keep_playtime - left_time, keep_name))
                    left_time = 0
        else:
            keep.append((start, playtime - (Q[0][0] - start), name))
            
    return answer