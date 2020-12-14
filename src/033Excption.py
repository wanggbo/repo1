'''
Created on 2019年10月17日
异常的处理
@author: wb
'''
try:
#     类型出错抛出异常
    int("abc");
    f = open("我是一个文件");
    print(f.read());
    f.close();
# 操作系统的异常
except OSError as  reason:
    print("出错了"+str(reason));
except TypeError as reason:
    print("类型出错"+str(reason));
except ValueError as reason:
    print("转化出错"+str(reason));
    
    
# 组合异常
try:
#    类型出错抛出异常
    f = open("我是一个文件");
    print(f.read());
    f.close();
    sum = 1+"1";
# 操作系统的异常
except (OSError,TypeError) :
    print("我是组合的异常,其中有一个问题出错就可以捕获");

# finally的用法
try:
    f = open("一个文件.txt","w");
    f.write("我是文件的内容");
except (OSError,TypeError):
    print("出错了,finally 的用法,不管处不出错都要执行到");
finally:
    f.close();
    print("不管系统是否出错,finally里边的语句都可以执行");
    




