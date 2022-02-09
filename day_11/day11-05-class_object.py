"""
파일명 : day11-05-class_object
개요 : 클래스 도입의 필요성
page : 258 ~ 259
"""

def student_info(name, department, professor, phone, address, grade):
    print(name)
    print(department)
    print(professor)
    print(phone)
    print(address)
    print(grade)

# 임의로 학생을 한 명 추가해보자.
name1 = 'emily'
department1 = 'computer engineering'
professor1 = 'james'
phone1 = '010-1234-5678'
address1 = 'seoul'
grade1 = 'A'

student_info(name1, department1, professor1, phone1, address1, grade1)

# 한명의 학생을 더 추가해보자.

name2 = 'alice'
department2 = 'chemical engineering'
professor2 = 'david'
phone2 = '010-4321-1414'
address2 = 'busan'
grade2 = 'B'

student_info(name2, department2, professor2, phone2, address2, grade2)

# 한명의 학생을 추가하는데도 6개의 변수를 만들어주어야하며 변수 이름을 정리해서
# 관리하는게 쉽지않음.

# 이런 상황을 클래스와 객체를 이용하면 다음과 같이 해결된다.
# 동작 X
# student1 = Student('emily', 'computer engineering', 'james', '010-1234-5678',
#                    'seoul', 'A')
# student2 = Student('alice', 'chemical engineering', 'david', '010-4321-1414',
#                    'busan', 'B')
#
# student_info(student1)
# student_info(student2)

# 여기서 student1, student2는 변수가 아닌 객체라고 합니다.










