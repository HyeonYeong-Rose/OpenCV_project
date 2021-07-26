#파일 입출력 간단하게 하기

#general way
f=open('mytextfile.txt','r')
while True:
    line = f.readline()
    if not line:
        break
    raw = line.strip().split('\t')
    print(raw)
f.close()

#simple way
#파이썬 with - as 구문 사용하기 - 자동으로 파일 close됨.
# + readlines가 EOF까지만 읽어서 while 안에서 EOF체크 필요없음.

with open('mytextfile.txt')as file:
    for line in file.readlines():
        print(line.strip().split('\t'))