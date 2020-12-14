'''
Created on 2019年7月25日
字典也就是 json 数组
@author: Administrator
'''
# 空字典
dct1 = {'key1':'val1','key2':'val2'};
# 数组的键值对
dct2 = {1:'val1',2:'val2'};
print('键值对的访问'+dct1['key2']);
print('键值对的访问'+dct2[1]);
print('用get方法来获取'+dct2.get(1));
# 付默认值
print('用get方法来获取'+dct2.get(3,'不存在'));
# 校验数据是否存在
print(1 in dct2 );
# 转化成字段
dict1 = dict((('key1',1),('key2',2)));
print('键值对的访问'+str(dict1));
# 关键字的参数
print(str(dict(学生=0,老师='联系')));
# 改变键值对
dict1['key1']='改变了';
print('我修改了键值对'+str(dict1));
# 如果没有键值对.就会添加
dict1['key3']='我添加了';
print('我添加了键值对'+str(dict1));
# 创建并返回新的数据,旧的不变,会创建新的数据
# dict.fromkeys(type, iterable, value)
dict2 = {};
dict2 = dict2.fromkeys((1,2,3),'val');
print('我添加了键值对'+str(dict2));

seq = ('Google', 'Runoob', 'Taobao');
 
dict3 = dict.fromkeys(seq)
print ("新字典为 : %s" %  str(dict3));
 
dict3 = dict.fromkeys(seq, 10)
print ("新字典为 : %s" %  str(dict3));
# 不会修改值,会重新创建数据
dict3 = dict3.fromkeys(('Google',  'Taobao'), '该值了');
print ("新字典为 : %s" %  str(dict3));

# 获取所有的key
dict4 = dict.fromkeys(range(10), '添值了');
print ("新字典为 : %s" %  str(dict4));
# 打印所有的key
for item in dict4.keys():
    print("输出key %s" %item);
# 打印所有的val
for item in dict4.values():
    print("输出val %s" %item);
# 打印所有的键值对
for item in dict4.items():
    print(item);

# 清空字典
a = {'1':2,'2':4};
b = {1:2,3:4};
# 会将b也清空掉
a.clear();

# 删除数据,删除指定剑
dict4.pop(2);
print ("新字典为 : %s" %  str(dict4));

# 随机删除键值对
dict4.popitem();
print ("新字典为 : %s" %  str(dict4));
# 添加数据
dict4[9] = 'ii';
print ("新字典为 : %s" %  str(dict4));
dict4.setdefault('数据',10);
print ("新字典为 : %s" %  str(dict4));

# 跟新数据,用b来更新4,并且返回值
a = {1: 2, 2: 2};
b = {1: 1, 3: 3};
dict4.update(b);
print(dict4);


