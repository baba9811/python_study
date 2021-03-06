"""
파일명 : day10-02-file_open
개요 : 파일 열기 와 입력
page : 226 ~ 229
"""

'''
1. 파일 열기
- 파일 열기 != 열어본다 
-> 입출력 작업을 진행할 파일을 지정하는 것.

** 파일 입력과 파일 출력 모두 반드시!!!!!! 
    파일 열기 작업을 먼저 수행해야합니다.
    
파일 열기는 기본적으로 open() 함수를 이용합니다.
open() 함수의 기본 형식은 다음과 같습니다.

[ 형식 ]
파일 객체 = open(파일명, 모드)
'''

'''
1-1. 파일명
파일명은 입출력 작업을 수행할 파일을 의미함.
파일명만 작성할 수 있고, 경로를 함께 작성할 수 있습니다.
'''

# 같은 경로에 있는 파일 열기
# open('test.txt')

# 전체 경로로 파일 열기 [ 절대 경로 ]
# open('C:/pythonStud/WS/day10/test.txt')

# 현재 디렉토리(.)를 기준으로 경로를 결정 [ 상대 경로 ]
# open('./test.txt')

# 상위 디렉터리(..)를 기준으로 경로를 결정 [ 상대 경로 ]
# open('../test2.txt')

'''
2-2. 모드
모드란 파일을 여는 목적이라고 볼 수 있습니다.
파일 입력을 위해서인지 파일 출력을 위해서인지는 모드를 통해서 결정함.

------
책 227p -> 2) 모드 표 확인

- 입력
    ㄴ r : 읽기
- 출력
    ㄴ w : 쓰기
    ㄴ a : 추가
    ㄴ x : 배타적 추가 

* 입출력 모드를 생략하면 기본적으로 r 모드로 파일이 열림.
* 출력을 목적으로 한다면 반드시 해당 모드를 명시해야함.
------

파일을 여는 목적을 결정했다면 어떤 파일인지 파일의 종류도 구분해야함.
일반적으로 열려고 하는 파일이 텍스트 파일인가 아닌가? 요걸로 결정

[ 파일 종류 ]
- t : 텍스트 파일
- b : 바이너리 파일 ( 텍스트 파일 외의 모든 파일 )

* 열고자 하는 파일의 종류를 생략하면 기본적으로 t모드(텍스트 모드)로 파일이 열림.
* 바이너리 파일인 경우에는 반드시 b모드 명시

[ t ]
텍스트 모드는 문자를 대상으로 입출력을 처리하기 때문에,
영문이나 한글 등으로 작성된 텍스트 파일에서 사용함.

******************************** 
텍스트는 영문, 한글, 인코딩 방식등에 따라서 한 글자의 크기(바이트)가 달라짐.
-> 별도의 텍스트 모드를 통해서 처리하는 것이 좋음.

[ b ]
바이너리 모드는 모든 파일의 데이터를 1바이트 기본 단위로
입출력을 처리하기 때문에 텍스트를 사용하지 않는 모든 파일(이미지, 사운드, 동영상 등)
사용하는 모드
'''

'''
2. 파일 닫기
파일을 더 이상 사용하지 않거나 프로그램을 종료하고자 할때 열어 놓은 파일은 꼭!!!!!!!!!!
닫아주는게 좋습니다. 

close() 메소드를 이용해 열린 파일 객체를 닫을 수 있습니다.

[ 기본 형식 ]
파일 객체.close()
'''

'''
3. 파일의 생성
day10 디렉터리에 myFile.txt를 생성해보자.
'''

# file = open('myFile.txt', 'wt')
# print('myFile.txt 파일이 생성되었습니다.')
# file.close()

'''
4. with 문
파일을 사용하는 프로그램은 언제든지 예기치 않는 문제가 발생할 수 있습니다.
생성에 문제가 발생하거나, 파일을 여는데 문제가 생길 수 있습니다.
이러한 이유로 try-except(예외처리) 함께하면 좋지만.
예외처리가 아니더라도 python에서는 close() 메소드를 자동으로 호출 할 수 있는
with이 존재합니다.

- with문을 활용하면 with문이 끝날때 항상 close() 메소드를 자동으로 호출함.
** 에러로 인해서 close() 메소드가 호출되지 않는 불상사를 방지할 수 있다.

[ 기본 문법 ]
with open(파일명, 모드) as 파일 객체:
    파일 처리 코드 
'''

# file = open('myFile.txt', 'wt')
# print('myFile.txt 파일이 생성되었습니다.')
# file.close()

with open('myFile.txt', 'wt') as file:
    print('myFile.txt 파일이 생성되었습니다.')




