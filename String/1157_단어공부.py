#1157_단어공부

word = input().upper()

#alpha = list(range(97,122))
#Alpha = list(range(65, 90))

cntalp = []
for i in set(word):
    cntalp.append(word.count(i))

pos = [i for i, x in enumerate(cntalp) if x==max(cntalp)]

if len(pos)>1: print("?")
else: print(list(set(word))[cntalp.index(max(cntalp))])
'''

for i in alpha:
     cntalp.append(word.find(chr(i)))
     print(cntalp)

print(max(cntalp))
'''
