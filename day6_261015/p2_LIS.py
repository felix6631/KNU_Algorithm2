import sys
input = sys.stdin.readline


def reconstruct(end, prev, S):
    if end == -1:
        return []
    return reconstruct(prev[end], prev, S) + [S[end]]


def lis(n, S):
    dp = [1] * n
    prev = [-1] * n

    for i in range(n):
        for j in range(i):
            if S[j] < S[i] and dp[j] + 1 > dp[i]:
                dp[i] = dp[j] + 1
                prev[i] = j

    end = max(range(n), key=lambda i: dp[i])
    return dp[end], end, prev

def main():
    for _ in range(int(input())):
        n = int(input())
        S = list(map(int, input().split()))

        optval, end, prev = lis(n, S)
        optsol = reconstruct(end, prev, S)
        print(optval)
        print(*optsol, sep=" ")


if __name__ == "__main__":
    main()

