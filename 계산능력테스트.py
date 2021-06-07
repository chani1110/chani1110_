import random
import math
import time
import os
from threading import Timer 

heart = 3 #목숨
time1 = 5 
score = 0 #점수
problem_num = 1 # 문제 번호 
correct_answer = 0 #맞은 문제수
problem_time = 7 #제한 시간

os.system('cls')
print("▣"*110)
game = str(input("계산 능력 테스트\na. 게임 시작 b. 게임 방법 및 주의사항\n원하시는 항목의 문자('a'또는 'b')를 입력해주세요:"))  #선택
os.system('cls')
if game=='b':
    print("▣"*110)
    print("2. 게임 방법 및 주의 사항")
    print("➥ 게임을 시작하면 5초 후 문제와 답 입력란이 나옵니다. ")
    print("➥ 문제를 제한 시간 안에 풀고 옳은 답을 입력하고 엔터를 입력합니다.")
    print("➥ 문제를 풀수록 문제당 점수는 늘어나고 제한 시간은 줄어듭니다.. 점수와 제한 시간은 다음과 같이 주어집니다.")
    print("➥ 1~5문제/1점, 7초\n  ~7문제2점, 5초\n  ~10문제3점, 4초\n  ~13문제5점, 3초\n  15문제~/7점, 2초")
    print("➥ 목숨은 총 3번입니다. 틀리거나 제한 시간 안에 풀지 못하면 1목숨이 줄어듭니다.(문제 번호도 오르지 않습니다.)")
    print("➥ 시간 초과가 돼도 문제를 풀면 점수가 주어집니다.(시간 초과에 문제까지 틀리면 목숨이 2가 떨어집니다.")
    print("➥ 문제가 한 자릿수 일 때 십의 자리는 0으로 간주합니다.")
    print("➥ 나눗셈 문제에서는 몫만 입력합니다.(예, 37의 앞자리에서 뒷자리를 나눈 값은? ➔ 0(3÷7=0....3/7))")
    print("➥ 문제가 끝나면 2초 뒤에 다음 화면이 나옵니다.")
    print("▣"*110)
    game = str(input("게임을 시작하기위해 'a'을 눌러주세요: "))
os.system('cls')
if game=='a':  #시작
    while time1>0:
        print(str(time1)+"초 후에 게임이 시작됩니다.")
        time.sleep(1)
        time1 -=1
    os.system('cls')
    while heart>0:
        print("▣"*40)   
        print("목숨 :",heart)
        print("점수 :",score)
        print("▣"*40)
        question_num = int(random.randint(1, 99)) #문제 (랜덤) 숫자

        #질문 준비
        listed= []
        a_count=30
        b_count=10

        if question_num==1 or question_num==4 or question_num==9 or question_num==16 or question_num==25 or question_num==36 or question_num==49 or question_num==64 or question_num==81 or question_num==100:
            while a_count>0:
                a_count-=1
                listed.append('a')
        if question_num**question_num<=1000: 
            while b_count>0:
                b_count-=1
                listed.append('b') 
        if 10<=question_num<100:
            listed.append('d')
            listed.append('e')
            listed.append('h')
        if 0<question_num<100:
            listed.append('f')
            listed.append('g')
        if question_num%10!=0:
            listed.append('i')

        question_num_first = question_num//10
        question_num_last = question_num%10
        question_num_plus = question_num_first + question_num_last
        question_num_minos = question_num_first - question_num_last
        question_num_time = question_num_first * question_num_last
        if question_num%10!=0:
            question_num_div = question_num_first // question_num_last
        random_list = random.choice(listed)
        answer_number = 0

        #질문
        if random_list=='a':
            question = "%d의 제곱근은?" %question_num
            answer_number = math.sqrt(question_num)
        if random_list=='b':
            question = "%d의 제곱은?" %question_num
            answer_number = pow(question_num, 2)
        if random_list=='d':
            question = "%d의 앞자리는?" %question_num
            answer_number = question_num_first                      
        if random_list=='e':
            question = "%d의 뒷자리는?" %question_num
            answer_number = question_num_last
        if random_list=='f':
            question = "%d의 십의 자리수와 일의 자리수를 더한 값은?" %question_num
            answer_number = question_num_plus
        if random_list=='g':
            question = "%d의 십의 자리수에서 일의 자리수를 뺀 값은?" %question_num
            answer_number = question_num_minos
        if random_list=='h':
            question = "%d의 십의 자리수와 일의 자리수를 곱한 값은?" %question_num
            answer_number = question_num_time
        if random_list=='i':
            question = "%d의 십의 자리수에서 일의 자리수를 나눈 값은?" %question_num
            answer_number = question_num_div
        
        #제한 시간
        def timeout():
            print("시간 초과")
            global heart
            heart-=1

        print(str(problem_num)+'.',question)
        k = problem_time
        t = Timer(k, timeout)
        t.start()
        try: 
            answer = int(input('답:')) #답 입력
        except ValueError:
            print("정수를 입력해주세요")
        else:
            os.system('cls')
            print("▣"*40)   
            print("목숨 :",heart)
            print("점수 :",score)
            print("▣"*40) 

            #검사
            if answer == answer_number:
                print("정답입니다.")
                if problem_num <5:
                    problem_time = 7
                    score += 1
                elif problem_num <7:
                    problem_time = 5
                    score += 2  
                elif problem_num <10:
                    problem_time = 4
                    score += 3
                elif problem_num <14:
                    problem_time = 3
                    score += 5
                else:
                    problem_time = 2
                    score += 7
                problem_num +=1
                correct_answer +=1
            else:
                print("오답입니다.")
                heart -=1
        t.cancel()
        print("2초 후 다음 화면이 나옵니다.")
        ready_time = 2
        while ready_time>0:
            time.sleep(1)
            ready_time -=1
        os.system('cls')
#끝
os.system('cls')
print("게임 끝!")
print("▣"*40)
print("최종 점수 :",str(score)+'점')
print("맞힌 문제 :",str(correct_answer)+"문제")
print("▣"*40)

# 2021.5.24 ~ 2021.5.31