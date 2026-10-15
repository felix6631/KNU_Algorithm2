import sys
input = sys.stdin.readline
MAX = sys.maxsize
dp_len, dp_cnt = 0, 0
n = 0
S = []
start = 0


def reconstruct(start: int, skip: int, result: list):
    global n, S, dp_len, dp_cnt
    result.append(S[start]) # 1. S[start]는 항상 LIS에 포함
    followers = [] # 2. 뒤에 오는 숫자들과 위치의 목록을 만든다. (숫자, 위치)
    for next in range(start + 1, n):
        if S[start] < S[next] and dp_len[start] == dp_len[next] + 1:
            followers.append((S[next], next))
    followers.sort() # 숫자의 오름차순으로 정렬
    for f in followers: # 3. k번째 LIS의 다음 숫자를 찾는다.
        cnt = dp_cnt[f[1]] # 이 숫자를 뒤에 이어서 만들 수 있는 LIS의 개수를 본다.
        if cnt <= skip: # 건너 뛰어야 할 개수이면
            skip -= cnt # 건너 뛰자.
        else: # 4. 아니면 다음 위치 f[1]에서 재귀 호출
            reconstruct(f[1], skip, result)
            break


def make_count(n: int, S: list) -> list:
    global dp_len
    dp = [1] * (n + 1) #-inf를 포함한 길이 n+1의 DP
    for i in range(n-1, -2, -1): # bottom-up (-1까지)
        if dp_len[i] == 1: #LIS의 길이가 1이면, 그 이후의 수열은 고려하지 않아도 됨
            dp[i] = 1
        else : #아니면 조건에 부합하는 dp[j]의 값을 모두 더함
            ret = 0
            for j in range(i + 1, n):
                if S[i] < S[j] and dp_len[i] == dp_len[j] + 1:
                    ret = min(MAX, ret+ dp[j])
            dp[i] = ret
    return dp


def make_length(n: int, S: list) -> list:
    global dp_len
    dp = [1] * (n + 1) #-inf를 포함한 길이 n+1의 DP
    for i in range(n - 1, -2, -1): # bottom-up (-1까지)
        for j in range(i + 1, n):
            if S[i] < S[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    return dp

def klis(n: int, k: int, S: list) -> None:
    global dp_len, dp_cnt
    S += [-float('inf')]
    dp_len = make_length(n, S) #LIS의 길이 DP
    dp_cnt = make_count(n, S) #LIS의 개수 DP
    optsol = []
    reconstruct(-1, k-1, optsol)
    print(dp_len[-1] - 1) #-inf의 LIS에서 1을 뺀 값이 최적값
    print(*optsol[1:]) #최적해에서 -inf를 제외한 값들을 출력


def main():
    global S, n, k
    for _ in range(int(input())):
        n, k = map(int, input().split())
        S = list(map(int, input().split()))
        
        klis(n, k, S)

if __name__ == "__main__":
    main()