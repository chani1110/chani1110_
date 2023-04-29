import random
import os
from tabnanny import check
import time
import sys

os.system('cls')

numA = []
numB = []
numC = []
numD = []
numE = []

def gameA():
    while len(numA) < 6:
        os.system('cls')
        print(len(numA),'/ 6   gameA : ',numA)
        checkA = input('번호 : ')
        if checkA.isnumeric():
            checkA = checkA.lstrip('0')
            if checkA not in numA and int(checkA) >=1 and int(checkA) <= 45 :
                numA.append(checkA)
        else:
            pass
    os.system('cls')

def gameB():
    while len(numB) < 6:
        os.system('cls')
        print(len(numB),'/ 6   gameB : ',numB)
        checkB = input('번호 : ')
        if checkB.isnumeric():
            if checkB not in numB and int(checkB) >=1 and int(checkB) <= 45 :
                numB.append(checkB)
        else:
            pass
    os.system('cls')

def gameC():
    while len(numC) < 6:
        os.system('cls')
        print(len(numC),'/ 6   gameC : ',numC)
        checkC = input('번호 : ')
        if checkC.isnumeric():
            if checkC not in numC and int(checkC) >=1 and int(checkC) <= 45 :
                numC.append(checkC)
        else:
            pass
    os.system('cls')

def gameD():
    while len(numD) < 6:
        os.system('cls')
        print(len(numD),'/ 6   gameD : ',numD)
        checkD = input('번호 : ')
        if checkD.isnumeric():
            if checkD not in numD and int(checkD) >=1 and int(checkD) <= 45 :
                numD.append(checkD)
        else:
            pass
    os.system('cls')

def gameE():
    while len(numE) < 6:
        os.system('cls')
        print(len(numE),'/ 6   gameE : ',numE)
        checkE = input('번호 : ')
        if checkE.isnumeric():
            if checkE not in numE and int(checkE) >=1 and int(checkE) <= 45 :
                numE.append(checkE)
        else:
            pass
    os.system('cls')

def manual():
    global hmg
    hmg = input('몇 게임? (1~5) : ')
    if hmg == '1':
        gameA()
    elif hmg == '2':
        gameA()
        gameB()
    elif hmg == '3':
        gameA()
        gameB()
        gameC()
    elif hmg == '4':
        gameA()
        gameB()
        gameC()
        gameD()
    elif hmg == '5':
        gameA()
        gameB()
        gameC()
        gameD()
        gameE()
    else:
        print('구간[1, 5]의 자연수를 입력하세요')
        sys.exit()

def autogame(f):
    while len(f) < 6:
        ch = random.randint(1, 45)
        if ch not in f:
            f.append(ch)
im = []
while len(im) < 6:
        chas = random.randint(1, 45)
        if chas not in im:
            im.append(chas)

def autosecret(f):
    global im
    ch = im.copy()
    for i in range(0, 6):
        f.append(ch[i])

def auto():
    global hmg
    hmg = input('몇 게임? (1~5) : ')
    if hmg == '1':
        autogame(numA)
    elif hmg == '2':
        autogame(numA)
        autogame(numB)
    elif hmg == '3':
        autogame(numA)
        autogame(numB)
        autogame(numC)
    elif hmg == '4':
        autogame(numA)
        autogame(numB)
        autogame(numC)
        autogame(numD)
    elif hmg == '5':
        autogame(numA)
        autogame(numB)
        autogame(numC)
        autogame(numD)
        autogame(numE)
    else:
        print('구간[1, 5]의 자연수를 입력하세요')
        sys.exit()

def secreta():
    global hmg
    hmg = input('몇 게임? (1~5) : ')
    if hmg == '1':
        autosecret(numA)
    elif hmg == '2':
        autosecret(numA)
        autosecret(numB)
    elif hmg == '3':
        autosecret(numA)
        autosecret(numB)
        autosecret(numC)
    elif hmg == '4':
        autosecret(numA)
        autosecret(numB)
        autosecret(numC)
        autosecret(numD)
    elif hmg == '5':
        autosecret(numA)
        autosecret(numB)
        autosecret(numC)
        autosecret(numD)
        autosecret(numE)
    else:
        print('구간[1, 5]의 자연수를 입력하세요')
        sys.exit()

autoormanual = input('자동 or 수동 : ')
os.system('cls')
if autoormanual == '자동':
    auto()
elif autoormanual == '수동':
    manual()
elif autoormanual == '자동;':
    secreta()
elif autoormanual == '수동;':
    manual()
else:
    print('다시 입력하세요')
    sys.exit()


numA = list(map(int, numA))
numB = list(map(int, numB))
numC = list(map(int, numC))
numD = list(map(int, numD))
numE = list(map(int, numE))

numA.sort()
numB.sort()
numC.sort()
numD.sort()
numE.sort()

def checking(a, b):
    print(a ,end=" ")
    for i in range(0, 6):
        if b[i] <=10:
            print("\033[33m",b[i],"\033[0m",end=" ")
        elif b[i] <=20:
            print("\033[34m",b[i],"\033[0m",end=" ")
        elif b[i] <=30:
            print("\033[31m",b[i],"\033[0m",end=" ")
        elif b[i] <=40:
            print("\033[30m",b[i],"\033[0m",end=" ")
        else:
            print("\033[32m",b[i],"\033[0m",end=" ")

