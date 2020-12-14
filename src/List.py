from builtins import list, zip

# print("我喜欢你,美女啊");
str1 = "我这是测试字符串";
# 单个的字符串
print("查找单个的字符  -->"+str1[2]);
print("默认从0开始长度为6的显示字段"+str(str1[:6]));
# 序列
# 空的列表
list3 = list();
# 拆分列表
list4 = "我要好好的学习";
list4 = list(list4);
print(list4);
# 将远足转化成列表
tupl3 = (1,3,34,5);
tupl3 = list(tupl3);
print("输出元组"+str(tupl3));  
print("找到序列的最大的值"+str(max(tupl3)));
# 返回参数的最小值
print("找到最小的值"+str(min(tupl3)));
# 找到序列的长度  
print("序列的最大值"+str(len(tupl3)));  
# 元组可以
tuple1 = (1,2,4,-1);
# 找到序列的最大的值
print("序列的最大值"+str(max(tuple1)));
# 返回参数的最小值
print("元组的最小值"+str(min(tuple1)));
# 找到序列的长度  
print("元组的长度"+str(len(tuple1)));  
# 元组可以
tuple2 = (2,22,41,-12,23);
print(("获取集合,参数是后边集合再加"+str(sum(tuple2, 2))));
print(("排序, 从小到大排序"+str(sorted(tuple2))));
list1 = [2,22,41,-12,23]; 
print("将列表倒过来,并不是排序,是逆转"+str(list(reversed(list1))));
print("将列表转化成元组,并且添加下标"+str(list(enumerate(list1))));
list2 = [13,84,95,89,39,4];
print("将列表打包,并且将按照最少的数组来合并"+str(list(zip(list1,list2))));
# 函数的创建


