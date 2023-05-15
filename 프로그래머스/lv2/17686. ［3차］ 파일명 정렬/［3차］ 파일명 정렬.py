def solution(files):
    answer = []
    arr = []
    for index, file in enumerate(files):
        file = file.lower()
        arr.append([index,'',''])
        number_section = False
        for w in file:
            if w.isdigit():
                number_section = True
                arr[-1][2] += w
            else:
                if number_section:
                    break
                arr[-1][1] += w
        arr[-1][2] = int(arr[-1][2])
    arr.sort(key=lambda x: (x[1],x[2],x[0]))
    return [files[v[0]] for v in arr]