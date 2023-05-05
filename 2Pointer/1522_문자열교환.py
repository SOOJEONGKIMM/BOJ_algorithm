#1522_문자열교환
# <슬라이딩 윈도우 개념>
s=input()
a = s.count('a')

# 교환 후 연속된 a 문자열길이는 입력된 문자열 a개수와 동일
# 즉, a개수와 동일한 길이로 연속된 문자열을 슬라이싱하고,
# 슬라이싱한 문자열 내부의 b와 외부의 a를 교환하면 a가 연속적이게됨
# 교환 횟수는 슬라이싱한 문자열 내부 b 개수와 동일 

s+=s[0:a-1] #원형문자열로 만들기 위해 문자열 늘려주기 (필요한만큼만) 
min_val = float('inf')
for i in range(len(s)-(a-1)):
    min_val = min(min_val, s[i:i+a].count('b'))
    #print(s[i:i+a], s[i:i+a].count('b'))

print(min_val)
