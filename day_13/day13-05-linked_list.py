"""
파일 : day13-05-linked_list
개요 : 링크드 리스트
"""

'''
1. 링크드 리스트 ( Linked List )
데이터와 다음 노드의 주소를 담고있는 노드들이 한 줄로 연결되어있는 방식의 자료구조.
- data, next로 구성되어있고 이 data, next를 포함하고있는 것을 node라고 함.

[ 장점 ]
- List의 길이를 동적으로 조절 가능
- 데이터의 삽입과 삭제가 쉬움

* Python에서의 배열이 아닌 다른 언어에서는 배열 선언 시 초기에 메모리 공간을 잡아두고 
변경이 불가하지만, LinkedList는 그런 걸 생각할 필요가 없음.

[ 단점 ]
- 임의의 노드에 바로 접근할 수가 없음
- 다음 노드의 위치를 저장하기 위한 추가 공간이 필요
- 거꾸로 탐색이 어려움

[ 사용 이유 ]
C언어에서 해당
#include <stdio.h>

int main()
{
    # 정수형 배열을 만들껀데 10개의 요소가 들어가있는 배열을 만들꺼야.
    int numArr[10] = {11, 22, 33, 44, 55, 66, 77, 88, 99, 110};
    
    reutrn 0;
}

[ C언어에서 배열 선언시 에러 발생 상황 ] 
int numArr[0]; # 컴파일 에러. 크기가 0인 배열은 선언할 수 없음  
int numArr[];  # 컴파일 에러. 요소를 선언하지 않고는 크기를 생략할 수 없음

{ 요소가 있을때는 생략이 가능 }
int numArr[] = {11, 22, 33, 44};
'''
numArr = [11, 22, 33, 44, 55, 66, 77, 88, 99, 110, 111]

# Node 생성
class Node:
    def __init__(self, data):
        """
        data = 현재 노드가 가지고있는 값
        next = 현재 노드의 다음 노드를 가리키는 값
        """
        self.data = data
        self.next = None

# LinkedList 클래스 생성
class LinkedList:

    def __init__(self, data):
        # node 시작점
        self.head = Node(data)

    '''
    2. 추가    
    '''
    def add(self, data):
        if not self.head:
            # 노드가 없을때 만들어주기!
            self.head = Node(data)
        else:
            # 첫번째까지 포함한 노드들
            node = self.head
            # 마지막 노드까지 탐색 후 마지막 노드에 새로운 노드를 만들어주며 연결
            while node.next:
                node = node.next
            node.next = Node(data)

    '''
    3. 조회
    '''
    def display(self):
        # 첫번째 노드 가져옴
        node = self.head
        display_nodes = []
        while node:
            # 현재 node의 data값을 display_nodes에 넣어주기
            display_nodes.append(node.data)
            node = node.next
        print(' > '.join(display_nodes))

    '''
    4. 삭제 
    - 다음 상황 고려해야합니다.
        ㄴ LinkedList가 모두 비어있을 경우
        ㄴ LinkedList의 첫번째 Node가 비워야 할 값인 경우
        ㄴ LinkedList의 제일 끝 아니면 도중에 Node가 있어 지울경우
        ㄴ 끝까지 다 찾아봐도 지워야할 데이터가 없는 경우
    '''
    def delete(self, data):
        # 현재 노드 가져오기 ( 첫번째 )
        node = self.head
        # 노드에 값이 있을 때 
        if node is not None:
            # 첫번째 노드의 값이 전달받은 인수와 같으면 현재 노드 삭제
            if node.data == data:
                # 현재 노드 값을 임시로 temp에 담자.
                temp = self.head
                # 현재 노드 다음 값을 현재 노드로 변경
                self.head = node.next
                # 이전에 저장된 값은 삭제
                del temp
                return
        # 첫번째 노드의 값이 인수로 전달받은 노드가 아닌 경우 반복문
        while node is not None:
            # 만약 현재 노드 값과 인수의 값이 같으면
            if node.data == data:
                # 이전에 읽은 노드의 다음 바라보는 노드를 현재 노드의 다음으로 연결
                # - 현재 노드를 바라보게 하는게 아님
                prev.next = node.next
                # 반복문 종료
                break
            # 이전에 읽은 노드 값
            prev = node
            # 다음 노드 값
            node = node.next
        if not node:
            return

    '''
    5. 사이즈 출력
    '''
    def size(self):
        node = self.head
        count = 0
        while node:
            count += 1
            node = node.next
        return count

    '''
    6. 탐색 메소드
    '''
    def search(self, data):
        node = self.head
        for i in range(self.size()):
            if node.data == data:
                print(f'{data} The data is at the {i + 1} index.')
                return
            node = node.next
        print(f'{data} Does not exist in Linked List')
        return

linked = LinkedList('1')

linked.add('2')
linked.add('3')
linked.add('4')
linked.add('5')
linked.display()

linked.delete('6')
linked.display()

linked.search('1')
print(linked.size())



























