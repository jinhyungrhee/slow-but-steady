# 계산된 결과를 저장하는 메모이제이션 리스트 초기화
d = [0] * 100

# 재귀호출 + 메모이제이션 => 탑다운 다이나믹 프로그래밍
def fibo(x):
  # 호출되는 함수 확인
  print('f(' + str(x) + ')', end=' ')
  # 종료 조건
  if x == 1 or x == 2:
    return 1
  # 이미 계산된 문제라면 그대로 반환
  if d[x] != 0:
    return d[x]
  # 아직 계산하지 않은 문제라면 점화식에 따른 결과 반환
  d[x] = fibo(x - 1) + fibo(x - 2)
  return d[x]

print(fibo(6))