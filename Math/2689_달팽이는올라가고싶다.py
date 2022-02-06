#2869_달팽이는 올라가고 싶다

a,b,v=map(int,input().split())
daily = (v-b) / (a-b)
print(int(daily) if daily==int(daily) else int(daily)+1) #else for float
