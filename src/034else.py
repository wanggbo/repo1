'''
Created on 2019年10月18日

@author: wb
'''

if 1<0:
    print("我是if 的语句");
else:
    print("else 的语句");


try:
    int("abc");
except ValueError  as reason:
    print("如果没有错误,try里边的语句完成的话,走else");
else:
    print("我是else的语句");

def getMaxFactor(num):
    #while 正常运行完了 就可以执行else
    count = num // 2;
    while count > 1:
        if num % count == 0:
            print("%d最大的素数是%d" %(num,count));
            break;
        count -= 1;
    else:
        print("如果while 是正常的循环完成的我才可以执行");
        print("%d是素数" %num);
num = int(input("请输入一个数"));
getMaxFactor(num);




