def solution(fees, records):
    answer = []
    a = {}
    for i in records:
        time, number, io = i.split()
        h, m = map(int, time.split(":"))
        Mtime = h * 60 + m
        if a.get(number):
            if a[number]["io"] == "IN":
                a[number]["time"] += Mtime - a[number]["t"]
            else:
                a[number]["t"] = Mtime
            a[number]["io"] = io
                
        else:
            a[number] = {"time": 0, "t": Mtime , "io": io}
    
    b = []
    for number, d in a.items():
        fee = 0
        
        if d["io"] == "IN":
            d["time"] += 1439 - d["t"]
        
        if d["time"] < fees[0]:
            fee = fees[1]
        else:
            pfee = 0
            if (d["time"] - fees[0]) % fees[2]:
                pfee = ((d["time"] - fees[0]) // fees[2] + 1) * fees[3]
            else:
                pfee = ((d["time"] - fees[0]) // fees[2]) * fees[3]
            fee = fees[1] +  pfee
        
        b.append((int(number), fee))
    b.sort()
    for n, f in b:
        answer.append(f)
    return answer