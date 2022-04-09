N = int(input())
plan = []
for _ in range(N):
    S, E = map(int, input().split())
    plan.append((E, S))

plan.sort()
cnt = 0
end_time = 0
for e, s in plan:
    if end_time > s:
        continue
    else:
        end_time = e
        cnt += 1

print(cnt)