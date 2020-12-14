'''
Created on 2019年7月25日
map
map(func, *iterables)
fn 会将 iterables 的里边的每个参数进行
操作,然后返回修改后的集合
@author: Administrator
'''
from builtins import map, str, list
# print(help(map));
list1 =  map(lambda x:x+1,range(1,8,2));
print("这是map修改后的结果"+ str(list(list1)));
