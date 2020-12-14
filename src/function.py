'''
Created on 2019年7月24日
函数的创
@author: wb
'''
# 必须先定义函数,再调用 def define声明的意思 
from builtins import str, int
def fn1():
    print("这是我的第一的函数")
#     nameI = input("请输入你的名字");
#     print("你好"+nameI);
    print("你好 小李");

# 调用函数
fn1();
# 带参数的函数
def fn2(nameI):
   print("你好"+nameI);
fn2("李四");
# 有返回值的参数
# 返回数据的最大值
def check(num1,num2):
    return num1 if num1>num2 else num2
print("我输入数字的最大值"+str(check(5, 6)));
# 返回集合的参数
def back(num1,num2):
    '多个的话,会变成元组返回'
    return num1,num2
print("返回的参数是元组"+str(back(5, 6)));

# 参数的不确定,集合参数
def fn4(*num4):
    for i in num4:
        print("我正在输出参数-->"+str(i));
fn4(1,"lisi",3);
# 集合参数主意参数的位置
def fn8(*num4,num2):
    for i in num4:
        print("我正在输出参数-->"+str(i));
    print("集合参数的其他的参数-->"+str(num2));
    
fn8(1,"lisi",3,num2 ='李四');
# 最好是在集合参数的后边的参数付默认值
def fn9(*num4,num2='5'):
    for i in num4:
        print("我正在输出参数-->"+str(i));
    print("集合参数的其他的参数-->"+str(num2));
    
fn9(1,"lisi",3,num2 ='李四');


# 可选参数
def fn5(num1,num2=5):
    return num1 if num1>num2 else num2;
print("我输入数字的最大值"+str(fn5(2)));
# 参数的健壮性

def fn6(num1,num2):
    if isinstance(num1, int) and isinstance(num2, int):
        return num1 if num1>num2 else num2;
    else:        
        return "你在逗我么,传递的是什么的参数-->"+str(num1)+"--->"+str(num2);
print("我输入数字的最大值"+str(fn6('a', 11)));
# 函数文档
def fn7(num1,num2):
    '首先校验数据的准确定'
    if isinstance(num1, int) and isinstance(num2, int):
        return num1 if num1>num2 else num2;
    else:        
        return "你在逗我么,传递的是什么的参数-->"+str(num1)+"--->"+str(num2);
print(fn7.__doc__);

    
    
