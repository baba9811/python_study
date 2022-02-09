import sys
"""
파일명 : day16-04-addressBook2
개요 : 주소록 프로젝트의 구현
page : 353 ~ 364
"""

'''
1. addressBook.csv 파일
addressBook.csv 파일은 주소록에 저장된 모든 데이터를 저장하는 파일
일반 변수에 데이터를 저장하면 프로그램이 종료될 때 데이터도 함께 사라지기 때문에,
데이터베이스나 파일을 이용해서 데이터를 저장해 두어야 하는데
이번 프로젝트에서는 addressBook.csv 파일이 데이터 베이스 대신 사용됨.
'''

'''
2. 클래스 Person
각 개인의 정보를 저장할 클래스
다음과 같이 구현되어있습니다.
[ 인스턴스 변수 ]
- 이름
- 전화번호
- 주소

[ 메소드 ]
- 생성자 : 인스턴스 변수 초기화
- info : 저장된 정보를 출력할 수 있는 메소드
'''

class Person:

    def __init__(self, name, phone, addr):
        """
        이름, 전화번호, 주소를 입력받으면 인스턴스 변수에
        해당 정보를 저장하는 생성자
        """
        self.name = name
        self.phone = phone
        self.addr = addr

    def info(self):
        """
        인스턴스 변수에 저장된 name, phone, addr을 보여주는 함수
        """
        print(f'{self.name}, {self.phone}, {self.addr}')

'''
3. 클래스 AddressBook
주소록 프로젝트의 모든 기능을 가지고있으며
Peson 클래스의 객체(인스턴스)를 여러 개 저장할 수 있도록 
address_list 리스트를 가지고 있음.
다음과 같은 기능들이 구현되어있습니다.
[ 인스턴스 변수 ]
- address_list = Person 클래스의 객체를 여러개 저장

[ 메소드 ]
- 생성자
- file_reader : addressBook.csv 파일 읽기
- file_generator : addressBook.csv 파일 생성
- menu : 수행 메뉴 소개 및 입력
- exit : 프로그램 종료
- run : 프로그램 실행
- insert : 추가
- delete : 삭제
- update : 수정
- search : 검색
- print_all : 전체 출력

* menu 메소드를 제외한 모든 메소드는 인스턴스 변수인 address_list를 참고
'''

