mylist=list(input())
answer = []
mylist1 = list(map(int,mylist))
for i in mylist1:
    if i % 2 == 0:
        answer.append(i**2)
print(answer)

#list comprehension 으로 for 문과 if 문을 한 번에 처리하기

mylist2=[3,2,4,5,7]
ans = [number**2 for number in mylist2 if number % 2 ==0]
print(ans) #[4, 16]