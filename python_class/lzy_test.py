print("小丑最帅！")
print("你最丑")
print("努力学习python第一天")
# python注释：
# 1.单行注释：#
# 2.多行注释“”“或‘’‘
# 3.快捷键：ctrl+/，可以选中多行进行多行注释，再次执行可以取消注释
'''
print("我要学习！")
print("加油！")
'''
print("我要多喝水哦")
'''
python基础语法：
1）对缩进非常敏感，会报错，除非多行代码有父子关系，都要顶格编写
2）没有分号；
3)区分大小写

常用数据类型：整型（int）、浮点型（float）、布尔型（bool）：True（1）  False（0）
字符串（str）:被成对的引号包裹的内容字符串
确定数据类型：
1.type（）：内置函数、判断数据类型
2.isinstance（）：结果是bool：True--类型对   False--类型错
'''
print(type(3.1415926535))
print(isinstance(12.1, int))
'''
字符串（str）:被成对的引号包裹的内容字符串：单、双、三引号都可以
三引号：多段内容可保持编写格式
'''
print(type("猜猜我是什么类型"))
print('''----李自月----
name:李自月   age:24
hobby:运动
        自我评价：非常好
''')
'''
变量：存储数据==保险柜：钱、金条---用来存储东西
数据类型：int  float  bool str
变量名：标识符---只能是字母、数字、下划线，不能以数字开头
名字见名知意
变量名一定要先申明（定义并赋值），再调用，否则报错
'''
info = "今天喝了几杯水"  # 定义了一个变量，赋值
name = "李自月"
print(name, info)

'''
字符串的操作：
1.取值：位置--索引，从0开始，依次加1
2.取多个值：切片：[开始：结束：步长]==取头不取尾
  开头省略的话从0开始取，尾省略的话默认末尾结束，步长省略默认为1
3.负数，-1为取最后一个，指从相反的方向取
4.元素个数：len()--内置函数，统计元素个数
5.替换字符串里的元素：replace()、
6.查找：find()  、index（）、 
'''
str1 = '我今天很开心阿'
# 想要取“我”字，需要给“我今天很开心阿”每个字赋值为01234567，我值为0
print(str1[0])
print(str1[0:3:1])
print(len(str1))
print(str1[2:len(str1):3])
str1 = str1.replace('开心', '难过')
print(str1)
print(str1.index('我'))  # 如果元素没有找到，会报错，代码终止运行
print(str1.find('我'))  # 元素没有找到，不会报错，返回-1
print(str1.count('天'))  # 计数，看此变量中包含几个’天‘

'''
格式化输出:
第一种：（必须会）
1.占位符：{}--传变量的地方   .format()
2、.format（）可以默认按顺序传入变量：也可以指定位置传入变量===注意不能混合使用
第二种：（不常用，做了解）
%s--字符串（可以匹配所有变量）   %d--整数   %f--小数
'''
# 格式化输出第一种案例
name = "李自月"
age = 18
hobby = "学习"
print('''----{1}----
name:{1}
age:{0}
hobby:{3}
'''.format(age, name, age, hobby))

# 格式化输出第二种案例
name = "李自月2"
age = 18
hobby = "学习"
print('''---%s---
name:%s
age:%s
hobby:%s
''' % (name, name, age, hobby))

'''
python运算符：
1、算数运算符：+ - * / % **
2.赋值运算符：=  +=  -=  :方向性，右边赋值给左边
3、比较运算符:<  ≤  ＞ ≥  == !=  返回结果是bool 布尔值 True/False
4、逻辑运算符：与：and 或：or 非：not
5、成员运算符：in、not in
'''
print(10 + 20)  # 两个数字相加
print('love' + 'you')  # 两个字符串的拼接
print(str(123) + 'abc')
# int --》 str:str()--强制字符串的转化，int（）--整型  float（）  bool（）
print(30 - 10)  # 两个数字相减
print(2 * 3)  # 两个数字相乘
print('I love you' * 3000)  # 字符串重复输出*次数
print(10 / 3)  # 除法，结果浮点型

a = 5
b = 8
print(a + b)
a = a + 10  # 此写法== a+=10
print(a)
a += 10
print(a)

print(1 > 2)
print('我饿了' == '我饿了')  # 判断字符串是否相同

print(1 > 2 and 3 > 2)

# 作业
name = 'musne'
age = 18
sex = 'nan'
print('*' * 20)
print('''
name:{0}
sex:{2}
age:{1}
'''.format(name, age, sex))
# 作业2：现有字符串str1='python hello aaa 123123aabb'
# 1.请取出并打印字符串中的‘python’
# 2.请分别判断’oa' ‘he’ 'ab'是否是该字符串中的成员
# 3.替换‘python’为‘lemon’
# 4.找到‘aaa’的位置
# 1.
str1 = 'python hello aaa 123123aabb'
print(str1[0:6:1])
# 2.
print('oa' in str1)
print('he' in str1)
print(str1.find('ab'))
# 3
print(str1.replace('python', 'lemon'))
# 4
print(str1.find('aaa'))

