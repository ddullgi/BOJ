def solution(m, n, startX, startY, balls):
    answer = []
    end_li = ((-startX,startY),(startX,-startY),(m*2-startX,startY),(startX,2*n-startY))

    for X,Y in balls:
        distances = []
        for endX,endY in end_li: 
            e_b_distance = (X-endX)**2+(Y-endY)**2 
            e_s_distance = (startX-endX)**2+(startY-endY)**2 

            if not (startX==X==endX or startY==Y==endY) or (e_b_distance > e_s_distance):
                distances.append(e_b_distance)
        answer.append(min(distances)) 
    return answer