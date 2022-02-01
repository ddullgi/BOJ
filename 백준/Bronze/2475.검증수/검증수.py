A = list(map(int, input().split()))
sum_list= 0
for i in A:
    sum_list += i ** 2
    
print(sum_list%10)