#모든 멤버 type 변환하기
#스트링으로 인풋을 받았으면 아웃풋으로 정수형을 리턴하는 함수를 만드세요

def change(mylist):
    answer=list(map(int, mylist))
    return answer

mylist=['12','14']
print(change(mylist))

#이차원 리스트의 원소의 길이를 담은 리스트 만들기
#[[1, 2], [3, 4], [5]]-------> [2, 2, 1]

def length(mylist):
    answer = list(map(len, mylist))
    return answer

mylist = [[1,2,3,4,5],[1,2,3]]
print(length(mylist))
