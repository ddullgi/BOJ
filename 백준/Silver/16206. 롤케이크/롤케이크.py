n, m = map(int, input().split()) 
arr = list(map(int, input().split()))   
l1 = [] 
l2 = [] 

for l in arr:
  if l < 10:
    continue
  elif l % 10 == 0:
    l1.append(l)
  else:
    l2.append(l)
    
l1.sort()
l2.sort()
arr = l1 + l2

cut = 0   
cnt = 0  

for l in arr:
    while True:
        if l < 10:
            break
        elif l == 10:
            cnt += 1
            l -= 10
        else:
            l -= 10
            cnt += 1
            cut += 1
            if cut == m:
                if l == 10:
                    cnt += 1
                print(cnt)
                exit(0)
                
print(cnt)