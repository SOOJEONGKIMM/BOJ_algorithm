import sys 
left=["(","["]
right = [")","]"]
checka=0
checkb=0
check=0
while True:    
        inp = str(sys.stdin.readline().rstrip())
        #inp=input()
        if inp=='.':
                break
        stack=[]
        s =list(map(str,inp.split()))
        checka, checkb, check = 0,0,0
        for i in s:
                ss = list(i)
                while len(ss)!=0:
                        cha = ss.pop(0)
                        if cha not in left and cha not in right:
                                continue
                        elif cha in left:
                                if cha==left[0] and checka!=-1:
                                        checka+=1
                                        check=1
                                        stack.append(cha)
                                elif cha==left[1] and checkb!=-1:
                                        checkb+=1
                                        check=2
                                        stack.append(cha)
                                
                        elif cha in right:
                                if cha==right[0] and check!=2:
                                    if len(stack)!=0 and stack.pop()!=left[0]:
                                        check=5
                                        break
                                    else:
                                        checka-=1
                                        check=0
                                elif cha==right[1] and check!=1:
                                    if len(stack)!=0 and stack.pop()!=left[1]:
                                        check=5
                                        break
                                    else:
                                        checkb-=1
                                        check=0
                                else:
                                    check=5
                                    break
                               
                if check==5:
                    break
        
        if checka!=0 or checkb!=0 or check==5:
                print("no")
        else:
                print("yes")
        check=0
