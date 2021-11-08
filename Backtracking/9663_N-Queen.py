#9663_N-queen
n=int(input())
board_row = [0] * n
res=0
visited=[False]*n


def promising_check(cur_col):
    for i in range(cur_col):
        if abs(board_row[cur_col]-board_row[i]) == cur_col-i:
            return False
    return True

def n_queen(cur_col):
    global res
    #visited[cur_col-1]=False
    if cur_col == n:
        res += 1
        return 
    for i in range(n):
        if visited[i]:
            continue
        board_row[cur_col]=i
        if promising_check(cur_col):
            visited[i]=True
            n_queen(cur_col+1)
            visited[i]=False

n_queen(0)            
print(res)
