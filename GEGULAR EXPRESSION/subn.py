import re
# t=re.subn('\d','xxxx','a7b9k5t9k')
# print(t)


# count=0
# p=re.compile('ab')
# m=p.finditer('abaababa')
# for i in m:
#     count=count+1
#     # print("start="{},'end='{},'group='{}.format(i.start(),i.end(),i.group()))
#     print('group={} start={} end={}'.format(i.group(),i.start(),i.end()))
#     #print(i.group(),"-----------",i.start(),i.end())
# print(count)

# m=re.finditer('.','abcbca abcau fbc')           
# # [abc],[^abc],[a-z],[0-9],[a-zA-Z]
# for i in m:
#     print(i.group(),'-----------',i.start(),i.end())

# m=re.match('a','bdkdjkdkvn')
# if m!=None:
#     print("Match is available at begining")
# else:
#     print("dose not match")
    

# m=re.fullmatch('bdkdjkdkvn','bdkdjkdkvn')
# if m!=None:
#     print("Match is available at begining")
# else:
#     print("dose not match")

s=input("Enter the pattern :")
m=re.search(s,"uehwsdkjskgsa665gnnvd")
if m!=None:
    print("Match is available")
    print("First occurence with stating index: {} and ending index: {}".format(m.start(),m.end()))
else:
    print("dose not match")




















