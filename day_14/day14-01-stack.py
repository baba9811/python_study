"""
개요 : 스택
"""

'''
1. 스택??
[ Stack모양.JPG 참고 ] 
- 데이터의 삽입과 삭제가 데이터의 가장 한쪽 끝에서만 일어나는 자료구조
- 가장 마지막에 삽입된 데이터가 가장 먼저 사용되거나 삭제 =  LIFO ( Last-In-First-Out )

일상속 스택은 프링글스로 예를 들 수 있습니다.
-> 프링글스는 과자를 뺼 수 있는 입구가 한개이며 이 한개로 감자칩을 꺼내 먹습니다.
-> 제일 먼저 넣어진 감자칩이 제일 마지막에 먹게됩니다.
'''

'''
2. 스택의 주요 메소드
- 마지막에 데이터를 삽입 [ push ]
- 마지막 데이터를 삭제 [ pop ]
- 마지막 데이터를 삭제하지않고 반환 [ top ]
- 현재 스택이 비어있는지 확인 [ isEmpty ]
'''


# 코드로 구현하기
class Stack:
    def __init__(self):
        # 리스트로 표현
        self.stack = []

    def push(self, data):
        self.stack.append(data)

    def isEmpty(self):
        is_empty = False
        if len(self.stack) == 0:
            is_empty = True
        return is_empty

    def pop(self):
        if self.isEmpty():
            print('Stack is Empty')
        else:
            self.stack.pop()

    def top(self):
        if self.isEmpty():
            print('Stack is Empty')
        else:
            return self.stack[-1]


stack = Stack()

stack.push(10)
stack.push(20)
stack.push(40)
stack.push(60)

print(stack.stack)

stack.pop()
stack.pop()

print(stack.stack)
print(stack.top())

print(stack.isEmpty())

stack.pop()
stack.pop()
stack.pop()
print(stack.isEmpty())