class AddressBook:

    def __init__(self):
        """
        addressBook.csv 파일의 모든 내용을 읽어서 address_list에 저장하는 기능을 가짐
        - address_list생성 후 addressBook.csv 파일을 읽기 위해서 file_reader()
        메소드를 호출
        """
        self.address_list = []
        self.file_reader()

    def file_reader(self):
        """
        addressBook.csv 파일의 정보를 읽어서 address_list에 저장하는 메소드입니다.
        - 모든 정보는 한 줄에 한 명씩만 저장되어있음
        - readline() 메소드를 이용해서 한 줄씩 읽어 들이는 방법을 사용함
        - 읽어 들이는 정보는 쉼표(,)로 분리되어있기 때문에 split(',') 메소드를 이용해서
        이름, 전화번호, 주소를 분리함
        - 주소에는 \n이 포함되어있는데, 이는 줄 바꿈을 의미하는 이스케이프 문자
            -> 불필요하기 때문에 이를 제거할 수 있는 rstrip('\n')메소드를 추가 사용
        - 처음 실행될때는 addressBook.csv 파일이 존재하지 않기 때문에 예외 처리를
        반드시 해줘야함
        """
        try:
            # addressBook.csv 파일이 없으면 예외 발생
            file = open('addressBook.csv', 'rt')
        except:
            # addressBook.csv 파일이 없을때 예외 처리
            print('addressBook.csv 파일이 없습니다.')
        else:
            # 정상 처리 ( addressBook.csv 파일이 존재할 때 )
            while True:
                buffer = file.readline()
                if not buffer:
                    break
                data = buffer.split(',')
                name = data[0]
                phone = data[1]
                addr = data[2].rstrip('\n')
                self.address_list.append(Person(name, phone, addr))
            print('addressBook.csv 파일을 로드 했습니다.')
            file.close()

    def file_generator(self):
        """
        address_list에 저장된 모든 데이터를 이용해서 addressBook.csv 파일을 생성
        하는 메소드
        파일 생성에 오류가 발생하면 프로그램이 예기치 않게 종료될 수 있으므로
        예외 처리 반드시 해야함.
        """
        try:
            file = open('addressBook.csv', 'wt')
        except:
            print('addressBook.csv 파일을 생성할 수 없습니다.')
        else:
            for person in self.address_list:
                file.write(f'{person.name},{person.phone},{person.addr}\n')
            file.close()

    @staticmethod
    def menu():
        """
        유일한 address_list를 참고하지 않는 정적 메소드입니다.
        어떤 동작을 수행할 것인지 사용자로부터 입력받아서 그 값을 반환하기만 합니다.
        """
        print('-' * 30)
        print('신규 주소록 등록은 1번')
        print('기존 주소록 삭제는 2번')
        print('기존 주소록 수정은 3번')
        print('주소록 검색은 4번')
        print('전체 주소록 출력은 5번')
        print('-' * 30)

        choice = int(input('수행할 작업을 숫자로 입력하세요 >>>'))
        return choice

    def exit(self):
        """
        주소록 프로그램을 종료하는 메소드
        sys 모듈의 exit() 메소드를 호출합니다.
        -> import sys 해야함
        """
        print('프로그램을 종료합니다.')
        sys.exit()

    def run(self):
        """
        사용자로부터 어떤 작업을 수행할 것인지 입력받은 뒤
        입력받은 해당 메소드를 호출하는 역할
        """
        while True:
            choice = AddressBook.menu()
            if choice == 0:
                self.exit()
            elif choice == 1:
                self.insert()
            elif choice == 2:
                self.delete()
            elif choice == 3:
                self.update()
            elif choice == 4:
                self.search()
            elif choice == 5:
                self.print_all()
            else:
                print('없는 명령입니다. 확인 후 다시 입력해주세요')

    def insert(self):
        """
        사용자로부터 새로 등록할 이름, 전화번호, 주소를 입력받고
        이를 이용해서 Person 객체 생성 후 이 Person 객체를 address_list에 저장
        이후 곧바로 file_generator() 메소드를 호출해서 변경된 address_list의 내용으로
        다시 addressBook.csv 파일을 새로 생성
        ( 곧바로 반영을 하지 않으면 예기치 못한 상황에서 입력된 데이터가 사라질 가능성이
        있음 )
        """
        print('=== 새로운 주소록 생성 ===')
        name = input('등록할 이름 입력 >>> ')
        phone = input('등록할 전화번호 입력 >>> ')
        addr = input('등록할 주소 입력 >>>')
        # 모두 입력 완료시
        if name and phone and addr:
            self.address_list.append(Person(name, phone, addr))
            self.file_generator()
            print('신규 주소록이 정상적으로 생성되었습니다.')
        else:
            # 누락된 입력이 하나라도 있으면 삽입 실패
            print('입력값이 부족하여 주소록이 생성되지 않았습니다. ')

    def delete(self):
        """
        사용자로부터 삭제하고자 하는 이름을 입력받아서 이를 address_list에서
        찾아 제거합니다.
        동일한 이름이 2개 이상 저장되어 있는 경우를 대비해서 삭제 전에
        확인 과정을 거치고 삭제합니다.
        삭제하려는 전화번호가 맞는지 확인하는 과정이 포함되어있습니다.
        ( 삭제도 추가와 동일하게 삭제하면 바로 file_generator() 메소드를 실행 )
        """
        print('=== 기존 주소록 삭제 ===')
        name = input('삭제할 이름 입력 >>> ')
        if not name:
            print('입력된 이름이 없어 삭제를 취소합니다.')
            return
        deleted = False
        for i, person in enumerate(self.address_list):
            if name == self.address_list[i].name:
                print(f'검색된 전화번호가 "{self.address_list[i].phone}"입니다.')
                if input('삭제할까요?(Y/N) >>> ').upper() != 'Y':
                    # for문으로 되돌아감
                    continue
                self.address_list.pop(i) # 삭제
                deleted = True
                print(f'{name}의 정보를 삭제했습니다.')
                self.file_generator()
                break
        if not deleted:
            print(f'{name}의 정보가 삭제되지 않았습니다.')


    def update(self):
        """
        update() 메소드는 delete() 메소드와 유사한 흐름으로 진행됩니다.
        사용자에게 사용자 정보를 입력받아서 address_list에서 찾은 뒤 수정합니다.
        * 이름은 수정하지 못합니다.
        * 수정은 전화번호와 주소만 수정할 수 있습니다.
        * 사용자가 수정할 정보를 입력하지 않으면 수정하지 않습니다.
        * 주소록 수정이 끝나면 file_generator() 메소드를 호출
        """
        print('=== 기존 주소록 수정 ===')
        name = input('수정할 이름 입력 >>> ')
        if not name:
            print('입력된 이름이 없어 수정을 취소합니다.')
            return
        updated = False
        for i, person in enumerate(self.address_list):
            if name == self.address_list[i].name:
                print(f'검색된 전화번호가 "{self.address_list[i].phone}"입니다.')
                if input('수정할까요?(Y/N) >>> ').upper() != 'Y':
                    # for문으로 되돌아감
                    continue
                new_phone = input('변경할 전화번호 입력 >>> ')
                # 입력이 있는 경우
                if new_phone:
                    # 입력된 내용으로 변경
                    self.address_list[i].phone = new_phone
                new_addr = input('변경할 주소 입력 >>>')
                if new_addr:
                    self.address_list[i].addr = new_addr
                updated = True
                print('주소록이 수정되었습니다. 수정된 주소록의 내용을 확인하세요.')
                self.address_list[i].info()
                self.file_generator()
                break
            if not updated:
                print(f'{name}의 정보가 수정되지 않았습니다.')

    def print_all(self):
        """
        전체 주소록 정보를 출력하는 메소드입니다.
        """
        print('=== 전체 연락처 출력 ===')
        for person in self.address_list:
            person.info()
        print(f'총 {len(self.address_list)}개의 주소록이 있습니다.')

    def clear(self):
        """
        사용자에게 확인을 받아서 Y를 입력시 
        현재 address_list에 있는 데이터를 모두 삭제 후 
        file_generator 실행

        [ 출력 ]
        정말로 모든 데이터를 삭제하시겠습니까?(Y/N) >>>
        - Y
            -> 모든 데이터가 삭제되었습니다.
            -> 총 {}개의 데이터가 삭제되었고 저장되었습니다.
        - N
            -> 취소되었습니다.
        """
        is_clear = input('정말로 모든 데이터를 삭제하시겠습니까?(Y/N)')
        if is_clear.upper() == 'Y':
            l = len(self.address_list)
            print('모든 데이터가 삭제되었습니다.')
            print(f'총 {l}개의 데이터가 삭제되었고 저장되었습니다.')
            self.address_list.clear()
            self.file_generator()
        else:
            print('취소되었습니다.')

    """
    page.365 응용문제 )
    정보를 검색해서 해당 정보를 출력하는 search() 메소드를 다음 지시사항을 참고하여
    search() 메소드를 구현하세요.
    
    [ 지시사항 ] 
    - class AddressBook의 메소드
    - 이름을 입력받아서 동일한 정보를 찾아서 모두 출력합니다.
    같은 이름이 2명 이상 포함되어있으면 검색된 사람을 모두 출력합니다.
    - 검색된 사람이 없으면 '홍길동의 정보가 없습니다'와 같은 메시지를 출력합니다.
    
    [ 출력 ]
    === 주소록 검색 ===
    찾을 이름을 입력 >>> 김철수
    김철수, 010-2345-5432, 서울시 강남구
    """
    def search(self):
        print('=== 주소록 검색 ===')
        name = input('찾을 이름을 입력 >>> ')
        if not name:
            print('입력된 이름이 없어 조회를 취소합니다.')
            return
        searched = False
        for i, person in enumerate(self.address_list):
            if person.name == name:
                person.info()
                searched = True
        if not searched:
            print(f'{name}의 정보가 없습니다.')

my_app = AddressBook()
my_app.run()


























































