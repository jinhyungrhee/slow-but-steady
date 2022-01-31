# 1이 될 때까지 - 단순하게 풀기

n, k = map(int, input().split())

result = 0

# N이 K 이상이라면 K로 계속 나누기
while n >= k:
  # N이 K로 나누어 떨어지지 않는다면 N에서 1씩 빼기
  while n % k != 0:
    n -= 1
    result += 1
  # 그렇지 않으면(= N이 K로 나누어지면) K로 나누기
  n //= k
  result += 1

# 마지막으로 남은 수에 대하여 1씩 빼기
while n > 1:
  n -= 1
  result += 1

print(result)


# N이 100억 이상의 큰 수가 되는 경우, 일일이 1을 빼는 방식은 느리게 동작할 수 있음
# => 더 효율적인 방법 존재!