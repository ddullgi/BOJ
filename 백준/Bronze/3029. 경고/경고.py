start_time = list(map(int, input().split(":")))
end_time = list(map(int, input().split(":")))

time = [0, 0, 0]
time[2] = end_time[2] - start_time[2]
time[1] = end_time[1] - start_time[1]
time[0] = end_time[0] - start_time[0]
if time[2] < 0:
    time[2] = 60 + time[2]
    time[1] -= 1

if time[1] < 0:
    time[1] = 60 + time[1]
    time[0] -= 1

if time[0] < 0:
    time[0] = 24 + time[0]

if time[0] == time[1] == time[2] == 0:
    time[0] = 24

for i in range(3):
    if time[i] < 10:
        time[i] = "0" + str(time[i])
    else:
        time[i] = str(time[i])

print(time[0]+":"+time[1]+":"+time[2])