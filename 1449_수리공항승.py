#1449
N, L = map(int, input().split())
leak = list(map(int, input().split()))
leak.sort()
start = leak[0]
end = leak[0]+L
tape = 1

for i in range(N):
    if start<= leak[i] < end:
        continue
    if end > 1000:
        continue
    else:
        start = leak[i]
        end = leak[i]+ L
        tape += 1

print(tape)
