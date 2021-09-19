#2941_크로아티아 알파벳
cro = input()

alph=['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

for i in alph:
    cro = cro.replace(i, '*')
    
print(len(cro))
