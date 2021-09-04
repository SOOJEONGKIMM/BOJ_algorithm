#2621
import sys
input = sys.stdin.readline
cards = []
color_cnt = {
    'R':0,
    'B':0,
    'Y':0,
    'G':0,
    }
number_cnt = [0]*10


def card_game():
    #1 5장 모두 같은색, 숫자가 연속적.
    if 5 in color_cnt.values(): #[0,5,0,0]
        successive = 0
        max_num = 0

        
        for cnt, i in enumerate(number_cnt):
            if number_cnt[cnt] == 1:
                successive += 1
                max_num = cnt
                if successive == 5:
                    break
            else:
                successive = 0
                continue
           
        if successive == 5:
            output = 900 + max_num
            return output    

    #2 5장 중 4장 숫자 같음.
    if 4 in number_cnt:
        ind = number_cnt.index(4)
        output = 800 + ind

        return output

    #3 5장 중 3장 숫자 같고 나머지 2장도 숫자 같음.
    if 3 in number_cnt and 2 in number_cnt:
        ind3 = number_cnt.index(3)
        ind2 = number_cnt.index(2)
        output = ind3*10 + ind2 + 700

        return output

    #4 5장 모두 같은 색
    if 5 in color_cnt.values():
        max_num=0
        for cnt, i in enumerate(number_cnt):
            if number_cnt[cnt] >= 1:
                max_num = cnt
            else:
                continue
        output = max_num + 600
        return output

    #5 5장 숫자 연속적.
    successive = 0
    max_num = 0
    for cnt, i in enumerate(number_cnt):
        if number_cnt[cnt]==1:
            successive += 1
            max_num = cnt
            if successive == 5:
                break
        else:
            successive = 0
            continue
    if successive == 5:
        output = max_num + 500
        return output

    #6 5장 중 3장 숫자 같음.
    if 3 in number_cnt:
        output = number_cnt.index(3) + 400
        return output

    #7 5장 중 2장 숫자 같고 또 다른 2장도 숫자 같음.
    twotwo=0
    max_num =0
    min_num =9
    for cnt, i in enumerate(number_cnt):
        if i == 2:
            twotwo += 1
            max_num = max(cnt, max_num)
            min_num = min(cnt, min_num)
    if twotwo == 2:
        output = max_num * 10 + min_num + 300
        return output

    #8 5장 중 2장 숫자 같음.
    if 2 in number_cnt:
        output = number_cnt.index(2) + 200
        return output
    #9 그 외
    else:
        max_num = 0

        for cnt, i in enumerate(number_cnt):
            if i != 0:
                max_num = max(max_num,cnt)
        output = max_num + 100
        return output

#getting ready for game
for _ in range(5):
    color,num = map(str, input().split())
    num = int(num)
    cards.append((color, num))

    
    color_cnt[color]+=1
    number_cnt[num]+=1
cards = sorted(cards, key=lambda x: x[1])
output = card_game()
print(output)


    
    

