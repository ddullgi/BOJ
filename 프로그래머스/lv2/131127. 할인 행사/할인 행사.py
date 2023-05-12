def solution(want, number, discount):
    answer = 0

    total_want = []
    for goods, num in zip(want, number):
        total_want.extend([goods] * num)

    for i in range(len(discount)-9):
        discount_goods = discount[i:i+10]

        if sorted(discount_goods) == sorted(total_want):
            answer += 1

    return answer