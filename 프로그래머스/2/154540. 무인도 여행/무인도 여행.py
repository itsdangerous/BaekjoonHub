from collections import deque

def check(r, c, N, M) -> bool :
    return 0 <= r < N and 0 <= c < M

def bfs(maps) :
    dr, dc = [-1, 0, 1, 0], [0, 1, 0, -1]
    result = []
    N = len(maps)
    M = len(maps[0])
    
    visited = [[False for _ in range(M)] for _ in range(N)]
    que = deque()
    for i in range(N) :
        for j in range(M) :
            if visited[i][j] : continue
            if maps[i][j] == 'X' : 
                visited[i][j] = True
                continue
            hap = 0
            que.append([i, j])
            hap += int(maps[i][j])
            visited[i][j] = True
            
            while(que) :
                cur = que.popleft()
                for d in range(4) :
                    nr = cur[0] + dr[d]
                    nc = cur[1] + dc[d]
                    if not check(nr, nc, N, M) : continue
                    if visited[nr][nc] : continue
                    if maps[nr][nc] == 'X' : 
                        visited[nr][nc] = True
                        continue
#                     숫자일 경우
                    visited[nr][nc] = True
                    que.append([nr, nc])
                    hap += int(maps[nr][nc])
                    # print(nr, nc, hap)
            result.append(hap)
            
    return result
    
def solution(maps):
    flag = False
    for i in maps :
        for j in i :
            if j != 'X' :
                flag = True
                break
    return [-1] if not flag else sorted(bfs(maps))
