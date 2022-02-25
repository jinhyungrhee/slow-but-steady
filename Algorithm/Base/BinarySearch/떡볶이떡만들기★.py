''' <파라메트릭 서치(parametric search)>
- 파라메트릭 서치 : '최적화 문제'를 '결정 문제'(=예/아니오로 답하는 문제)로 바꾸어 해결하는 기법
- '원하는 조건을 만족하는 가장 알맞은 값을 찾는 문제'에 주로 사용!
- 범위 내에서 조건을 만족하는 가장 큰 값을 찾으라는 최적화 문제라면 이진 탐색으로 결정 문제를 해결하면서 범위를 좁혀갈 수 있음!
  (= 중간점의 값은 시간이 지날수록 '최적화되 값'을 찾기 때문)
- TIP:
  - 적절한 높이를 찾을 때까지 절단기의 높이 h를 반복해서 조정
    ->'현재 이 높이로 자르면 조건을 만족할 수 있는가?'를 확인한 뒤에 조건의 만족 여부(예/아니오)에 따라서 
      탐색 범위를 좁혀서 해결 가능
  - 절단기 높이가 최대 10억까지이므로 순차 탐색이면 시간 초과 -> 이진 탐색(2^31 == 31번만에 탐색 가능)
  - 떡의 개수 N이 최대 100만 개이므로, (이진탐색으로) 절단기의 높이 h를 바꿀 때마다 모든 떡을 체크하면
    최대 3,000만번의 연산으로 문제 해결 가능
'''

# n : 떡의 개수, m : 요청한 떡의 길이
n, m = list(map(int, input().split()))
# 각 떡의 길이 저장
array = list(map(int, input().split()))

# 이진 탐색을 위한 시작점과 끝점 설정
start = 0
end = max(array)

# 이진 탐색 수행
result = 0
while(start <= end):
  total = 0
  # 중간값 : 최적화된 절단기의 높이 
  mid = (start + end) // 2

  for x in array:
    # 잘랐을 때의 떡의 양 계산
    if x > mid:
      total += x - mid

  # 떡 양이 부족한 경우 더 많이 자르기(= 왼쪽 부분 탐색)
  if total < m:
    end = mid - 1
  # 떡 양이 많은 경우 덜 자르기(= 오른쪽 부분 탐색)
  else:
    # 최대한 덜 잘랐을 때가 정답이므로, 이곳에서 result 기록 **
    result = mid
    start = mid + 1

print(result)


'''my solution(순차탐색 -> 시간초과)

def cut(array, length, target):
  result = 0
  for elem in array:
    if elem > length:
      result += elem - length

  if result >= target:
    return True
  else:
    return False

n, m = list(map(int, input().split()))

ddeok = list(map(int, input().split()))

ddeok.sort()

max_val = 0
for i in range(ddeok[0], ddeok[n-1]):
  if cut(ddeok, i, m):
    max_val = max(max_val, i)

print(max_val)
'''