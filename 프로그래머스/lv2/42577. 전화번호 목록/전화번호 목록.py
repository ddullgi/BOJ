def solution(phone_book):
    answer = True
    l = len(phone_book)
    phone_book.sort()
    i = 1
    while i < l:
        
        if len(phone_book[i - 1]) >= len(phone_book[i]):
            pass
        elif phone_book[i - 1] == phone_book[i][:len(phone_book[i - 1])]:
            answer = False
            break
        i += 1
    return answer