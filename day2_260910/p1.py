import sys
input = sys.stdin.readline


c = int(input())
for t in range(c):
    n, l = map(int, input().split())
    cost = [0] + list(map(int,input().split()))
    _sum = [0] + [0 for _ in range(n)]
    _sum[0] = 0
    _sum[1] = cost[1] 
    for i in range(2,n+1):
        _sum[i] = _sum[i-1] + cost[i]

    

    _min = 1e9
    for day in range(l,n+1):
        for i in range(n-day+1):
            rs = (_sum[i+day] - _sum[i])/day
            _min = min(_min, rs)


     

    print(_min)
