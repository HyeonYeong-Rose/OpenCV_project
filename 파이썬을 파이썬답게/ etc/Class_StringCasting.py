#인스턴스 출력형식 지정하기

#2차원 평면 위의 점을 나타내는 Coord 클래스의 인스턴스를 (x값, y값) 으로 출력하기

#Solution1
class Coord(object):
    def __init__(self, x, y):
        self.x, self.y = x,y

point = Coord(1,2)
print('Solution 1 '+'({}, {})'.format(point.x, point.y))

#Solution2
def print_coord(coord):
    print('Solution 2 '+'({}, {})'.format(point.x, point.y))
print_coord(point)

#The most simplest way~!!!!
#__str__메소드 사용해 class내부에서 출력 format지정하기

class Coord1(object):
    def __init__ (self, x, y):
        self.x, self.y = x, y
    def __str__ (self):
        return '({}, {})'.format(self.x, self.y)

point1 = Coord1(1, 2)
print("Simple way: "+ '({}, {})'.format(point1.x, point1.y))