#17413_단어뒤집기2
import sys
s=list(sys.stdin.readline().rstrip())
ptr=0
parse_word=''
bracket_flag=False
res=''
while ptr<len(s):
    if s[ptr]=='<':
        parse_word+=s[ptr]
        bracket_flag=True
    elif s[ptr]=='>' and bracket_flag==True:
        parse_word+=s[ptr]
        res+=parse_word
        parse_word=''
        bracket_flag=False
    elif bracket_flag==True:
        parse_word+=s[ptr]
    elif bracket_flag==False:
        if s[ptr]==' ':
            parse_word+=s[ptr]
            res+=parse_word
            parse_word=''
        else:
            parse_word=s[ptr]+parse_word
         
    ptr+=1
    
print(res+parse_word)
