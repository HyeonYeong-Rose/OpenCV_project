def bisect(a, x, lo=0, hi=None):
    if lo<0:
        raise ValueError('lo must be non-negative.')
    if hi is None:
        hi = len(a)
    while lo < hi:
        mid = (lo+hi)//2
        if a[mid]<x:
            lo = mid+1
        else:
            hi = mid
    return lo

mylist = [1,2,3,7,9,11,33] #list index대로 하면 2
print(bisect(mylist, 3))

#bisect.bisect 메소드 활용하여 간략한 코드짜기
#bisect.bisect(a, x, lo=0, hi=len(a))
#리스트 a에 x값이 들어갈 자리의 인덱스값을 반환합니다.

import bisect
mylist2=[1,2,3,7,9,11,33]
print(bisect.bisect(mylist2, 7))
print('22가 들어갈 자리는 바로바로~~ ')
print(bisect.bisect(mylist2, 22))