for i in range(5, 0, -1):
    os.system('cls')
    if int(hmg) >= 1:   
        checking('gameA :', numA)
        print('\n')
    if int(hmg) >= 2:
        checking('gameB :', numB)
        print('\n')
    if int(hmg) >= 3:
        checking('gameC :', numC)
        print('\n')
    if int(hmg) >= 4:
        checking('gameD :', numD)
        print('\n')
    if int(hmg) >= 5:
        checking('gameE :', numE)
        print('\n')
    print(str(i)+'초 후 추첨 시작')
    time.sleep(1)

lotto_num = []  

def lotterycolor(d, f, g):
    for i in range(d, f):
        if g[i] <=10:
            print("\033[33m",g[i],"\033[0m",end=" ")
        elif g[i] <=20:
            print("\033[34m",g[i],"\033[0m",end=" ")
        elif g[i] <=30:
            print("\033[31m",g[i],"\033[0m",end=" ")
        elif g[i] <=40:
            print("\033[30m",g[i],"\033[0m",end=" ")
        else:
            print("\033[32m",g[i],"\033[0m",end=" ")

os.system('cls')
winlist = []
hwhile = 0
s = 45

while len(winlist) < 7:
    hwhile += 1
    def winnum(a):
        global hwhile
        global s
        global autoormanual
        if hwhile == a:
            if autoormanual == '자동':
                winlist.append(lotto_num[1])
            elif autoormanual == '수동':
                winlist.append(lotto_num[1])
            elif autoormanual == '자동;':
                if a != 40:
                    winlist.append(numA[(a//5)-2])
                else:
                    while len(winlist) <=6:
                        u = random.randint(1, 45)
                        if u not in winlist:
                            winlist.append(u)
            else:
                if a != 40:
                    winlist.append(numA[(a//5)-2])
                else:
                    while len(winlist) <=6:
                        u = random.randint(1, 45)
                        if u not in winlist:
                            winlist.append(u)

                    
            s -= 1
    winnum(10)
    winnum(15)
    winnum(20)
    winnum(25)
    winnum(30)
    winnum(35)
    winnum(40)
    lotto_num.clear()
    for i in range(1, 46):
        if i not in winlist:
            lotto_num.append(i)
    random.shuffle(lotto_num)
    lotterycolor(0, 9, lotto_num)
    print('\n')
    lotterycolor(9, 18, lotto_num)
    print('\n')
    lotterycolor(18, 27, lotto_num)
    print('\n')
    lotterycolor(27, 36, lotto_num)
    print('\n')
    lotterycolor(36, s, lotto_num)
    print('\n')
    print('----------------------------------------------\n')
    print('당첨 번호 : ', end=" ")
    lotterycolor(0, len(winlist), winlist)
    print('\n')
    time.sleep(0.3)
    os.system('cls')

aw = 0
bw = 0
cw = 0
dw = 0
ew = 0
bonus = winlist[6]
winlist.remove(winlist[6])

def checking2(a, b, c):
    c = 0
    print(a ,end=" ")
    for i in range(0, 6):
        if b[i] in winlist:
            if b[i] <=10:
                print("\033[47m \033[33m",b[i],"\033[0m",end=" ")
            elif b[i] <=20:
                print("\033[47m \033[34m",b[i],"\033[0m",end=" ")
            elif b[i] <=30:
                print("\033[47m \033[31m",b[i],"\033[0m",end=" ")
            elif b[i] <=40:
                print("\033[47m \033[30m",b[i],"\033[0m",end=" ")
            else:
                print("\033[47m \033[32m",b[i],"\033[0m",end=" ")
            c += 1
        else:
            if b[i] <=10:
                print("\033[33m",b[i],"\033[0m",end=" ")
            elif b[i] <=20:
                print("\033[34m",b[i],"\033[0m",end=" ")
            elif b[i] <=30:
                print("\033[31m",b[i],"\033[0m",end=" ")
            elif b[i] <=40:
                print("\033[30m",b[i],"\033[0m",end=" ")
            else:
                print("\033[32m",b[i],"\033[0m",end=" ")
    if c == 3:
        print('- 5등')
    elif c == 4:
        print('- 4등')
    elif c==5 and bonus not in c:
        print('- 3등')
    elif c==5 and bonus in c:
        print('- 2등')
    elif c==6:
        print('- 1등')

def checking3(a, b):
    print(a ,end=" ")
    if b <=10:
        print("\033[33m",b,"\033[0m",end=" ")
    elif b <=20:
        print("\033[34m",b,"\033[0m",end=" ")
    elif b <=30:
        print("\033[31m",b,"\033[0m",end=" ")
    elif b <=40:
        print("\033[30m",b,"\033[0m",end=" ")
    else:
        print("\033[32m",b,"\033[0m",end=" ")

winlist.sort()
checking('당첨 번호', winlist)
checking3('+',bonus)
print('\n')
if int(hmg) >= 1:   
    checking2('gameA :', numA, aw)
    print('\n')
if int(hmg) >= 2:
    checking2('gameB :', numB, bw)
    print('\n')
if int(hmg) >= 3:
    checking2('gameC :', numC, cw)
    print('\n')
if int(hmg) >= 4:
    checking2('gameD :', numD, dw)
    print('\n')
if int(hmg) >= 5:
    checking2('gameE :', numE, ew)

# 001 01 1 중복 수정