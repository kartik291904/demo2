# def takeScreenshot(driver,name):
#     driver.get_screenshot_as_file('/Users/kavyavijay/PycharmProjects/pythonProject1/'+name+'.png')
# str = 'karthik'
# for i in str:
#     print(i)




str = 'im home home'  ##em ohem ohmi
l1=[]
for j,i in  enumerate(str):
    if i==' ':
        l1.append(j)
print(l1)
str=str.replace(' ','')
str=str[::-1]
for  i in  l1:
    str=str[:i]+' '+str[i:]
print(str)



#
# l2=[68,3,9,34,78]
# for i in range(len(l2)):
#     for j in range(i+1,len(l2)):
#         if l2[i]>l2[j]:
#             l2[i],l2[j]=l2[j],l2[i]
# print(l2)
# print(sorted(l2))
#
# var='dad'
# if var==var[::-1]:
#     print('palidromme')
# else:
#     print('not  palindromme')
#
#
# dic={'a':9,'b':3,'c':4}
# print(dict(sorted(dic.items(),key=lambda items:items[1])))
#
#
# list=[7,2,1,6,5,4,5]
# k=9
# for i in range(len(list)):
#     for j in range(i+1,len(list)):
#         if list[i]+list[j]==k:
#             print(list[i],list[j])
#
# def feb(n):
#     a=0
#     b=1
#     while a<=n:
#         yield a
#         c=a+b
#         a=b
#         b=c
#     return b
#
# n=int(input('no: '))
# f1=feb(n)
#
# for i in f1:
#     print(i)
#
# import string
#
# my_string = "Hello! How are you? I'm doing well, thanks."
# str1=''
# for i in my_string:
#     if i not in string.punctuation:
#         str1=str1+i
#
# print(str1)

# my_dict = 'ieiieffjstdtdbi'
# dic={}
# for i in my_dict:
#     if i in dic:
#         dic[i]=dic[i]+1
#     else:
#         dic[i]=1
# print(dic)
# x=max(dic,key=dic.get)
# print(x)


import math


# def sqrt(n):
#     num = math.isqrt(n)
#     num1 = num * num
#     return num1 == n
# print(sqrt(9))
# import math
#
# var=math.factorial(10)
# var=str(var)
# count=0
# for i in var[::-1]:
#     # print(i)
#     if i=='0':
#         count=count+1
#     else:
#         break
# print(count)




# str='kaaarthik'
#
# dic={}
# for i in str:
#     if i in dic:
#         dic[i]=dic[i]+1
#     else:
#         dic[i]=1
# print(dic)
# x=max(dic,key=dic.get)
# print(x)
#
# dic={'a':5,'f':1,'g':9}
# x=dict(sorted(dic.items(),key=lambda item:item[1],reverse=True))
# print(x)
#
# list=[1,2,3,2,3,4,5,6]
# count=0
# dic1={}
# for i in list:
#     if i in dic:
#         pass
# print(list)
# print(count)
#
# st='hello world'
# print(st[-5:])
#
#

