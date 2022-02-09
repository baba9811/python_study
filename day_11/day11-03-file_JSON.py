"""
파일 : day11-03-file_JSON
개요 : JSON 파일 입출력
page : 250 ~ 253
"""
import json
'''
1. JSON ???
- JSON == JavaScript Object Notaion == JavaScript의 객체 표현 방법
- key - value == 키-값으로 이루어진 데이터 구조 

** JSON이 중요한 이유는 네트워크로 주고받는 데이터의 표준 형식으로 자리 잡았기 때문이다.
'''

'''
2. JSON 데이터의 형식
JSON 데이터는 속성-값 쌍으로 구성된 데이터들이 순서 없이 모여 있는 구조로 되어있다.
구조는 다음과 같다.
- 중괄호({})로 전체 JSON 데이터를 묶어줌.
- 속성과 값 사이에 콜론(:)을 붙여줍니다.
- 속성과 값으로 구성된 각 데이터의 구분은 쉼표(,) 사용
dict = {
    {
        "name": "alice",
        "age": 20
    }
}
'''

types = {
    'str': 'String',
    'int': 'Integer',
    'JSON': 'JavaScript Object Notation'
}
# dict 타입과 같은 모습을 하고있습니다.

'''
3. JSON 파일 생성
- Python은 JSON 데이터 처리를 위해서 json 모듈을 사용
* json 모듈
    - 리스트, 딕셔너리 같은 파이썬 객체를 JSON 데이터로 변환 가능
    - JSON 데이터를 파이썬 객체로 변환 가능

* 파이썬 객체를 JSON 데이터로 변환하는 것을 JSON 인코딩이라고 합니다.

인코딩을 처리하는 메소드는 json.dumps() 입니다.
'''

dict_list = [
    {
        'name': 'james',
        'age': 20,
        'spec': [
            175.5,
            70.5
        ]
    },
    {
        'name': 'alice',
        'age': 21,
        'spec': [
            168.5,
            60.5
        ]
    }
]

# json_string = json.dumps(dict_list)
#
# with open('dictList.json', 'w') as file:
#     file.write(json_string)
#
# print('dictList.json 파일이 생성되었습니다.')

'''
파일의 크기를 줄이기 위해서 의도적으로 불필요한 공백 문자가 제거가 된 상태로 만들어짐.
사람이 직접 읽기가 어렵기 때문에 json.dumps() 메소드에 indent 옵션을 추가해서
JSON 데이터에 들여쓰기와 줄 바꿈이 추가되면서 보기 좋은 형식으로 만들어지는 것도 확인할
수 있습니다.
'''
# indent=4 == 공백문자 4개로 처리한다.
# 네트워크 전송이 처리 목적이라면 사용하지 않는 편이 좋습니다.
json_string = json.dumps(dict_list, indent=4)

with open('dictList.json', 'w') as file:
    file.write(json_string)

print('dictList.json 파일이 생성되었습니다.')

'''
4. JSON 파일 읽기
JSON 데이터를 Python 객체로 변환하는 것을 JSON 디코딩이라고 합니다.

디코딩을 처리하는 메소드는 json.loads() 입니다.
'''

with open('dictList.json', 'r') as file:
    json_reader = file.read()
    dict_list = json.loads(json_reader)

for dic in dict_list:
    print(f"이름 {dic['name']}")
    print(f"나이 {dic['age']}")
    print(f"키 {dic['spec'][0]}")
    print(f"몸무게 {dic['spec'][1]}")



























