start = input() # 입력은 '열-행' 순서
row = int(start[1])
col = int(ord(start[0])) - int(ord('a')) + 1

# 나이트의 이동 방향 8가지 (행, 열 순서)
# 아래쪽과 오른쪽은 양수, 위쪽과 왼쪽은 음수
steps = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]

# 각 방향 이동 가능성 확인
result = 0
for step in steps:
  # 이동하고자 하는 위치 확인
  next_row = row + step[0] # 행
  next_col = col + step[1] # 열
  # 해당 위치로 이동 가능하면 count 증가
  if next_row >= 1 and next_row <= 8 and next_col >= 1 and next_row <= 8:
    result += 1

print(result)