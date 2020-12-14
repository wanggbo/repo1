# 变量,保存数据
# and	exec	not
# assert	finally	or
# break	for	pass
# class	from	print
# continue	global	raise
# def	if	return
# del	import	try
# elif	in	while
# else	is	with
# except	lambda	yield

counter = 100  # 赋值整型变量
miles = 1000.0  # 浮点型
name = "John"  # 字符串
# print = 1245;
print(counter,miles,name);
 # 连续赋值
a, b, c = 1, 2, "john";
a = b = c = 1
print(a,b,c);

# Python有五个标准的数据类型：
# Numbers（数字）
# String（字符串）
# List（列表）
# Tuple（元组）
# Dictionary（字典）

# type() type方法查看变量的类型
# 数据类型
a = 1
b = "hello"
c = 3.14
d = True
print(type(a))
print(type(b))
print(type(c))
print(type(d))
a = 111
print(isinstance(a, int))
class A:
    pass

class B(A):
    pass

isinstance(A(), A)  # returns True
print(type(A()) == A )     # returns True
isinstance(B(), A)    # returns True
type(B()) == A        # returns False


# int()的作用是将一个字符串或浮点数转换为一个整数,注意如果是foalt类型不允许直接的转化
a = '520'
b = int(a)
print(a,b)
print(a+"1",b+1);
print(str(b)+"1");
print(type(a),type(b))
c = "5.99"
d = int(float(c));
print(c,d)
print(type(c),type(d))
# float()的作用是将一个字符串或整数转换到一个浮点数
a = '5'
b = float(a)
print(a,b)
print(type(a),type(b))
c = 5
d = float(c)
print(c,d)
print(type(c),type(d))
# str()的作用是将一个数或其他类型转换为一个字符串，
a = 5.99
b = str(a)
print(a, b)
print(type(a), type(b))
c = 5
d = str(c)
print(c, d)
print(type(c), type(d))

# input接收的键盘输入结果都是字符串类型，如果接收数字类型需要使用类型转换函数。
c = input("请输入一个数把它赋值给c变量");
print("我在输出c变量的值-->"+c)

age1 = input("年龄：")
print(age1)
print(type(age1))
age2 = int(age1)
print(age2)
print(type(age2))
name = input("姓名：")
age = int(input("年龄："))
height = float(input("身高："))
# 保留2位小数
print("大家好，我叫%s，我今年%d岁了，我的身高是%0.2f米！" % (name,age,height))
#输出结果：大家好，我叫张三，我今年18岁了，我的身高是1.65米！
# 在字符串内部，%s表示用字符串替换，%d表示用整数替换，
# 有几个%占位符，后面就跟几个变量或者值，顺序要对应好。如果只有一个%，括号可以省略。


