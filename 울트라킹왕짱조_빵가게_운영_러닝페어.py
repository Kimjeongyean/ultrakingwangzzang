print('나는 지금 5천만원의 빚이 있다.')
print('나의 목표는 6개월 동안 빵가게를 운영하면서 빚을 갚고 이윤을 최대한 남기는 것이다.')
print('하지만 6개월 안에 빚을 탕감하지 못한다면 나는 파산을 할 것이다...')
print('열심히 장사해보자!')
      
print('\n가게에 들어가기 위해 도어락 네 자리의 비밀번호를 맞춰야 합니다.\n')

#비밀번호 설정
import random
def genSecret(secretLen):
    secretList = random.sample(range(10), secretLen)
    secret = ''
    for i in range(secretLen):
        secret = secret + str(secretList[i])
    return secret

def getGuess(secretLen, chance):
    while True:
        print('%2d 번의 기회가 남았습니다.' % chance, end='')
        guess = input(' 비밀번호를 입력하세요: ')
        if len(guess) == secretLen and guess.isdigit():
            return guess

def getClues(secretLen, secret, guess):
    strike = 0
    ball = 0
    for i in range(secretLen):
        if secret[i] == guess[i]:
            strike += 1
        elif secret[i] in guess:
            ball += 1
    return strike, ball

def printResult(secretLen, strike, ball):
    if strike == secretLen:
        print('문이 열립니다.\n')
        return True

    if strike > 0:
        print('%d strike(s) and %d ball(s)\n' % (strike, ball))
    elif strike > 0:
        print('%d strike(s)\n' % strike)
    elif ball > 0:
        print('%d ball(s)\n' % ball)
    else:
        print('Out\n')
    return False



# 판매할 빵 선택
#식빵 = (원가: 1000원, 판매가: 3000원)
#크림빵 = (원가: 500원, 판매가: 2000원)
#피자빵 = (원가: 1200원, 판매가: 3500원)
#단팥빵 = (원가: 400원, 판매가: 1800원)
#소세지빵 = (원가: 700원, 판매가: 2500원)
def sell(month1):
    while True:
        print( month1 +'번째 달에 판매할 빵의 종류를 고르세요. \n빵은 식빵, 크림빵, 피자빵, 단팥빵, 소세지빵이 있습니다.')
        global bread
        bread = input('이달의 빵: ')
        if bread == '식빵' :
            break
        elif bread =='크림빵':
            break
        elif bread =='피자빵':
            break
        elif bread =='단팥빵':
            break
        elif bread =='소세지빵':
            break
        else:
            print('해당되는 빵이 없습니다. 빵을 다시 선택하세요.')
            continue
        
    while True:
        print('\n' + month1 +'번째 달에 판매한 빵의 개수를 정하세요. \n단, 판매개수의 범위는 8000개 이상 13000개 이하입니다.')
        global num
        num = int(input('이번 달 빵 판매량: '))
        if num < 8000 or num > 13000 :
            print('범위 내의 수를 다시 입력하세요.')
            continue
        else :
            break
    
#리스트
iwanttobeblackword = []


# 정산 함수
def calculation(month):
    print('\n' + month + '번째 달 장사 후 정산시간입니다!')
    print('임대료= 10000000원 \n인건비= 1000000원 \n광고비= 150000원')
    
    if bread == '식빵':
        p = int(1000)*num
        
    elif bread == '크림빵':
        p = int(500)*num
        
    elif bread == '피자빵':
        p = int(1200)*num
        
    elif bread == '단팥빵':
        p = int(400)*num
        
    elif bread == '소세지빵':
        p = int(700)*num
            
    print('재료비= '+ str(p) + '원')

    import random
    r= str(random.randrange(350000, 500000, 10000))
    print('공과금= '+ r + '원')
    
    sum= int(10000000) + int(1000000) + int(150000) + int(p) + int(r)
    print('지출비: ' + str(sum) + '원')

    if bread == '식빵':
        q = int(3000)*num
        
    elif bread == '크림빵':
        q = int(2000)*num
        
    elif bread == '피자빵':
        q = int(3500)*num
        
    elif bread == '단팥빵':
        q = int(1800)*num
        
    elif bread == '소세지빵':
        q = int(2500)*num

    print('판매실적= '+ str(q) + '원')

    theif()

    sale = q - sum - m

    print('\n이번 달 최종 수익은 '+ str(sale) + '원 입니다.')

    iwanttobeblackword.append(sale)

    if sale>0 :
        print('따라서 이번 달은 흑자입니다.\n')
            
    elif sale<0 :
        print('따라서 이번 달은 적자입니다.\n')

    elif sale==0 :
        print('따라서 이번 달은 이득도 손해도 없습니다.\n')

    return sum

#도둑(매 달 확률->30%, 랜덤->100~300)
def theif():
    import random
    t = random.randint(1,10)
    global m
    m = int(random.randrange(1000000, 3000000, 100000))
    if t % 3 == 0:
        print('※ 도둑이 들어 ' + str(m) + '원이 털렸습니다.')    
    else:
        m = 0
        
        
    

#시작
secLen = 4
sec = genSecret(secLen)
for chance in range(10, 0, -1):
    gue = getGuess(secLen, chance)
    s,b = getClues(secLen, sec, gue)
    result = printResult(secLen, s, b)
    if result == True:

        #첫째 달
        sell('첫')
        calculation('첫')
        
        print('\n')    
        
        #둘째 달
        sell('두')
        calculation('두')
        
        print('\n')
        
        #셋째 달
        sell('세')
        calculation('세')
        
        print('\n')
        
        #넷째 달
        sell('네')
        calculation('네')
        
        print('\n')
        
        #다섯째 달
        sell('다섯')
        calculation('다섯')
        
        print('\n')

        #여섯째 달
        sell('여섯')
        calculation('여섯')
        
        print('\n')

        total = int(sum(iwanttobeblackword))

        print('지난 여섯 달 동안의 수익은 '+ str(total) + '원 입니다.')

        if total >= 50000000 :
            print('빚을 다 갚았습니다.\n')

        else :
            print('빚을 다 갚지 못하여 파산하였습니다.\n')
        break

else:
    print('침입자로 판단되어 비상벨이 울립니다.\n')        
