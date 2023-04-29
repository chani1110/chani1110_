import os
import random
import time
import sys

a = [['a', 'ア'],['i', 'イ'],['u', 'ウ'],['e', 'エ'],['o', 'オ']]
ka = [['ka', 'カ'],['ki', 'キ'],['ku', 'ク'],['ke', 'ケ'],['ko', 'コ']]
sa = [['sa', 'サ'],['shi', 'シ'],['su', 'ス'],['se', 'セ'],['so', 'ソ']]
ta = [['ta', 'タ'],['chi', 'チ'],['tsu', 'ツ'],['te', 'テ'],['to', 'ト']]
na = [['na', 'ナ'],['ni', 'ニ'],['nu', 'ヌ'],['ne', 'ネ'],['no', 'ノ']]
ha = [['ha', 'ハ'],['hi', 'ヒ'],['fu', 'フ'],['he', 'ヘ'],['ho', 'ホ']]
ma = [['ma', 'マ'],['mi', 'ミ'],['mu', 'ム'],['me', 'メ'],['mo', 'モ']]
ya = [['ya', 'ヤ'],['yu', 'ユ'],['yo', 'ヨ']]
ra = [['ra', 'ラ'],['ri', 'リ'],['ru', 'ル'],['re', 'レ'],['ro', 'ロ']]
wa = [['wa', 'ワ'],['wo', 'ヲ']]
n = [['n', 'ン']]
contain = ['a', 'ka', 'sa', 'ta', 'na', 'ha', 'ma', 'ya', 'ra', 'wa', 'n', 'end', 'all', 'c all', 'c a', 'c ka', 'c sa', 'c ta', 'c na', 'c ha', 'c ma', 'c ya', 'c ra', 'c wa', 'c n']
question_c = []
question_c1 = []
question = []
question_1 = []
ch = ('a', 'ka', 'sa', 'ta', 'na', 'ha', 'ma', 'ya', 'ra', 'wa', 'n')
li = (a, ka, sa, ta, na, ha, ma, ya, ra, wa, n)

print("추가할 행 입력, ex) '\033[91ma\033[0m'(あ행), '\033[91mka\033[0m'(か행), '\033[91mna\033[0m'(な행), '\033[91mall\033[0m'(전체 추가),'\033[91mend\033[0m'(입력 끝), etc")
print("취소 시 앞에 '\033[91mc\033[0m '붙이기")
j = ""
    
while j != "end":
    j = input()
    if j in contain:
        if j == "all":
            for i in ('a', 'ka', 'sa', 'ta', 'na', 'ha', 'ma', 'ya', 'ra', 'wa', 'n'):
                question_c.append(i)
            question = a + ka + sa + ta + na + ha + ma + ya + ra + wa + n
        elif j == "c all":
            question_1.clear()
            question.clear()
            question_c.clear()
            question_c1.clear()
        elif j == "c a":
            try:
                question_c.remove("a")
                question_c1.remove("a")
                for l in range(0, 47):
                    if len(question_1[l][0]) == 1 and question_1[l][0] != "n":
                        e=5
                        while e > 0:
                            e -=1
                            question.remove(question[l])
                            question_1.remove(question_1[l])
            except:
                pass
        elif "c" in j:
            try:
                for d in ('ka', 'sa', 'ta', 'na', 'ha', 'ma', 'ra', 'wa'):
                    if d[0] == j[2] and j == "c "+ d:
                        question_c.remove(d)
                        question_c1.remove(d)
                        for q in range(0, 47):
                            if question_1[q][0][0] == d[0]:
                                e=5
                                while e > 0:
                                    e -=1
                                    question.remove(question[q])
                                    question_1.remove(question_1[q])
                if j == "c ya":
                    question_c.remove("ya")
                    question_c1.remove("ya")
                    for l in range(0, 47):
                        if question_1[l][0][0] == "y":
                            e=3
                            while e > 0:
                                e -=1
                                question.remove(question[l])
                                question_1.remove(question_1[l])
                if j == "c n":
                    question_c.remove("n")
                    question_c1.remove("n")
                    for l in range(0, 47):
                        if question_1[l][0][0] == "n" and len(question_1[l][0]) == 1:
                            question.remove(question[l])
                            question_1.remove(question_1[l])
            except:
                pass
        elif j == "end":
            if len(question_1) == 0:
                sys.exit(0)
            else:
                pass
        elif len(j) < 3:
            question_c.append(j)
            for y in range(0, 11):
                if j == ch[y] :question = question + li[y]
        elif len(j)>=3:
            qw = j[2:]
            print(qw)
            question_c.remove(qw)             
            
                
    os.system('cls')
    for v in question:
        if v not in question_1:
            question_1.append(v)
    for q in question_c:
        if q not in question_c1:
            question_c1.append(q)
    print("추가할 행 입력, ex) '\033[91ma\033[0m'(あ행), '\033[91mka\033[0m'(か행), '\033[91mna\033[0m'(な행), '\033[91mall\033[0m'(전체),'\033[91mcancel\033[0m'(취소),'\033[91mend\033[0m'(입력 끝), etc")
    print("취소 시 앞에 '\033[91mc\033[0m '붙이기")
    print(question_c1)
# 문제 시작-------------------------------------------------------------------------------------------------------------------------------------------
os.system('cls')
for i in range(2, 0, -1):
    print(str(i)+"초 후 시작..")
    print("'end' 입력하면 끝")
    time.sleep(1)
    os.system('cls')
an = 0
example = []
score = 0
qn = -1

class EnJp():
    def quesJP():
        global score
        example = []
        try:
            for i in range(0, 50):
                example.append(question_1[i][1])
        except:
            pass
        random.shuffle(example)
        print("보기)", end="")
        for i in range(0, len(example)):
            print('\033[91m',example[i],'\033[0m' ,end="")
        an = input("\n답 : ")
        if an == qu[1]:
            os.system("cls")
            print("\033[33m정답\033[0m")
            score += 1   
        else:
            os.system("cls")
            print("\033[33m오답\033[0m 정답:",qu[1]) 
    def quesEn():
        global score
        an = input("답 :")
        if an == qu[0]:
            os.system("cls")
            print("\033[33m정답\033[0m")
            score += 1
        else:
            os.system('cls')
            print("\033[33m오답\033[0m 정답:",qu[0])
    
while an != "end":
    os.system('cls')
    qu = random.choice(question_1)
    quci = random.randrange(1, 2)
    qn +=1
    print('Q.\033[91m',qu[quci],'\033[0m,              점수/문제:', score,'/',qn)
    if quci == 0:
        EnJp.quesJP()
    else:
        EnJp.quesEn()
    time.sleep(1)

print("END 최종 점수/문제수",score,'/',qn)