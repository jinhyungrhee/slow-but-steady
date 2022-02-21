n, k = tuple(map(int, input().split()))

A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort()
B.sort(reverse=True)

for i in range(k):
  # 비교 연산 필요! - A의 원소가 더 작은 경우에만 교체
  if A[i] < B[i]:
    A[i], B[i] = B[i], A[i]
  else:
    # 정렬되어 있으므로 더 비교할 필요 없이 반복문 탈출
    break

print(sum(A))