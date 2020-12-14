'''
Created on 2019年7月25日
算法
@author: Administrator
'''
# 递归
from builtins import str
def recur(n):
    if n == 1:
        return 1;
    else:
        return  n*recur(n-1);
# num = int(input("请输入一个整数"));
# print('递归函数的结果'+str(recur(num)));
# 首先明白界限,结束的条件
def recur2(n):
    if n==2 or n==1:
        return 1;
    else:
        return recur2(n-1)+recur2(n-2);
rtn = recur2(7);
# print('递归函数的结果'+str(recur2(7)));
# print('递归函数的结果%d对兔子' %rtn);
print('%d递归函数的结果%d对兔子' %(rtn,recur(3)));


# 汉诺塔
def hanoi(n,x,y,z):
    if n==1:
        print("将"+x+'-->'+z );
    else :
        hanoi(n-1,x,z,y);
        print("将"+x+'-->'+z );
        hanoi(n-1,y,x,z);
hanoi(3, "x", "y", "z");
