"""
개요 : CSV 파일 입출력
page : 245 ~ 249
"""
import csv
'''
1. CSV ?
CSV = Comma Separated Values 약자
-> 쉼표로 분리한 값들
-> 데이터 베이스나 스프레드시트 데이터를 저장하기 위해서 사용하는 형식.
-> 엑셀 같은 스프레드시트에서는 쉼표가 아닌 각 데이터가 분리되어있는 것 처럼 보임.
( 메모장으로 CSV 파일을 열어보면 ',' 쉼표로 데이터가 구분되어있는 게 보임. )
'''

'''
2. csv 모듈로 CSV 파일 생성하기
csv 모듈을 이용해보자.

사용법
1. csv 파일을 w모드로 열기
2. 열린 file을 csv.writer() 메소드 인수에 전달
3. writerow 메소드를 이용해 값을 전달.
4. newline 옵션을 이용해서 불필요한 라인 제거.
'''
# file = open('차량관리.csv', 'w', newline='')
# with open('차량관리.csv', 'w', newline='') as file:
#     csv_maker = csv.writer(file, delimiter=',', quotechar='"')
#     csv_maker.writerow([1, '08러1234', '2020-10-20,14:00'])
#     csv_maker.writerow([2, '25다1234', '2020-10-20,14:10'])
#     csv_maker.writerow([3, '28하1234', '2020-10-20,14:20'])
# print('차량관리.csv 파일이 생성되었습니다.')

'''
3. CSV 파일 읽기 ( 기본 방법 )
-> 한 줄에 한 데이터가 있기 때문에 readline() 메소드로 한 줄씩 읽습니다.
-> 쉼표(,)로 분리하기 위해서 split() 메소드를 이용합니다.
'''

car_list = []
with open('차량관리.csv', 'rt') as file:
    while True:
        line = file.readline()
        if not line:
            break
        # print(line)
        car = line.split(',')
        car_list.append(car)
print(car_list)

'''
4. csv 모듈로 CSV 파일 읽기

사용법 
1. csv 파일을 'r' 모드로 읽기
2. 읽은 파일을 csv.reader() 메소드에 전달
3. csv.reader()에서 반환된 iterator을 for 문으로 처리
'''

with open('차량관리.csv', 'r', newline='') as file:
    csv_reader = csv.reader(file, delimiter=",", quotechar='"')
    for line in csv_reader:
        print(line)










