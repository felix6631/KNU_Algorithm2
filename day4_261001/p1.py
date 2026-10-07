import sys 
input = sys.stdin.readline 

def get_next(quadtree):
    get_next.idx += 1
    return quadtree[get_next.idx - 1]

def quadtree_reverse(quadtree):
    head = get_next(quadtree)
    if head in "bw":
        return head 
    else :
        qt1 = quadtree_reverse(quadtree) 
        qt2 = quadtree_reverse(quadtree) 
        qt3 = quadtree_reverse(quadtree) 
        qt4 = quadtree_reverse(quadtree) 
        return "x"+qt3+qt4+qt1+qt2 

for i in range(int(input())):
    quadtree = input()
    get_next.idx = 0
    reversed = quadtree_reverse(quadtree)
    print(reversed)


