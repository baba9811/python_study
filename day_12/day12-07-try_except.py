"""
파일명 : day12-07-try_except
개요 : 예외 처리
page : 294 ~ 305
"""

'''
1. 고전적인 예외 처리
예외는 개발자가 처리할 수 있는 문제

간단한 예시)
'''
# a = int(input('제수를 입력하세요 >>>>'))
# b = int(input('피제수를 입력하세요 >>>>'))
#
# if b == 0:
#     print('0으로 나누는 것은 불가능합니다.')
# else:
#     print(f'{a}/{b} = {a/b}')
'''
[ 고전적인 예외처리에 대한 문제 ]
- 어떤 문제가 발생할지 예상할 수 있어야 대비를 할 수 있음.
- 어떤 문제가 발생할지 예상은 하더라도 대비를 할 수 없는 경우가 있음.

* 어떤 문제가 발생할 수 있는지 모두 예상하면 좋겠지만, 현실은 그렇지 않음
-> 여러 사람이 같이 하는 프로젝트일 수록 문제를 예상하는 것은 현실적으로 어렵습니다.

* 발생 가능한 문제를 예상하더라도 대비가 힘들때가 있음.
-> input으로 받은 값을 int로 변환하는 과정에서 실수, 문자로 입력하면 
    에러가 발생한다는 사실을 인지는 하지만 처리가 힘듬.
'''

'''
2. 예외의 종류
파이썬은 발생할 수 있는 모든 문제를 예외 클래스로 만들어둠.
-> 프로그램이 실행되면서 어떤 문제가 발생하면 자동으로 해당 문제의 예외 인스턴스가
발생합니다.

p 295 표 참고
* 외울 필요 X 
-> 실무 뛰면 다양한 예외를 경험하고 그로 인해 자연스럽게 알게됨.
'''

'''
3. 예외 처리 방식

3.1) 모든 예외를 처리하는 방식
다음과 같은 구조를 이용해서 모든 예외를 처리합니다.

[ 기본 구조 ]
try:
    코드 작성 영역
except:
    예외 발생 시 처리 영역

* 들여쓰기 주의 !!
'''
# try:
#     a = int(input('제수를 입력하세요 >>>'))
#     b = int(input('피제수를 입력하세요 >>>'))
#     print(f'{a}/{b} = {a/b}')
# except:
#     print('예외가 발생했습니다.')

# 책 예제 ) 다음은 사용자가 입력한 키를 정수로 반올림해서 다시 저장하는 프로그램입니다.
# 일부러 예외가 발생하도록 구현되었으며 어디에서 예외가 발생하는지 찾아보세요.

# try:
#     height = input('키를 입력하세요 >>>')
#     # height = float(height)
#     height = round(height)
#     print(f'입력하신 키는 {height}cm로 처리됩니다.')
# except:
#     print('예외가 발생했습니다.')

'''
3.2) 특정 예외만 처리하는 방식
try except문을 사용하면 기본적으로 예외의 종류에 상관없이
모든 예외가 처리됩니다.
이번에는 좀 더 친절한 예외 처리를 위해서 다음과 같은 예외 메시지를 출력하려고합니다.

- 0으로 나누는 경우 => 0으로 나눌 수 없습니다.
- 정수가 아닌 값을 입력한 경우 => 정수만 입력할 수 있습니다.

* 이런 경우에는 except문 뒤에 처리하고자 하는 예외를 모두 명시하면 됨.
'''
# try:
#     a = int(input('제수를 입력하세요 >>>>'))
#     b = int(input('피제수를 입력하세요 >>>>'))
#     print(f'{a}/{b} = {a/b}')
# except ZeroDivisionError:
#     print('0으로 나눌 수 없습니다.')
# except ValueError:
#     print('정수만 입력할 수 있습니다.')
# except Exception:
#     print('알 수 없는 예외가 발생했습니다.')

'''
3.3) 예외 메시지 처리하기
지금까지는 모든 예외 메시지를 직접 만들어서 사용
-> 기본적으로 예외 메시지를 이미 가지고있기에 
    해당 예외 메시지를 이용해볼것.

* 예외 메시지는 직접 만들어서 처리하는게 좋음.

[ 사용법 ]
try:
    코드 작성 영역
except 예외 as 예외 메시지:
    예외 발생 시 처리 영역
'''

# 예시
# 0 ~ 4까지만 인덱스를 사용할 수 있는데 10을 사용해서 에러 발생!!!!
a = [10, 20, 30, 40, 50]

try:
    a[10]
except IndexError as e:
    print(e)

'''
3.4) else문과 finally 문
try except 문에 추가로 else문과 finally문을 사용할 수 있습니다.
else문 == 예외가 발생하지 않을 때 처리되는 구문
finally문 == 예외 발생과 상관없이 항상 처리되는 구문

[ 기본 구조 ]
try:
    코드 작성 영역
except:
    예외 발생 시 처리 영역
else:
    예외가 없을 떄 처리 영역
finally:
    언제나 실행되는 영역
'''
# try:
#     a = int(input('제수를 입력하세요 >>>>'))
#     b = int(input('피제수를 입력하세요 >>>>'))
#     result = a/b
# except ZeroDivisionError:
#     print('0으로 나눌 수 없습니다.')
# except ValueError:
#     print('정수만 입력할 수 있습니다.')
# else:
#     print(f'{a}/{b} = {result}')
# finally:
#     print('프로그램을 종료합니다.')

'''
책 예제 ) 사용자가 입력한 파일을 읽어서 화면에 그대로 출력하는 프로그램이다.
사용자가 입력한 파일이 존재하지 않는다면 예외 처리를 통해서 파일이 존재하지 않습니다.
메시지를 출력하세요.
'''
# try:
#     filename = input('파일명을 입력하세요 >>>>')
#     file = open(filename, 'rt')
# except FileNotFoundError:
#     print(f'{filename} 파일이 존재하지 않습니다.')
# else:
#     buffer = file.read()
#     print(buffer, end='')
#     print()
#     file.close()
# finally:
#     print('프로그램을 종료합니다.')

'''
4. 강제로 예외 발생시키기
파이썬은 예외로 인식하지는 못하지만 실제로는 예외인 경우가 있습니다.
예시 ) 나이를 정수로 입력받는 프로그램을 만들었다.
50과 같은 정수를 입력하면 예외 발생 X
-1000을 입력해도 예외 발생 X

[ 강제 예외 발생 사용법 ]
raise 예외 클래스()
or 
raise 예외 클래스(예외 메시지)

* 예외 메시지를 생략할 수 잇지만, 생략하지 말고 작성해주는게 좋습니다.
'''
# try:
#     raise Exception('강제로 발생시킨 예외')
# except Exception as e:
#     print('발생한 예외 메시지는 다음과 같습니다.')
#     print(e)

# 실제 코드에선 if 문을 이용해서 예외 발생 조건문을 작성 한 뒤
# raise문을 작성하는 것이 일반적입니다.

try:
    age = int(input('나이를 입력해주세요 >>>'))
    if age < 0:
        raise Exception('나이는 0이상이여야합니다.')
    print(age)
except Exception as e:
    print(e)










