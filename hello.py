# a = 10
# a = 1111111111111111111110000000000000000000000000
# print('hello world')
# print("ggggg")
# if 10 < 100:
#   print("가나다")
#   print("eeeee")
#
# print("cccc")
#
# while 10 < 100:
#   print("bbbbbb")
#   break
#   print("eegggg")
# print("end")
# print( int(10 / 3))
#
# print("sss\n"
#       "ddddd"
#       "ffff")
#
# aaa={'aaaa','bbbb','cccc'}
# bbb={'dddd','bbbb','ffff'}
# print(aaa.union(bbb))
#
# if 10 > 5:
#   print(11)
# elif 20 < 5:
#     print(22)
#
# result = input("숫자 입력:")
# print("입력 숫자:",result);
#
# c = print("입력숫자2",input("숫자입력하세요"))
#
# def circle_area(a): return a * a * 3.14
# def square_area(a, b): return a * b / 2
# def triangel_area(a, b): return a * b
#
# ss = True
# while ss == True:
#   ii = input("삼각 1, 사각 2, 원 3 ,종료 4 : ")
#   if ii == '1':
#     # print("입력하신 삼각형의 넓이는 " + str(square_area(int(input("밑변: ")), int(input("높이: ")))) + " 입니다")
#     print("입력하신 삼각형의 넓이는 {0} 입니다.".format(square_area(int(input("밑변: ")), int(input("높이: ")))))
#   elif ii == '2':
#     print("입력하신 사각형의 넓이는 " + str(triangel_area(int(input("가로: ")), int(input("세로: ")))) + " 입니다")
#   elif ii == '3':
#     print("입력하신 원의 넓이는 " + str(circle_area(int(input("반지름: ")))) + " 입니다")
#   elif ii == '4':
#     print("종료합니다.")
#     ss = False
#   else:
#     print("잘못된 입력입니다.")
# 
# class GString:
#   def __init__(self,value):
#     self.Value = value
#     print("Class test = ",value)
#   def __sub__(self,str):
#     for i in str:
#       self.content = self.content.replace(i,'')
#       return GString(self.content)
#   def __del__(self):
#       print("Class del")
# 
#   def tsprt(self,val):
#     print("test prt " + val)
# 
#   def Remove(self,str):
#     return self.__sub__(str)
# 
# def foo():
#   d = GString(10)
#   d.tsprt("send msg")
# 
# cc = GString.tsprt(None,"aaadd")
# # cc = GString.tsprt("aaadd")
# print( cc )
# foo()

for n in {1,3,5,7,9}:
  (x%2==0) for x in {1,2,3,4,5,6,7,8,9,10}:
    print("{0}  {1}   {2}".format(n,x,n*x))
    
