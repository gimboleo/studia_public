import heapq


n, p = [int(x) for x in input().split()]
ts = [int(x) for x in input().split()]


for i, t in enumerate(ts): ts[i] = (t, i)
ts.sort()


res = [None for i in range(n)]
queue = []
phantasmal_queue = []                                                       #Priority queue - pop() returns the smallest element
idx = 0
clock = 0

for i in range(n):
    if not queue and not phantasmal_queue: clock = ts[idx][0]

    while idx < n and ts[idx][0] <= clock + p:
        if not queue or queue[-1] > ts[idx][1]: queue.append(ts[idx][1])    #Queue is always in decreasing order
        else: heapq.heappush(phantasmal_queue, ts[idx][1])
        idx += 1

    print(queue, phantasmal_queue)

    clock += p
    res[queue.pop(0)] = clock
    if not queue and phantasmal_queue: queue.append(heapq.heappop(phantasmal_queue))


print(*res)