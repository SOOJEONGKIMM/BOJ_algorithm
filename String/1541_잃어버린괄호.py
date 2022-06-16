#1541_잃어버린 괄호
a=input().split('-')
new=[]
for i in a:
    if len(i)>1:
        b=list(map(int,i.split('+')))
        b=sum(b)
        new.append(b)
    else:
        new.append(int(i))
res=new[0]
for i in range(1,len(new)):
    res-=new[i]

print(res)
