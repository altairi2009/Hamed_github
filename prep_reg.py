import re
NameAge = '''
Hamed is 35 and Salim is 30
Mohammed is 44 and John is 50
'''
ages = re.findall(r'\d{1,3}', NameAge)
names = re.findall(r'[A-Z][a-z]*', NameAge)
ageDict = {}
x = 0
for eachname in names:
    ageDict[eachname] = ages[x]
    x+=1
print (ageDict)


## ---(Fri Dec 29 22:42:30 2017)---

#find a word in a string
import re
if re.search("inform", "we need to inform him with the latest information"):
    print ("there is inform")

#find a list of matches
allinform = re.findall("inform", "we need to inform him with the latest information")
for i in allinform:
    print (i)

#get the starting and edning index of a particular string
str = "we need to inform him with the latest information"
for i in re.finditer("inform", str):
    loctup = i.span()
    print(loctup)


#match words with a particular pattern
str = "Sat, hat, mat, pat"
allstr = re.findall("[shmp]at", str)
for i in allstr:
    print(i)

#match series of range of characters
str1 = "Sat, hat, mat, pat"
someStre = re.findall("[h-m]at", str1)
for i in someStre:
    print (i)

#replace a string
food = "cake pen orange bread"
regex = re.compile("[p]en")
food = regex.sub("eggs", food)
print (food)

# slash problem
randstr = "here is \\hamed"
print(randstr)

#slash problem solved
#randstr = "here is \\hamed"
#print(re.search(r"\\hamed", randstr))


find_man = re.findall ("من", "أكدت الشبكة السورية لحقوق الإنسان أن 411 مدنيا قُتلوا، وشُرد 200 ألف آخرون من قبل قوات النظام السوري وروسيا وإيران في منطقة البوكمال بريف دير الزور الشرقي منذ سبتمبر/أيلول الماضي، وأن هذه القوات انتهكت القانون الدولي الإنساني")
for i in find_man:
    print (i)














