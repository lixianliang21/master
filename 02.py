"""
使用input函数输入
使用int()进行类型转换
使用占位符格式话输出的字符串

Version;0.1
Author:Li.xl
"""

a= int(input("a = "))
b= int(input("b = "))
print('%d + %d = %d ' %(a,b,a+b))
print('%d + %d = %d ' % (a,b,a+b))
print('%d - %d = %d ' % (a,b,a-b))
print('%d * %d = %d ' % (a,b,a*b))
print('%d / %d = %d ' % (a,b,a / b))
print('%d // %d = %d ' % (a,b,a / b))
print('%d %% %d = %d ' % (a,b, a % b))
print('%d ** %d = %d ' % (a,b,a ** b))

"""
使用type()检查变量的类型

Version: 0.1
Author: li.xl
Date: 2019-05-01
"""
a = 100
b = 12.345
c = 1 + 5j
d = "hello world"
e = True
print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))

​"""
输入年份，计算是否闰年，是输出True ,否则输出False

Version : 0.1
Author : Li.xl
Date : 2019-05-12
"""
year = int(input("请输入要判定的年份："))
is_leap = (year % 4 ==0 and year % 100 !=0 or
           year % 400 == 0)
if  is_leap:
    print("%d年份是闰年"%year)
else:
    print("%年份不是闰年"%year)

