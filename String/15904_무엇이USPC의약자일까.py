#15904_USPC는 무엇의 약자일까
uspc_ex = input()
UCPC = ['U','C','P','C']
flag=0
for i in UCPC:
    if flag==0:
        if i in uspc_ex:
            uspc_ex=uspc_ex[uspc_ex.index(i)+1:]
            print(uspc_ex)
            flag+=1
    elif flag==1:
        if i in uspc_ex:
            uspc_ex=uspc_ex[uspc_ex.index(i)+1:]
            flag+=1
    elif flag==2:
        if i in uspc_ex:
            uspc_ex=uspc_ex[uspc_ex.index(i)+1:]
            flag+=1
    elif flag==3:
        if i in uspc_ex:
            uspc_ex=uspc_ex[uspc_ex.index(i)+1:]
            flag+=1

if flag==4:
    print("I love UCPC")
else:
    print("I hate UCPC")
