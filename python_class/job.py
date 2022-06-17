# #第一天 作业
# name = 'musne'
# age = 18
# sex = 'nan'
# print('*' * 20)
# print('''
# name:{0}
# sex:{2}
# age:{1}
# '''.format(name, age, sex))
# # 作业2：现有字符串str1='python hello aaa 123123aabb'
# # 1.请取出并打印字符串中的‘python’
# # 2.请分别判断’oa' ‘he’ 'ab'是否是该字符串中的成员
# # 3.替换‘python’为‘lemon’
# # 4.找到‘aaa’的位置
# # 1.
# str1 = 'python hello aaa 123123aabb'
# print(str1[0:6:1])
# # 2.
# print('oa' in str1)
# print('he' in str1)
# print(str1.find('ab'))
# # 3
# print(str1.replace('python', 'lemon'))
# # 4
# print(str1.find('aaa'))

# # 第二天
# # 作业1：a=[1,2,6,'summer']请用成员运算符判断i是否在这个列表里面
# 第一种：
# a = [1, 2, 6, 'sunmmer']
# print('i' in a)
# 第二种
# a = [1, 2, 6, 'sunmmer']
# if "i" in a:
#     print('i是成员')
# else:
#     print('不是')
# 作业2.dict_1={"class_id":45,'num':20} 请判断班级上课人数是否大于5，注：num表示课堂人数。如果大于5，输出人数
# dict_1 = {"class_id": 45, 'num': 20}
# num =dict_1.get('num')
# if num >= 5:
#     print('班上的人数是{}'.format(num))
# else:
#     print('上课人数不足5人')
# # 作业：将列表用字典表示，在以列表形式打印
# li = ['李自多', '濮阳', '王多', '18', '女', '20', '日本', '男']
# dict_li = {'name': '李自多', 'age': '18', 'city': '濮阳'}
# dict_wang = {'name': '王多', 'age': '20', 'city': '日本'}
# li_x = [dict_li,dict_wang]
# # li_x.append(dict_li)
# # li_x.append(dict_wang)
# print(li_x)

# 第二种方式：for循环：遍历数据
# li = ['李自多',  '王多']
# li1 = ['濮阳', '日本']
# li2= [ '18', '20']
# li3=[]
# for i in range(2):
#     dict1=dict(name=li[i],city=li1[i],age=li2[i])
#     li3.append(dict1)
# print(li3)

# 第四天
# 作业1：把字符串转成列表[]
# list1=list('我想看电视')
# print(list1)

# # # 作业2，生成成一个整数序列，里面全是数字，求里边所有数字的和
# li = []
# for i in range(6):
#     # sun+=i
#     li.append(i)
# print(li)
# print(sum(li))
#
#
# # 作业3，定义函数：判断一个对象（列表、字典、字符串）的长度是否大于5，如果大于5，输出true，否则输出false
def dx(args):
    # if type(args) == dict or type (args) == list or type(args)==str:
    #     if len(args) > 5:
    #         return True
    # return False

    if isinstance(args , (list, dict, str)):
        if len(args) > 5:
            return True
    return False


li = [1, 2, 2, 3, 4,4]
res = dx(li)
print(res)
# tuple1=(tuple(dudu))
# print(len(tuple1))
# num=6
# if num >5:
#     print(True)
# else:
#     print(False)

# 练习题
# str1='123我今天'
# print(len(str1))
# print(str1[0:3])
# print(str1.find('我'))

dict1 = {'name': '鲁班', 'height': '50', 'weight': '39'}
print(dict1)
print(dict1['height'])  # 用key取值
print(dict1.get('weight'))  # 第二种取值方法
dict1['weight'] = '98'  # 修改体重为98，如果key不存在，则新增键值对
dict1.update({"city": "王者峡谷", "hobby": "推塔"})  # 字典增加多个键值对
print(dict1)