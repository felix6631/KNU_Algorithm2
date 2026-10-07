import sys
from itertools import product 
input = sys.stdin.readline 

coverType = [
    [(0,0), (1,0), (0,1)],
    [(0,0), (0,1), (1,1)],
    [(0,0), (1,0), (1,1)],
    [(0,0), (1,0), (1,-1)]
]

def find_white(H: int, W: int, board: list) -> tuple :
    for i, j in product(range(H), range(W)):
        if board[i][j] == 0:
            return i, j 
    return -1, -1

def place(board: list, y: int, x: int, type, delta: int, H: int, W: int) -> bool:
    ok = True
    for i in range(3):
        ny = y + coverType[type][i][0]
        nx = x + coverType[type][i][1]
        if not (0 <= ny < H and 0 <= nx < W):
            ok = False 
        else :
            board[ny][nx] += delta
            if (board[ny][nx] > 1):
                ok = False 
    return ok


def cover(H: int, W: int, board: list) -> int :
    y, x = find_white(H, W, board)
    if y == -1:
        return 1 
    else :
        ret = 0
        for type in range(4):
            if place(board, y, x, type, 1, H, W):
                ret += cover(H, W, board)
            place(board, y, x, type, -1, H, W) 
        return ret 


def boardcover(H: int, W: int, board: list) -> int :
    board2 = [[0] * W for _ in range(H)]
    for i, j in product(range(H), range(W)):
        board2[i][j] = [0, 1][board[i][j] == '#']

    if sum([row.count(0) for row in board2]) % 3 != 0:
        return 0
    else :
        return cover(H, W, board2)

c = int(input())
for _ in range(c):
    h, w = map(int, input().split())
    board = [input() for _ in range(h)]
    print(boardcover(h, w, board))

