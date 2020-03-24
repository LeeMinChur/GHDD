from collections import Counter
list1=['커피','햄버거','커피','피자','콜라','콜라']
b=list(set(list1))
print(b)
c=[]
for i in b:
    c.append(list1.count(str(i)))

print(c)
