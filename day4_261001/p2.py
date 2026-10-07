import sys 
input = sys.stdin.readline 





def fence(h):
    h.append(0)
    stack = []
    ret = 0
    for i in range(len(h)):
        while stack and h[stack[-1]] >= h[i]:
            j = stack.pop()
            width = i if not stack else (i-stack[-1]-1)
            ret = max(ret, h[j] * width)
        stack.append(i)
    return ret


for _ in range(int(input())):
    n = int(input())
    h = list(map(int, input().split()))
    print(fence(h))
