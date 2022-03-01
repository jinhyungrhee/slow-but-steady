def fibo(x):
  if x == 1 or x == 2:
    return 1

  return fibo(x - 1) + fibo(x - 2)

print(fibo(4))

# n이 커지면 커질수록 반복해서 호출되는 경우가 많아짐 => 시간 복잡도 : O(2^N)