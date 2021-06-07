"""
실행을 하고 주민번호 앞자리를 입력한 뒤 뒷자리를 입력한다. 
이때 뒷자리는 표시되지 않는다. 
모두 입력하면 주민번호에서 알 수 있는 정보(출생날짜, 성별, 내/외국인, 출생지역, 출생신고 순서 그리고 오류인증번호)를 보여준다. 
"""

import datetime as dt
import getpass
year = dt.datetime.today().year
yn = 0
print("------------------------------")

print("(1900년 이전 또는 2020년 10월 1일 이후 출생자는 해당 안됨)")
rrn1 = str(input("주민등록번호의 앞자리를 입력하세요 :"))
rrn2 = str(getpass.getpass("주민등록번호의 뒷자리를 입력하세요 :"))

yn19 = "19"+rrn1[0]+rrn1[1]
yn20 = "20"+rrn1[0]+rrn1[1]
m = int(rrn1[2:4])
d = int(rrn1[4:6])
lf = 0
gender = 0
area = 0
order = 0
check = 0
order = str(rrn2[5])
check = (int(rrn1[0])*2+int(rrn1[1])*3+int(rrn1[2])*4+int(rrn1[3])*5+int(rrn1[4])*6+int(rrn1[5])*7+int(rrn2[0])*8+int(rrn2[1])*9+int(rrn2[2])*2+int(rrn2[3])*3+int(rrn2[4])*4+int(rrn2[5])*5)%11

if check==0 or check==1:
    check+=10
else:
    check+=0
if not len(rrn1)==6 or not len(rrn2)==7:  
    print("잘못된 주민등록번호입니다.")
elif int(rrn1)>=201001 and (int(rrn2[0])==3 or int(rrn2[0])==4 or int(rrn2[0])==7 or int(rrn2[0])==8):  
    print("잘못된 주민등록번호입니다.")
elif ((int(rrn2[0])==3 or int(rrn2[0])==4 or int(rrn2[0])==7 or int(rrn2[0])==8) and year-int(yn20)<=0) or m>=13 or d>=32:
    print("잘못된 주민등록번호입니다.")
elif int(rrn2[0])==9 or int(rrn2[0])==0:
    print("잘못된 주민등록번호입니다.")
elif check + int(rrn2[6])!=11:
    print("잘못된 주민등록번호입니다.")
else:
    if rrn2[0]=='1' or rrn2[0]=='2' or rrn2[0]=='5' or rrn2[0]=='6':
        yn = yn19
    elif rrn2[0]=='3' or rrn2[0]=='4' or rrn2[0]=='7' or rrn2[0]=='8':
        yn = yn20
    else:
        ''
    if rrn2[0]=='1' or rrn2[0]=='2' or rrn2[0]=='3' or rrn2[0]=='4':
        lf = '내국인'
    elif rrn2[0]=='5' or rrn2[0]=='6' or rrn2[0]=='7' or rrn2[0]=='8':
        lf = '외국인'
    else:
        ''
    if rrn2[0]=='1' or rrn2[0]=='3' or rrn2[0]=='5' or rrn2[0]=='7':
        gender = '남자'
    elif rrn2[0]=='2' or rrn2[0]=='4' or rrn2[0]=='6' or rrn2[0]=='8':
        gender = '여자'
    else:
        ''
    for seoul in range(1, 9):
        if int(rrn2[2])==seoul and int(rrn2[1])==0:
            area = '서울특별시'
    for busan in range(9, 13):
        if (int(rrn2[2])==busan and int (rrn2[1])==0) or int(rrn2[1:3])==busan:
            area = '부산광역시'
    for incheon in range(13, 16):
        if int(rrn2[1:3])==incheon:
            area = '인천광역시'
    for GG in range(16, 26):
        if int(rrn2[1:3])==GG:
            area = '경기도'
    for GW in range(26, 35):
        if int(rrn2[1:3])==GW:
            area = '강원도'
    for CHb in range(35, 39):
        if int(rrn2[1:3])==CHb:
            area = '충청북도'
    for CHn in range(42, 44) or (45, 48):
        if int(rrn2[1:3])==CHn:
            area = '충청남도'
    for sejong in [44, 96]:
        if int(rrn2[1:3])==sejong:
            area = '세종특별자치시'
    for Jb in range(48, 54):
        if int(rrn2[1:3])==Jb:
            area = '전라북도'
    for Jn in range(55, 65):
        if int(rrn2[1:3])==Jn:
            area = '전라남도'
    for gwangju in [55, 56, 65, 66]:      
            if int(rrn2[1:3])==gwangju:
                area = '광주광역시'
    for daegu in range(67, 71):
        if int(rrn2[1:3])==daegu:
            area = '대구광역시'
    for GSb in range(71, 82):
        if int(rrn2[1:3])==GSb:
            area = '경상북도' 
    for GSn in range(82, 85) or (86, 92):
        if int(rrn2[1:3])==GSn:
            area = '경상남도'
    for ulsan in [85, 90]:
        if int(rrn2[1:3])==ulsan:
            area = '울산광역시'
    for jeju in range(92, 96):
        if int(rrn2[1:3])==jeju:
            area = '제주특별자치시도'

    print("------------------------------")
    print(str(yn)+'년',str(m)+'월',str(d)+'일생')
    print('성별 :',gender)
    print(lf)
    print('출생지역 :',area)
    print("출생신고순서 :",order+"번째")
    print("오류인증번호 : 확인")  
    print("------------------------------")