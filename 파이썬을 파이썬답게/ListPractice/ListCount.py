#가장 많이 등장하는 알파벳 찾기
import collections
from collections import Counter

my_str = input().strip()

counter = Counter(my_str).most_common()
answer = ""

for i in range(len(counter)):
    if counter[i][1]==counter[0][1]:

        answer += counter[i][0]

print(''.join(sorted(list(answer))))


my_list = [1, 2, 3, 4, 5, 6, 7, 8, 7, 9, 1, 2, 3, 3, 5, 2, 6, 8, 9, 0, 1, 1, 4, 7, 0]
ans = collections.Counter(my_list)

print(ans[1]) # = 4
print(ans[3])  # = 3
print(ans[100]) # = 0

#반복문 사용
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 7, 9, 1, 2, 3, 3, 5, 2, 6, 8, 9, 0, 1, 1, 4, 7, 0]
answer = {}
for number in my_list:
    try:
        answer[number] += 1
    except KeyError:
        answer[number] = 1

print(answer[1]) # = 4
print(answer[3])  # = 3
print(answer[100])  # =  raise KeyError