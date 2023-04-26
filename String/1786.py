#1786_찾기
def make_table(pattern):
    length = len(pattern)
    table = [0]*length
    j=0

    for i in range(1, length):
        while j > 0 and pattern[i]!=pattern[j]:
            j=table[j-1]

        if pattern[i]==pattern[j]:
            j+=1
            table[i]=j

    return table

def kmp(parent, pattern):
    table = make_table(pattern)
    parent_len = len(parent)
    pattern_len = len(pattern)
    result=[]
    count=0

    j=0
    for i in range(parent_len):
        while j>0 and parent[i]!=pattern[j]:
            j=table[j-1]

        if parent[i]==pattern[j]:
            if j==pattern_len-1:
                result.append(i-pattern_len+2)
                count+=1
                j=table[j]
            else:
                j+=1
    print(count)
    for el in result:
        print(el)

parent = input()
pattern = input()
kmp(parent, pattern)
