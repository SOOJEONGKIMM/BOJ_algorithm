#2447_별 찍기-10

def star(n, x):
    res=[]
    if n==3:
        return x
    else:
        for i in x:
            res.append(i*3)
        for i in x:
            res.append(i+" "*len(x)+i)
        for i in x:
            res.append(i*3)
        return star(n//3,res)
    
if __name__ == "__main__":
    n=int(input())
    three = ['***','* *','***']
    final = star(n,three)
    for i in final:
        print(i)
