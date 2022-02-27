w, h = map(int, input().split())
p, q = map(int, input().split())
tp = tq = int(input())

tp -= w - p
tq -= h - q

tpn = tp // w
tpm = tp % w
tqn = tq // h
tqm = tq % h

if tpn % 2:
    p = tpm
else:
    p = w - tpm

if tqn % 2:
    q = tqm
else:
    q = h - tqm

print(p, q)