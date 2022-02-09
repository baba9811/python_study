"""
파일명 : day11-08-class_quiz
개요 : 응용문제
page : 270 ~ 271
"""

'''
1. 지시사항에 따라 책 제목과 저자 정보를 저장할 수 있는 Book 클래스를 만드세요.

[ 지시사항 ]
- 책 제목과 책 저자 정보를 출력하는 print_info() 메소드 구현
- 다음과 같은 방법으로 book1, book2 인스턴스 생성
    # book1, book2 인스턴스 생성
    book1 = Book()
    book2 = Book()
    
    # book1, book2 제목과 저자 정보 저장
    book1.set_info('파이썬', '민경태')
    book2.set_info('어린왕자', '생텍쥐페리')
- 생성된 인스턴스 book1, book2를 리스트 book_list에 저장
- print_info() 메소드를 이용해 값 표현

[ 출력 ]
책 제목 : 파이썬
책 저자 : 민경태
책 제목 : 어린왕자
책 저자 : 생텍쥐페리
'''

class Book:

    def print_info(self):
        print(f'책 제목 : {self.title}')
        print(f'책 저자 : {self.writer}')

    def set_info(self, title, writer):
        self.title = title
        self.writer = writer

book1 = Book()
book2 = Book()

book1.set_info('파이썬', '민경태')
book2.set_info('어린왕자', '생텍쥐페리')

book_list = [book1, book2]

for book in book_list:
    book.print_info()

'''
2. 지시사항에 따라 시, 분, 초로 구성된 Watch 클래스를 생성하세요.

[ 지시사항 ] 
- 사용자로부터 'HH:mm:ss' 형식의 시간을 입력받아서 이를 Watch 클래스의
hour, minute, second 인스턴스 변수에 저장하세요
- add_hour() 메소드를 이용해서 지정된 시간이 지난 시간을 계산하세요.
- add_minute() 메소드를 이용해서 지정된 분이 지난 시간을 계산하세요.
- add_second() 메소드를 이용해서 지정된 초가 지난 시간을 계산하세요.
-- hour는 0~23, minute은 0~59, second는 0~59, 사이의 값만 가질 수 있습니다.

[ 출력 ]
시간을 입력하세요 >> 12:00:00
계산할 시간을 입력하세요 >> 3
계산할 분을 입력하세요 >> 90
계산할 초를 입력하세요 >> 3690
계산된 시간은 17시 31분 30초입니다.
'''

class Watch:

    def set_time(self, input_time):
        times = input_time.split(':')
        self.hour = int(times[0])
        self.minute = int(times[1])
        self.second = int(times[2])

    def add_hour(self, hour):
        self.hour += hour
        self.hour %= 24

    def add_minute(self, minute):
        self.minute += minute
        self.add_hour(self.minute//60)
        self.minute %= 60

    def add_second(self, second):
        self.second += second
        self.add_minute(self.second//60)
        self.second %= 60

    def print_time(self):
        print(f'계산된 시간은 {self.hour}시 {self.minute}분 {self.second}초입니다.')


watch = Watch()
times = input('시간을 입력하세요 >>>')
watch.set_time(times)
add_hour = input('계산할 시간을 입력하세요 >>>')
watch.add_hour(int(add_hour))
add_minute = input('계산할 분을 입력하세요 >>>')
watch.add_minute(int(add_minute))
add_second = input('계산할 초를 입력하세요 >>>')
watch.add_second(int(add_second))
watch.print_time()







