import sys
input = sys.stdin.readline

n = 0
w = []
p = []
cache = dict()
items = []

def packing(i, capacity):
    global n, w, p, cache
    if i == n or capacity <= 0:
        return 0
    elif (i, capacity) in cache:
        return cache[(i, capacity)]
    else :
        pick = packing(i + 1, capacity-w[i]) #담는 경우
        skip = packing(i + 1, capacity) #담지 않는 경우
        cache[(i, capacity)] = max(pick + p[i], skip) if capacity >= w[i] else skip #최적값을 캐시에 저장
        return cache[(i, capacity)]

def reconstruct(i, c):
    global n, items, w
    if i == n:
        return []
    elif packing(i, c) == packing(i + 1, c): #담지 않아도 될 경우
        return reconstruct(i + 1, c)
    else: #담아야 하는 경우
        return [items[i][0]] + reconstruct(i + 1, c - w[i])

#knapsack problem
def main():
    global n, w, p, cache, items
    for _ in range(int(input())):
        n, W = map(int, input().split()) #아이템의 수, 배낭 무게
        items = [input().split() for _ in range(n)] # 아이템 집합
        w = [int(item[1]) for item in items] #아이템의 무게
        p = [int(item[2]) for item in items] #아이템의 이익
        cache = dict()
        optval = packing(0, W)
        optsol = reconstruct(0, W)
        print(f"{optval} {len(optsol)}")
        print(*optsol, sep="\n")

if __name__ == "__main__":
    main()