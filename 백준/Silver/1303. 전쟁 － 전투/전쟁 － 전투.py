def bfs(x, y, team):
    queue = [(x, y)]
    count = 0
    while queue:
        cx, cy = queue.pop(0)
        if visited[cy][cx]:
            continue
        visited[cy][cx] = True
        count += 1
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = cx + dx, cy + dy
            if 0 <= nx < N and 0 <= ny < M and not visited[ny][nx] and battlefield[ny][nx] == team:
                queue.append((nx, ny))
    return count

# 입력 받기
N, M = map(int, input().split())
battlefield = [input().strip() for _ in range(M)]

visited = [[False] * N for _ in range(M)]

our_power = 0
enemy_power = 0

# 모든 위치를 확인하며 BFS 실행
for y in range(M):
    for x in range(N):
        if not visited[y][x]:
            team = battlefield[y][x]
            team_count = bfs(x, y, team)
            if team == 'W':
                our_power += team_count ** 2
            else:
                enemy_power += team_count ** 2

# 결과 출력
print(our_power, enemy_power)
