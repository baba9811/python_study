"""
개요 : 큐
"""

'''
1. 큐??
[ Queue 모양.JPG ] 
큐는 양쪽이 뚫려있는 기다란 통에서 한쪽은 데이터를 삽입하고 한쪽은 데이터를 삭제하는 자료구조입니다.
스택이 후입선출 ( LIFO - Last In, First Out ) 구조였다면
큐는 먼저 들어간 데이터가 먼저 나오는 선입선출 ( FIFO - Fist In, Last Out ) 구조입니다.
'''

'''
2. 큐의 주요 메소드
- 맨 뒤로 데이터를 삽입 : enqueue
- 맨 앞의 데이터를 빼기 : dequeue
- 맨 앞의 데이터를 빼지않고 조회 : peek
- 현재 큐에 데이터가 있는지 확인 : isEmpty
'''

class Queue:

    def __init__(self):
        self.queue = []

    def isEmpty(self):
        if len(self.queue) == 0:
            return True
        else:
            return False

    def enqueue(self, data):
        self.queue.append(data)

    def dequeue(self):
        if self.isEmpty():
            print('Queue Is Empty')
        else:
            self.queue.pop(0)

    def peek(self):
        if self.isEmpty():
            print('Queue is Empty')
        else:
            return self.queue[0]


queue = Queue()

queue.enqueue(1)
queue.enqueue(3)
queue.enqueue(6)

print(queue.queue)
print(queue.peek())

queue.dequeue()
queue.dequeue()

print(queue.queue)

queue.dequeue()

print(queue.isEmpty())

