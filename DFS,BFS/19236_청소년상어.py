#19236_청소년상어
import sys
import copy



def move_fish(x_shark, y_shark, graph):
    #번호가 낮은 물고기부터 순차 이동
    for fish in range(1, 17):
        pos = find_fish(graph, fish)
        #해당 물고기가 살아있는경우
        if pos:
            x_fish, y_fish = pos[0], pos[1] #좌표 리턴
            direction = graph[x_fish][y_fish][1]
            #반시계 45도 회전
            for _ in range(len(d)):
                nx_fish = x_fish + d[direction][0]
                ny_fish = y_fish + d[direction][1]
                if 0<=nx_fish<4 and 0<=ny_fish<4:
                    if not (nx_fish==x_shark and ny_fish==y_shark):
                        #해당방향을 진행방향으로 
                        graph[x_fish][y_fish][1]=direction
                        #물고기 위치 서로 바꾸기
                        graph[nx_fish][ny_fish], graph[x_fish][y_fish] = graph[x_fish][y_fish], graph[nx_fish][ny_fish]
                        break
                
                direction = (direction+1) %len(d) #방향 이동 
                
def find_fish(graph, fish):
    for i in range(4):
        for j in range(4):
            if graph[i][j][0]==fish:
                return [i,j]

#상어 이동좌표 구하기 
def get_movable_pos(x_shark, y_shark, graph):
    direction = graph[x_shark][y_shark][1]
    pos = []
    for _ in range(3):
        x_shark += d[direction][0]
        y_shark += d[direction][1]
        if 0<=x_shark<4 and 0<=y_shark<4 and graph[x_shark][y_shark][0]!=-1:
            pos.append([x_shark, y_shark])
    return pos

def dfs(x_shark, y_shark, graph, eat):
    global answer
    graph = copy.deepcopy(graph)
    #상어가 해당 물고기 먹음
    eat += graph[x_shark][y_shark][0]#물고기 번호의 합의 최댓값 구하는 문제
    graph[x_shark][y_shark][0]=-1 #먹은 애는 표시
    move_fish(x_shark, y_shark, graph) #물고기이동
    position = get_movable_pos(x_shark, y_shark, graph)

    if position:
        for nx_shark, ny_shark in position:
            dfs(nx_shark, ny_shark, graph, eat)
    else:
        answer = max(answer, eat)
        return
    
if __name__ == '__main__':
    graph = [[0]*4 for _ in range(4)]
    for i in range(4):
        data = list(map(int,sys.stdin.readline().split()))
        for j in range(4):
            graph[i][j] = [data[2*j], data[2*j+1]-1]
            #물고기번호, 방향정보 저장
            #-1을 한 이유는 방향 인덱스가 0부터 시작하기 때문 

    d = [(-1,0),(-1,-1),(0,-1),(1,-1),(1,0),(1,1),(0,1),(-1,1)]
    #진행방향: 상, 좌상, 좌, 좌하, 하, 우하, 우, 우상
    #방향 b 인덱스 12345678을 01234567로 봄 

    #(0,0)에서 시작
    x_shark = y_shark = 0
    answer = 0
    dfs(x_shark, y_shark, graph, 0)
    print(answer)
