"""
파일 : day13-04-array
개요 : 배열
"""

'''
1. 배열 ( Array )
- 서로 연관된 변수 값을 묶어서 저장할 수 있는 것
- 메모리의 효율적인 관리와 관련

* 메모리의 효율 ????
-> 시간을 거슬러 올라가서 C언어가 주력으로 사용되던 시점으로 돌아가야함.
- 각가의 변수 값이 메모리의 임의 구역에 저장되며, 해당 구역은 변수명으로 이름이 지정됨.
문제점
- 값이 서로 연관성이 있는 값인 경우 변수 값을 호출하기 위해 메모리에서 찾는 과정에서
시간이 소요.
ex) 학생의 3과목 시험 점수 

그렇다면! 배열은 어떻게 처리가 되었는가???
- Array 영역만큼 메모리를 잡고 순서대로 값을 저장
- Array의 주소는 첫 원소가 들어있는 값의 주소값을 가지게됩니다.
- 이에 메모리는 첫 원소 주소로 이동 후 한칸씩 옆으로 이동하면서 호출하면 끝!

** Python에서의 배열 동작은 다르다.
- Array의 영역만큼 메모리 영역 생성 X
    -> 변수는 그대로 각각 메모리를 잡음.
- Array안에 들어가있는 변수의 주소값을 각각 가지고있는것.
----------------------------------------------------
[ 다른 프로그래밍 언어 ]
배열 : 같은 자료형을 가진 값들을 저장하는 자료형

[ Python ]
List => 서로 다른 자료형을 저장할 수 있는 자료형 
Tuple => List와 같음 
-> 메모리에 자료를 저장하는 형태는 다르지만, 배열과 유사하게
연관된 값을 나열하는 모습을 가지기 때문에, 배열의 일종으로 취급.
-> 순차적으로 나열하여 자료를 저장하기에 배열은 선형 자료구조의 한 종류로 봄. 
'''
