'''
常用数据类型续：列表（list）：[]  元组（tuple）()  字典dict{}  集合
列表（list）：[],元素之间用英文逗号隔开
1.元素可以是任意的数据类型：int float bool  str list....
2、取值：用索引取值--类比字符串，取多个值：切片
扩展：列表的嵌套取值
3、列表的元素是可以被改变的！：增加，修改，删除
4、列表元素可以重复，用count可以统计数量
5、len()--统计元素个数
'''
list1 = [1997, 10.11, "李自月", '李若彤', [6, 6, 6, 6]]
print(list1)

# 取值
print(list1[2:4:1])

# 增加
list1.append('胡一天')  # 默认追加到末尾
print(list1)
list1.insert(2, '多多')  # 指定位置进行元素插入
print(list1)
list1.extend(['刘亦菲', '陈晓', '华梦录'])  # 两个列表合并
print(list1)

# 删除
list1.pop(0)  # 指定位置进行删除
list1.remove('胡一天')  # 指定元素本身进行删除
# list1.clear()  清除列表所有元素，很少用

# 修改：取值--重新赋值
list1[4] = '章若楠'
print(list1)

list1.append('刘亦菲')
print(list1)
print(list1.count('刘亦菲'))  # 统计列表中刘亦菲有几个
print(len(list1))  # 统计列表所有元素个数

# 元组tuple，符号（）
# 元素可以为任意类型，不可修改，可将其转换为列表修改
tuple1 = ('李大为', '杨树', '夏诘', '赵继伟')
print(tuple1)
list2 = list(tuple1)  # 元组转化为列表
list2[2] = '曹建军'
print(list2)
tuple2 = tuple(list2)  # 列表转化为元组
print(tuple2)
'''
字典：dict {}
1、元素：key、value(键值对)
2、应用场景：存储数据属性
key: 不能是可以任意改变的数据类型 （list、dict）---字符串
    不能重复
value:可以是任意数据类型---可以被改变===增删改
3、字典是没有顺序的！！！---不能用索引进行取值， 取值：用key取value
'''

dict1 = {'name': '鲁班', 'height': '50', 'weight': '39'}
print(dict1)
print(dict1['height'])  # 用key取值
print(dict1.get('weight'))  # 第二种取值方法
dict1['weight'] = '98'  # 修改体重为98，如果key不存在，则新增键值对
dict1.update({"city": "王者峡谷", "hobby": "推塔"})  # 字典增加多个键值对
print(dict1)

# 删除
dict1.pop('weight')  # 指定key删除对应的键值对

'''
集合：set {}  元素单个
    1.无序
    2.元素不可以重复。  使用场景：去重
做了解：面试会问用过集合吗？ 回答：这个项目中用很少，但是我知道他是无序的而且元素不可以重复的类型
'''
list3 = [11, 22, 33, 44, 33, 11]  # 列表去重，将列表转为集合，再转化为列表
set1 = set(list3)
print(set1)

'''
控制流：代码的执行顺序--从上至下依次执行，用判断、循环来控制
判断：if 语法
if 条件：--成立---进入子代码：格式：冒号：缩进（4个空格=tab键）
    子代码（执行语言）
elif 条件：---成立
    执行语句（子代码）
...(elif可以没有，可以有多个)
else：---可以没有
    执行语句
'''
# money=int(input('请输入你的余额：'))   #input（）控制台输入--数据类型：字符串
# if money >=500:
#     print('买别墅')
# elif money >=200:
#     print('买一栋楼')
# elif money >=50:
#     print('买一辆车')
# else:
#     print ('滚去上班赚钱！')


# 作业：a=[1,2,6,'summer']请用成员运算符判断i是否在这个列表里面
a = [1, 2, 6, 'sunmmer']
print('i' in a)
# dict_1={"class_id":45,'num':20} 请判断班级上课人数是否大于5，注：num表示课堂人数。如果大于5，输出人数
dict_1 = {"class_id": 45, 'num': 20}
num = 20
if num >= 5:
    print(dict_1['num'])
# 作业：将列表用字典表示，在以列表形式打印
li = ['李自多', '濮阳', '王多', '18', '女', '20', '日本', '男']
dict_li = {'name': '李自多', 'age': '18', 'city': '濮阳'}
dict_wang = {'name': '王多', 'age': '20', 'city': '日本'}
li_x = []
li_x.append(dict_li)
li_x.append(dict_wang)
print(li_x)

'''
for循环：遍历 数据对象里的所有元素：str,list,tuple,dict
for 变量名 in 数据对象：
循环多次由元素个数决定
中断：break   continue
range（）---内置函数：生成一个整数序列：1，2，3，4，5，6   跟for循环一起使用：star-开始，==默认值=0，stop-结束，step--步长。取值取头不取尾
'''
count = 0  # 计数器
list_h = ['赵盼儿', '顾千帆', '欧阳旭', '孙三娘', '皇城司']
for name in list_h:
    if name == '欧阳旭':  # false
        # break   #跳出整个循环
        continue  # 跳出本次循环
    print(name)
    print('*' * 20)
    count += 1
print(count)

for i in range(0, 5, 1):
    print(i)

