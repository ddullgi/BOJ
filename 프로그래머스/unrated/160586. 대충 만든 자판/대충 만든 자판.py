def solution(keymap, targets):
    answer = []
    key = {}
    for keymap_info in keymap:
        for i in range(len(keymap_info)):
            if not key.get(keymap_info[i]) or key.get(keymap_info[i]) > i + 1:
                key[keymap_info[i]] = i + 1
                
    for target in targets:
        count = 0
        for j in target:
            if not key.get(j):
                answer.append(-1)
                break
            else:
                count += key[j]
        else:
            answer.append(count)       
    return answer