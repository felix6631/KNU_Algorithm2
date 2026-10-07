import sys
input = sys.stdin.readline 

c = int(input())


linked = {
    0 : [0, 1, 2],
    1 : [3, 7, 9, 11],
    2 : [4, 10, 14, 15],
    3 : [0, 4, 5, 6, 7],
    4 : [6, 7, 8, 10, 12],
    5 : [0, 2, 14, 15],
    6 : [3, 14, 15],
    7 : [4, 5, 7, 14, 15],
    8 : [1, 2, 3, 4, 5],
    9 : [3, 4, 5, 9, 13]
}

sequence = [
    (8, linked[4]),
    (11, linked[1]),
    (13, linked[9]),
    (6, linked[3]),
    (10, linked[2]),
    (7, linked[7]),
    (4, linked[8]),
    (1, linked[0]),
    (3, linked[6]),
    (0, linked[5])
]
def clocksync(clocks) :
    ret = 0 
    for clock, linked_clock in sequence:
        cnt = (4 - clocks[clock]) % 4
        for other in linked_clock: 
            clocks[other] = (clocks[other] + cnt) % 4
        ret += cnt
    return -1 if any(clocks) else ret 


# __main__
for _ in range(c):
    clocks = [(int(x) // 3 % 4) for x in input().split()]
    print(clocksync(clocks))


