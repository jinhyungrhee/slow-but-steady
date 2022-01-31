# 1이 될 때까지 - 더 효율적인 방법 **

# N이 K의 배수가 되도록 효율적으로 한 번에 빼는 방식
# - 배수 만들기 : target = (n // k) * k
# - 입력 값에서 배수를 빼서 -1 횟수를 카운트 : result += (n - target)

n, k = map(int, input().split())

result = 0

while True:
  # (N == K로 나누어떨어지는 수)가 될 때까지 1씩 빼기 **
  # (N == K로 나누어떨어지는 수)가 될 때까지 빼는 계산을 한 큐에 처리!
  target = (n // k) * k
  result += (n - target)
  n = target
  # N이 K보다 작을 떄(= 더 이상 나눌 수 없을 때) 반복문 탈출
  if n < k:
    break
  # N을 K로 나누기
  result += 1
  n //= k

# 마지막으로 남은 수에 대하여 1씩 빼기
result += (n - 1)
print(result)
