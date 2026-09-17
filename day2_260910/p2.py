import sys
input = sys.stdin.readline

#Kadane's Algorithm
def solution(n: int, lst: list) -> int:
    cur, _max = 0, 0
    for i in range(n):
        cur = max(cur, 0) + lst[i]
        _max = max(_max,cur)
    return _max
    
t = int(input())
for _ in range(t):
    n = int(input())
    lst = list(map(int,input().split())) 
    print(solution(n,lst)) 



