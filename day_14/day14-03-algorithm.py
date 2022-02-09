"""
개요 : 정렬, 검색 알고리즘
"""

'''
1. 정렬 알고리즘
- 섞여 있는 데이터를 순서대로 나열하는것
-> 시간 복잡도에 따라 성능이 좌우되며 성능이 좋을수록 구현 방법이 어려워짐 
'''

'''
2. 대표적인 정렬의 종류
O(n2)의 시간 복잡도 ( 정렬할 자료의 수가 늘어나면 제곱에 비례해서 증가 )
- 버블 정렬
- 선택 정렬
- 삽입 정렬

O(n log n)의 시간 복잡도 ( n개 * (2로 n을 만들려면 필요한 제곱 수 ))
ex ) 32 개를 정렬 => 32 * 5(2*2*2*2*2=32)
- 병합 정렬
- 퀵 정렬
'''

'''
2.1 버블 정렬
- 인접한 두 수를 비교하며 정렬해나가는 방법으로 느린 성능을 가지고있음.
- 앞에서 시작 -> 큰 수를 뒤로 보내 뒤가 가장 큰 값을 가지게 함
'''

array = [8, 4, 6, 2, 9, 1, 3, 7, 5]


def bubble_sort(array):
    n = len(array)
    for i in range(n - 1):
        for j in range((n - i) - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
            print(array)


print("before: ", array)
bubble_sort(array)
print("after:", array)

'''
2.2 선택 정렬
- 한 바퀴 돌 때 가장 작은 값을 찾아 맨 앞과 교환하는 방식의 정렬
- 최악의 성능
'''

array = [8, 4, 6, 2, 9, 1, 3, 7, 5]


def selection_sort(array):
    n = len(array)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if array[j] < array[min_index]:
                min_index = j
        array[i], array[min_index] = array[min_index], array[i]
        print(array[:i + 1])


print("before: ", array)
selection_sort(array)
print("after:", array)

'''
2.3 삽입 정렬
- 정렬된 데이터 그룹을 늘려가며 추가되는 데이터는 알맞은 자리에 삽입하는 방식
'''

array = [8, 4, 6, 2, 9, 1, 3, 7, 5]


def insertion_sort(array):
    n = len(array)
    for i in range(0, n):
        for j in range(i, 0, - 1):
            if array[j - 1] > array[j]:
                array[j - 1], array[j] = array[j], array[j - 1]
        print(array[:i + 1])


print("before: ", array)
insertion_sort(array)
print("after:", array)

'''
2.4 병합 정렬
- 괜찮은 성능을 가진 정렬
- 분할 해서 값을 읽고 정렬해줌
'''
array = [8, 4, 6, 2, 9, 1, 3, 7, 5]


def merge_sort(array):
    if len(array) < 2:
        return array
    mid = len(array) // 2
    low_arr = merge_sort(array[:mid])
    high_arr = merge_sort(array[mid:])

    merged_arr = []
    l = h = 0
    while l < len(low_arr) and h < len(high_arr):
        if low_arr[l] < high_arr[h]:
            merged_arr.append(low_arr[l])
            l += 1
        else:
            merged_arr.append(high_arr[h])
            h += 1
    merged_arr += low_arr[l:]
    merged_arr += high_arr[h:]
    print(merged_arr)
    return merged_arr


print("before: ", array)
array = merge_sort(array)
print("after:", array)

'''
2.5 퀵 정렬
- 분할 정복 알고리즘으로 평균적으로 빠른 속도를 수행
- 추가적인 메모리 공간이 필요없다는 장점 존재
- 많은 언어의 정렬 내장 함수로 사용
- pivot이라고 불리는 임의의 기준값을 사용
'''
array = [8, 4, 6, 2, 5, 1, 3, 7, 9]


def quick_sort(array):
    if len(array) <= 1:
        return array
    # 정 중앙값을 pivot으로 지정
    pivot = len(array) // 2
    front_arr, pivot_arr, back_arr = [], [], []
    for value in array:
        # pivot으로 지정된 애보다 작으면 다 왼쪽으로
        if value < array[pivot]:
            front_arr.append(value)
        # pivot보다 크면 다 오른쪽으로
        elif value > array[pivot]:
            back_arr.append(value)
        # pivoit 값 저장
        else:
            pivot_arr.append(value)
    print(front_arr, pivot_arr, back_arr)
    fa = quick_sort(front_arr)
    pa = quick_sort(pivot_arr)
    ba = quick_sort(back_arr)
    return fa + pa + ba


print("before: ", array)
array = quick_sort(array)
print("after:", array)

'''
3. 검색 알고리즘
- 검색은 특정한 요소를 찾는 과정
'''

'''
4. 검색 알고리즘의 종류
- 선형 탐색 알고리즘 : 처음부터 끝까지 순차적으로 탐색하는 방법
- 이진 탐색 알고리즘 : 중간지점을 정해서 반씩 제외해서 찾는 방법
'''

def linear_search(list, ele):
    for i in range(len(list)):
        if list[i] == ele:
            return i
    return -1

print(linear_search(["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "N", "O", "P"], "G"))

'''
4.2 이진 탐색 알고리즘
https://www.daleseo.com/search-binary/
'''
def binary_search(arr, target, low=None, high=None):
    low, high = low or 0, high or len(arr) - 1
    if low > high:
        return -1
    mid = (low + high) // 2
    if arr[mid] > target:
        return binary_search(arr, target, low, mid)
    if arr[mid] == target:
        return mid
    if arr[mid] < target:
        return binary_search(arr, target, mid + 1, high)

print(binary_search(["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "N", "O", "P"], "G"))