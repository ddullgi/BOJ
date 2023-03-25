def solution(n, words):
    answer = [0, 0]
    order = 1
    stage = 1
    word_list = []
    
    last_word = words[0][0]
    
    for word in words:
        if order > n:
            order = 1
            stage += 1
        
        if word[0] != last_word or word in word_list:
            answer = [order, stage]
            break
        else:
            last_word = word[-1]
            word_list.append(word)
        
        
        order += 1
    
    

    return answer