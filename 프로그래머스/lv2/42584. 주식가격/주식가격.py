def solution(prices):
    answer = []
    l = len(prices)
    
    for i in range(l):
        count = -1
        price = prices[i]
        for j in range(i, l):
            count += 1
            if prices[j] < price:
                answer.append(count)
                break
        else:
            answer.append(count)
        
    return answer