'''
Created on 2019年7月25日
lambda 表达式
作用:可是省下函数定义的过程,
使代码更加的简便
@author: wb
'''
from builtins import str
add  = lambda x,y:print("这是lambda的函数调用"+str(x*y+1));
add(2,3);

