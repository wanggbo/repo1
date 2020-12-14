'''
Created on 2019年7月25日
过滤的
filter(function or None, iterable) --> filter object
如果 传入的第一个的参数是 none 
则会将 iterable 集合里边是 true 的结果 返回成list
如果第一个参数是 fn 
则会将iterable 集合里边是数据使 fn 返回结果是 true 的数据变成list
@author: Administrator
'''
from builtins import filter, list
list1 = filter(None,[0,1,False,True]);
print("展示过滤返回的结果-->" +str(list(list1)));
def odd(n):
    '返回是基数的数据'
    return n%2==1
list1 = filter(odd,range(1,8));    
print("展示过滤返回的结果-->" +str(list(list1)));
# 使用lambda 来简化函数
list1 = filter(lambda n:n%2==1,range(1,8));   
print("展示过滤返回的结果-->" +str(list(list1)));
