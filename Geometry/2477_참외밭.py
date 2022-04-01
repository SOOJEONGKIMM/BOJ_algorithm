melon = int(input()) # 참외 개수 K
values = [input().split() for _ in range(6)] # 나머지 2~7 line의 6 줄을 입력 받는다.
directions = [int(v[0]) for v in values] # 방향을 뽑아내서 저장한다.
lengths = [int(v[1]) for v in values] # 길이를 뽑아내서 저장한다.
max_lengths, box_lengths = [], [] # 큰 박스의 길이, 작은 박스의 길이를 담을 배열

for i in range(1, 5):
    if directions.count(i) == 1: # direction이 한번만 존재한다 == 큰 박스의 변
        max_lengths.append(lengths[directions.index(i)]) # 큰박스의 변 길이 저장
        temp = directions.index(i) + 3 # 큰 박스 + 3 == 작은 박스의 변
        if temp >= 6:
            temp -= 6 # cycle을 위해 6 이상일 경우 -6
        box_lengths.append(lengths[temp]) 

area = max_lengths[0] * max_lengths[1] - box_lengths[0] * box_lengths[1]
print(melon * area)
