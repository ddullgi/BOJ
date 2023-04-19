def solution(msg):
    dictionary = {
        "A": 1,
        "B": 2,
        "C": 3,
        "D": 4,
        "E": 5,
        "F": 6,
        "G": 7,
        "H": 8,
        "I": 9,
        "J": 10,
        "K": 11,
        "L": 12,
        "M": 13,
        "N": 14,
        "O": 15,
        "P": 16,
        "Q": 17,
        "R": 18,
        "S": 19,
        "T": 20,
        "U": 21,
        "V": 22,
        "W": 23,
        "X": 24,
        "Y": 25,
        "Z": 26,
    }
    last_index = 26
    answer = []
    l = len(msg)
    i = 0
    while i < l:
        s = str(msg[i])
        
        while dictionary.get(s) and i < l - 1:
            i += 1
            s += msg[i]
        
        if dictionary.get(s):
            answer.append(dictionary[s])     
            break
        else:
            last_index += 1
            answer.append(dictionary[s[:-1]])
            dictionary[s] = last_index      
        
        if i == l - 1:
            answer.append(dictionary[msg[i]])    
            break
    
    return answer