from heapq import heappop, heappush

def solution(book_time):
    book_time_int=[]

    for start,end in book_time:
        book_time_int.append((int(start[:2])*60+int(start[3:]),int(end[:2])*60+int(end[3:])+10))
    book_time_int.sort(key=lambda x: (x[0], x[1]))
    lasts = []
    heappush(lasts, 0)

    for i, j in book_time_int:
        last = heappop(lasts)
        if i < last : 
            heappush(lasts, last)
            heappush(lasts, j)
        else:
            heappush(lasts, j)
    
    return len(lasts)