import sys
input = sys.stdin.readline

from heapq import heappop, heappush, heapify

def strjoin(strlen: list) -> int:
    heapify(strlen) # create a min-heap from the list of string lengths
    total_cost = 0
    while len(strlen) > 1:
        first = heappop(strlen) # pop the two smallest lengths
        second = heappop(strlen)
        cost = first + second # the cost of joining these two strings
        total_cost += cost # add to total cost
        heappush(strlen, cost) # push the new length back into the heap
    return total_cost

def main() -> None:
    for _ in range(int(input())):
        n = int(input())
        strlen = list(map(int, input().split()))
        print(strjoin(strlen))

if __name__ == "__main__":
    main()