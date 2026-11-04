import sys
input = sys.stdin.readline
import math

#Prim's Algorithm
def lan(n: int, W: list) -> float:
    dist = [W[0][i] for i in range(n)] # 출발 정점은 0번 정점
    ret = 0
    for _ in range(n - 1):
        # 현재까지 방문한 정점 집합에서 가장 가까운 정점을 찾는다.
        min = float('inf')
        for u in range(1, n):
            if 0 <= dist[u] < min:
                min = dist[u]
                vnear = u

        # 찾은 정점을 방문한다.
        ret += math.sqrt(dist[vnear])
        dist[vnear] = -1
        # 현재까지 방문한 정점 집합과의 거리를 업데이트한다.
        for u in range(1, n):
            if dist[u] > W[u][vnear]:
                dist[u] = W[u][vnear]
    return ret


def main() -> None:
    for _ in range(int(input())):
        n, m = map(int, input().split())
        x = list(map(int, input().split()))
        y = list(map(int, input().split()))
        W = [[0] * n for _ in range(n)]
        for u in range(n):
            for v in range(u, n):
                W[u][v] = W[v][u] = (x[u] - x[v]) ** 2 + (y[u] - y[v]) ** 2
        for _ in range(m):
            u, v = map(int, input().split())
            W[u][v] = W[v][u] = 0
        print(f"{lan(n, W):08f}")

if __name__ == "__main__":
    main()