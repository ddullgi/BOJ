from collections import deque

def check_word(change_word, words, l, n):
    arr = []
    arr2 = []
    while words:
        flag = [0] * l
        word = words.pop()
        for i in range(l):
            if change_word[i] == word[i]:
                flag[i] = 1
        if sum(flag) == l - 1:
            arr.append(word)
        else:
            arr2.append(word)
    
    return arr, arr2, n + 1
    
            
        

def solution(begin, target, words):
    answer = 0
    if target not in words:
        return 0
    
    Q = deque()
    Q.append((begin, 0))
    L = len(begin)
    
    while Q:
        change_word, n = Q.popleft()
        if change_word == target:
            answer = n
            break
        
    
        change_words, words, N = check_word(change_word, words, L, n)
        
        for i in change_words:
            Q.append((i, N))
    
    return answer