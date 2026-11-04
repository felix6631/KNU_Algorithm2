import sys
input = sys.stdin.readline

from bisect import bisect_left

def matchorder(n: int, russian: list, korean: list) -> int:
    korean.sort()
    wins = 0
    for i in range(n):
        if korean[-1] < russian[i]: # korean's strongest player cannot beat russian[i]
            korean.pop(0)
        else:
            wins += 1
            korean.pop(bisect_left(korean, russian[i])) # find the first korean player who can beat russian[i] and remove them from the list
    return wins

def main():
    for _ in range(int(input())):
        n = int(input())
        russian = list(map(int,input().split()))
        korean = list(map(int,input().split()))
        print(matchorder(n,russian,korean))

if __name__ == "__main__":
    main()
