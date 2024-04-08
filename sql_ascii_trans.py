import binascii
import re

txt=open("444.txt","r")
content=txt.readlines()
# print(content)
a=[]
for i in content:
    xx = re.findall("262\n", str(i), re.S)
    print(xx)
    print(i)
    if xx!=[]:
        # print(i)
        a.append(i)
    else:
        content
# print(a)
list_len=len(a)
list = []
list_str=[]
aaa=0
for c in range(list_len+2):
    for i in a:
        yy = re.findall("^\d+\\t",i,re.S)
        # print(i)
        # print(yy)
        for k in re.findall("\d+", str(yy), re.S):
            num1=int(k)
            # print(num1)
        if num1 == aaa:
            content_str=re.findall("\d+", str(yy), re.S)
            for q in a:
                qq = re.findall("\\t\d+\\t", i, re.S)
                for t in re.findall("\d+", str(qq), re.S):
                    num2 = chr(int(t))
                    # print(num2)

            list.append(i)
            list_str.append(num2)
            break
        else:
            continue
    aaa = 1 + aaa


print(list)
# 列表倒叙
list_str.reverse()
print(list_str)
xx=""
for xxx in list_str:
    xx=xxx+xx
print(xx)
# print(list)
# admin :zpf088

# print(a)