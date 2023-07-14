from collections import deque

n,m=map(int,input().split())
maze=[list(map(int,input())) for _ in range(n)]
d=[(1,0),(-1,0),(0,1),(0,-1)]

def bfs():
  q=deque([(0,0)])
  while q:
    x,y=q.popleft()
    for dx,dy in d:
      nx,ny=x+dx,y+dy
      if 0<=nx<n and 0<=ny<m:
        if maze[nx][ny]==1:
          maze[nx][ny]=maze[x][y]+1
          q.append((nx,ny))

bfs()
maze[0][0]=1
print(*maze,sep='\n')
print(maze[n-1][m-1])