# 숫자를 담은 리스트 mylist가 solution 함수의 파라미터로 주어집니다.
# solution 함수가 mylist의 i번째 원소와 i+1번째 원소의 차를 담은 일차원 리스트에 차례로 담아 리턴하도록 코드를 작성해주세요.
# 단, 마지막에 있는 원소는 (마지막+1)번째의 원소와의 차를 구할 수 없으니, 이 값은 구하지 않습니다.
# mylist의 길이는 1 이상 100 이하인 자연수입니다.
# mylist의 원소는 1 이상 100 이하인 자연수입니다.
# 예시 input=[83, 48, 13, 4, 71, 11], output=[35, 35, 9, 67, 60]
# 83과 48의 차는 35입니다. 48과 13의 차는 35입니다. 13과 4의 차는 9입니다......

def subtract(mylist):
    answer = []

    for i in range(len(mylist)-1):
        here = mylist[i] - mylist[i + 1]
        if here < 0:
            here = -here
        answer.append(here)
    return answer


a = subtract([83, 48, 13, 4, 71, 11])
print(a)

#zip함수 이용하면 인덱스 사용하지 않고 각 원소 접근 가능
def solution(mylist1):
    ans=[]
    for num1, num2 in zip(mylist1, mylist1[1:]):
        a = num1 - num2
        ans.append(a)
    return ans

if __name__ == '__main__':
    mylist1 = [10,9,8,7]
    print(solution(mylist1))