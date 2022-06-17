'''
函数：封装成函数，调用。===提高代码的复用率，提高执行的效率
def 函数名（）：
    子代码（函数体）--实现功能
注意：函数只定义了 没有调用，不会执行：写函数名调用

函数里不固定的数据---定义成函数里的参数--括号里
1.形参--函数定义的时候，用来定义
2.实参：调用参数传入参数

参数定义的类型：
1.必备参数：定义了就必须要传入的参数--不传会报错
2.默认参数（缺省参数）：可以定义的时候赋值一个默认值--调用的时候可以不传入；可以传替换掉默认值
默认参数必须在必备参数后面！！！
3.不定长参数（*args）：接受不确定数量、个数，--可以不传，可以传入（1个、多个）==元组接收
**kwargs:用字典接受，用关键字进行传参

传参的方式类型：
1.位置传参：按照位置传入参数
2.关键字传参：指定参数名来进行传参
3.混合传参:注：关键字传参必须跟在位置传参后边
'''

#
# def good_job():
#     salary = 8000
#     bonus = 2000
#     subsidy = 500
#     sum1 = salary + bonus + subsidy
#     print("这个工作的工资总和是{}".format(sum1))
# good_job()


# def good_job(salary, bonus, subsidy):
#     sum1 = salary + bonus + subsidy
#     print("这个工作的工资总和是{}".format(sum1))
# good_job(8000, 2000, 500)

# def good_job(salary, bonus, subsidy, *args, **kwargs):  # 定义函数==函数的参数
#     sum1 = salary + bonus + subsidy  # sum1 实现功能
#     print('salary的值:{}'.format(salary))
#     print('bonus的值:{}'.format(bonus))
#     print('subsidy的值: {}'.format(subsidy))
#     print('args的值: {}'.format(args))
#     print('kwargs的值: {}'.format(kwargs))
#     for i in args:
#         sum1 += i
#     for j in kwargs:
#         # print(kwargs.get(j))   通过key值取到value
#         sum1 += kwargs[j]
#     print('这个工作的工资总和是:{}'.format(sum1))
# good_job(8000, 2000, 500, 50, 30, 80, a=100, b=200)  # 用函数名进行函数调用

'''
有进有出：进--参数，出--返回值
返回值：函数可以给到外面的人用的数据，做后续操作，---调用函数的时候，可以获取到这个返回值--return
如果没有返回值--none， 多个返回值--元组保存

'''


def good_job(salary, bonus, subsidy, *args, **kwargs):
    sum1 = salary + bonus + subsidy
    for i in args:
        sum1 += i
    for j in kwargs:
        # print(kwargs.get(j))   通过key值取到value
        sum1 += kwargs[j]
    return sum1   #定义了一个返回值，两个返回值的话用逗号隔开
result = good_job (8000, 2000, 500)  # 用函数名进行函数调用
if result >=10000:
    print('这是一个不错的工作！')
else:
    print('我还可以找到更好的工作！')
