#다음을 만족하는 함수, solution을 완성해주세요.
#solution 함수는 mylist 원소의 행과 열을 뒤집은 한 값을 리턴해야합니다.
#예를 들어 mylist [[1, 2, 3], [4, 5, 6], [7, 8, 9]]가 주어진 경우,
#solution 함수는 [[1, 4, 7], [2, 5, 8], [3, 6, 9]] 을 리턴하면 됩니다.

#mylist의 원소의 길이는 모두 같습니다.
#mylist의 길이는 mylist[0]의 길이와 같습니다.
#각 리스트의 길이는 100 이하인 자연수입니다.

def ListSwift(mylist):
    answer = []
    for i in range(len(mylist[0])):
        temp = []

        for j in range(len(mylist)):
            temp.append(mylist[j][i])
            #print(temp)
        answer.append(temp)

    return answer

a=ListSwift([[1,2,3],[4,5,6],[7,8,9]])
#print('a = ' ,a)

#zip함수 사용하면 더 효율적이야~
def SwiftBetter(mylist):
    ans = list(map(list, zip(*mylist)))
    return ans

b=SwiftBetter([[1,2,3],[4,5,6],[7,8,9]])
#print('b = ', b)