#숫자를 차례로 곱해 나온 수가 제곱수가 되면 found,아니면 not found 출력

import math
num=1
numbers = [int(input()) for _ in range(0,5)]

print(numbers)

for i in numbers:
    num*=i
    if math.sqrt(num)==int(math.sqrt(num)): #제곱수가 존재한다면
        print('found')
        break

else:
    print('not found')