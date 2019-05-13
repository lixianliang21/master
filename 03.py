"""
学习python 第三天

分支结构--if语句的使用

Version : 0.1

Author : Li.xl

Date : 2019-05-13

"""
# 用户身份验证
import getpass

username = input("请输入用户名：")
psw = input("请输入密码：")
#psw = getpass.getpass("请输入密码")
if username =="admin" and psw=="123456":
    print("身份验证通过！")
else:
    print("身份验证失败！")

#判断输入的三条边能否构成三角形，如可以则计算周长和面积
import  math

a = float(input("请输入第一条边： "))
b = float(input("请输入第二条边： "))
c = float(input("请输入第三条边： "))

if a + b > c and  a + c > b and  b + c > a :
    print("这三条边可以构成三角形！","\n三角形周长 ：%.2f"% (a+b+c))
    p = (a + b + c) / 2
    area = math.sqrt(p * (p -a) * (p-b) *(p-c))
    print("三角形的面积：%.2f"%area)
else:
    print("这三条边不能构成三角形！")

# 通过月收入和五险一金计算个人所得税
salary =  float(input("本月收入 : "))
insurance =  float(input("五险一金 ： "))
diff = salary - insurance -3500
if diff <= 0:
    rate = 0
    reduction = 0
elif diff < 1500:
    rate =0.03
    reduction = 0
elif diff < 4500:
    rate = 0.1
    reduction = 105
elif diff < 9000:
    rate = 0.2
    reduction = 555
elif diff < 35000:
    rate = 0.25
    reduction = 1005
elif diff < 55000:
    rate = 0.30
    reduction = 2755
elif diff < 80000:
    rate = 0.35
    reduction = 5505
else:
    rate = 0.45
    reduction = 13505

tax = abs(diff * rate - reduction)
print("个人所得税：￥%.2f元，税率百分之%d"% (tax , rate*100))
print("实际到手收入：￥%.2f元"%(diff-tax +3500))

# 掷骰子决定干什么
from random import  randint

print("掷骰子开始了！")
face = randint(1,6)
if face == 1 :
    result = "唱首歌"
elif face == 2:
    result = "跳个舞"
elif face == 3:
    result = "学狗叫"
elif face == 4:
    result = "做俯卧撑"
elif face==5:
    result = "念绕口令"
else:
    result = "讲冷笑话"

print("掷的骰子是%d"%face,"所以",result,"咯，哈哈哈哈！")


#分段函数求值

x  = float(input("X = "))
if x > 1 :
    y = x *  3 -5
elif x > -1:
    y = x +2
else:
    y = 5 * x +3
print("函数f(%.2f) = %.2f" %(x, y))


#百分制成绩转换为等级制成绩
score  =  float(input("请输入成绩："))
if  score >= 90 :
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >=70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "E"
print("成绩%.2f分对应的等级为："%score,grade)


#英制单位英寸和公制单位厘米互相转换

value = float(input("请输入你要转换的长度："))
unit = input("请输入要转换的单位：")
if unit == "in" or unit == "英寸":
    print("%.2f 英寸 = %.2f 厘米"%(value, value * 2.54))
elif unit =="cm" or unit == "厘米":
    print("%.2f 厘米 = %.2f 英寸"%(value, value / 2.54))
else:
    print("请输入正确的单位(in，cm 或者英寸，厘米)！")

#输入月输入和五险一金计算个人所得税

salary = float(input("请输入本月收入："))
insurance = float(input("请输入本月五险一金："))
print("温馨提示：个税起征点：3500")

diff = salary - insurance - 3500
if diff <= 0:
    rate = 0
    reduction = 0
elif diff < 1500:
    rate = 0.03
    reduction = 0
elif diff < 4500:
    rate = 0.1
    reduction = 105
elif diff < 9000:
    rate = 0.2
    reduction = 555
elif diff < 35000:
    rate = 0.25
    reduction = 1005
elif diff < 55000:
    rate = 0.3
    reduction = 2755
elif diff < 80000:
    rate = 0.35
    reduction = 5503
else:
    rate = 0.45
    reduction = 13505

tax = abs(diff * rate - reduction)
print("个人所得税：%.2f元" % tax)
print("税后实际到手收入为：%.2f元" % (diff - tax+3500))