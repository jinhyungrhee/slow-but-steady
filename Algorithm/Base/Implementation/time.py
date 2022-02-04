'''
완전 탐색(Brute Forcing)
'''

h = int(input())

count = 0
for i in range(h+1):
  for j in range(60):
    for k in range(60):
      # 매 시각 안에 '3'이 포함되어 있다면 count 증가
      if '3' in str(i) + str(j) + str(k):
        print(str(i)+str(j)+str(k))
        count += 1

print(count)