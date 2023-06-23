def solution(participant, completion):
    answer = ''
    complete_list = {}
    for name in completion:
        if complete_list.get(name):
            complete_list[name] += 1
        else:
            complete_list[name] = 1
    for name in participant:
        if not complete_list.get(name) or complete_list.get(name) == 0:
            return name
        else:
            complete_list[name] -= 1
