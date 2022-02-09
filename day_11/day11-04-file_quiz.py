"""
파일 : day11-04-file_quiz
개요 : 응용문제
page : 254 ~ 255
"""

'''
1. 다음 지시사항에 따라 텍스트 파일을 복사하는 프로그램을 구현하세요.

[ 지시사항 ]
- Python에서 2021.01.01.txt 파일을 만드세요.
- 확장자가 txt가 아닌 파일을 복사하려고 하면 '복사할 수 없는 파일입니다' 라는 
    에러 메시지를 출력하세요
- 복사본 파일의 이름은 원본 파일명 앞에 '복사본-'을 추가하세요.
- 텍스트 파일의 인코딩은 기본 인코딩(cp949)으로 가정하고 별도로 지정하지 마세요.

[ 출력 ]
복사할 파일명을 입력하세요 >> 2021.01.01.jpg
복사할 수 없는 파일입니다.
복사할 파일명을 입력하세요 >> 2021.01.01.txt
복사본-2021.01.01.txt 파일이 생성되었습니다.
'''

# with open('2021.01.01.txt', 'wt') as file:
#     file.write('a')
#
# while True:
#     copy_file_name = input('복사할 파일명을 입력하세요 >>> ')
#     if copy_file_name.find('.txt') > 0:
#         with open(copy_file_name, 'rt') as file:
#             with open(f'복사본-{copy_file_name}', 'w') as copy_file:
#                 while True:
#                     line = file.readline()
#                     if line == '':
#                         break
#                     copy_file.write(line)
#                 print(f'복사본-{copy_file_name} 파일이 생성되었습니다.')
#                 break
#     else:
#         print('복사할 수 없는 파일입니다.')

'''
2. 다음 지시사항에 따라 세종특별자치시에 설치된 CCTV의 개수를 구하는 프로그램을 구현하세요.

[ 지시사항 ]
- csv 모듈사용
- isdecimal() 메소드 사용
- 공공데이터포털 -> cctv 검색 -> 세종특별자치시_CCTV 다운로드
- 모든 라인에 존재하는 카메라 대수를 합한 결과를 출력합니다.
    ( 5번째 데이터가 카메라 대수 )
    
[ 출력 ]
세종특별자치시에 설치된 CCTV는 총 2561대 입니다.
'''
import csv
# total = 0
# with open('세종특별자치시_CCTV_20210101.csv', 'r', newline='') as file:
#     csv_reader = csv.reader(file, delimiter=',', quotechar='"')
#     for line in csv_reader:
#         print(line)
#         if line[4].isdecimal():
#             total += int(line[4])
# print(f'세종특별자치시에 설치된 CCTV는 총 {total}대 입니다.')

'''
3. 다음 지시사항에 따라 세종특별자치시에 설치된 전체 CCTV의 설치 목적을 종류별로
모두 파악하는 프로그램을 구현하세요.

[ 지시 사항 ]
- 세종특별자치시_CCTV.csv 파일을 이용해 JSON 파일을 만들어보자.
- 설치 목적을 나열해보자 ( 중복 데이터 X )

[ 출력 ]
{'다목적'}
'''
import json
lists = []
with open('세종특별자치시_CCTV_20210101.csv', 'r', newline='') as file:
    csv_reader = csv.reader(file, delimiter=',', quotechar='"')
    for index, line in enumerate(csv_reader):
        if index > 0:
            line_val = {}
            line_val['관리기관명'] = line[0]
            line_val['소재지도로명주소'] = line[1]
            line_val['소재지지번주소'] = line[2]
            line_val['설치목적구분'] = line[3]
            line_val['카메라대수'] = line[4]
            line_val['카메라화소수'] = line[5]
            line_val['촬영방면정보'] = line[6]
            line_val['보관일수'] = line[7]
            line_val['관리기관전화번호'] = line[8]
            line_val['위도'] = line[9]
            line_val['경도'] = line[10]
            line_val['데이터기준일자'] = line[11]
            lists.append(line_val)

json_string = json.dumps(lists)
# json_string = json.dumps(lists, ensure_ascii=False)

# with open('cctv_json.json', 'w', encoding='utf-8') as file:
with open('cctv_json.json', 'w') as file:
    file.write(json_string)

# ---------------------------------------------

use_set = set()
# with open('cctv_json.json', 'r', encoding='utf-8') as file:
with open('cctv_json.json', 'r') as file:
    json_reader = file.read()
    dict_list = json.loads(json_reader)
    
for dic in dict_list:
    use_set.add(dic['설치목적구분'])

print(use_set)









