# N, M을 공백으로 구분하여 입력받기
n, m = map(int, input().split())

# 방문한 위치를 저장하기 위한 맵을 생성하여 0으로 초기화 - 리스트 컴프리헨션 문법 사용
d = [[0] * m for _ in range(n)]
#print(d)

# 현재 캐릭터의 X 좌표, Y 좌표, 방향을 입력 받기
x, y, direction = map(int, input().split())
d[x][y] = 1 # 현재 좌표 방문 처리

# 전체 맵 정보 입력받기
array = []
for i in range(n): # 행의 수 만큼 반복
  array.append(list(map(int, input().split())))

# 북, 동, 남, 서 방향 정의
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 왼쪽으로 회전
# 북:0, 서:3, 남:2, 동:1
def turn_left():
  global direction
  direction -= 1
  if direction == -1:
    direction = 3

# 시뮬레이션 시작
count = 1
turn_time = 0
while True:
  # 1.현재 방향에서 왼쪽으로 회전
  turn_left()
  nx = x + dx[direction]
  ny = y + dy[direction]
  # 2. 회전 후 정면에 가보지 않은 칸이 존재하는 경우 이동
  if d[nx][ny] == 0 and array[nx][ny] == 0:
    d[nx][ny] = 1
    # 현재 위치 업데이트
    x = nx
    y = ny
    count += 1
    turn_time = 0 # 직진
    continue
  # 회전한 이후 정면에 가보지 않은 칸이 없거나 바다인 경우
  else:
    turn_time += 1 # 이를 네번 반복하면 네 방향 모두 갈 수 없는 경우임!
  # 3.네방향 모두 갈 수 없는 경우
  if turn_time == 4:
    nx = x - dx[direction] 
    ny = y - dy[direction]
    # 뒤로 갈 수 있으면 뒤로 이동!
    if array[nx][ny] == 0:
      x = nx
      y = ny
    # 뒤가 바다로 막혀있는 경우
    else:
      break # 움직임을 멈춤
    turn_time = 0

# 정답 출력
print(count)