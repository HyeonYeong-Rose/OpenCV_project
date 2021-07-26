#최솟값을 저장하는 변수에 아주 큰 값을 할당할 때
#inf는 어떤 숫자와 비교해도 무조건 크다고 판정됩니다.

min_val = float('inf')
print(min_val > 1000000000000000000000) #True 출력

#inf에 음수 기호도 붙여서 그 어떤 수보다도 작은 수를 만들수도 있습니다.
max_val = float('-inf')
print(max_val>100000000000000) #False
print(max_val<100000000000000) #True