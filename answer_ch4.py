# answer.py

"""
answer.py
자료구조 실습: 5가지 정렬 알고리즘 (Selection, Bubble, Insertion, Quick)

사용 예시:
    python answer.py
    또는
    python main.py
"""

NEED_TO_SOLVE = 'sort'  # 이 부분을 채워 넣으세요

def selection_sort(arr):  # 선택 정렬 함수 정의
    """
    선택 정렬 (Selection Sort)
    - 아이디어: 매 단계 i에서 i..n-1 범위에서 '최소값'의 위치(min_idx)를 찾아 i와 교환
    - 불변식(invariant): 반복문의 단계가 끝날 때마다 arr[0..i]은 오름차순으로 정렬되어 있고,
                        이 구간에는 입력 배열의 가장 작은 i+1개의 원소가 위치한다.
    - 시간복잡도: O(n^2) (최선/평균/최악 모두)
    """
    #selection_sort란?
    #매 i번째 단계(i = 0~n-2,마지막 n-1인덱스는 자동 정렬)에서 
    # i~n-1 인덱스에서 최소값의 위치(min_idx)를 찾아
    # i번째 인덱스 요소와 min_idx위치 요소를 교환하는 알고리즘

    n = len(arr)  # 배열의 길이 n을 저장

    for i in range(n-1):  # 0 ~ n-2까지 반복 (마지막은 자동 정렬됨)
        min_idx = i  # i번째 원소를 현재 최소값으로 가정

        for j in range(i,n):
                # i 이후 구간에서 최소값 탐색
            if arr[j] < arr[min_idx]:   # 더 작은 값 발견 시
                min_idx = j # 최소값 인덱스 갱신

        arr[i],arr[min_idx] = arr[min_idx],arr[i]   # 최소값을 i번째 위치로 교환

    return arr  # 정렬된 배열 반환


def bubble_sort(arr):  # 버블 정렬 함수 정의
    """
    버블 정렬 (Bubble Sort)
    - 아이디어: 이웃한 두 원소(arr[j], arr[j+1])를 비교하여 '큰 값'을 오른쪽으로 보내는 과정을
               맨 끝까지 반복하여, 매 단계마다 '가장 큰 값'이 배열의 끝에 '거품처럼' 올라가도록 함.
    - 최적화: 한 바퀴에서 교환이 한 번도 일어나지 않으면 이미 정렬된 상태 → 조기 종료 가능.
    - 시간복잡도: O(n^2) (최악/평균), 최선은 O(n) (이미 정렬되어 있고 스왑 없음)
    """
    #bubble sort이란
    #i = 0~ n-2까지(n-1일때는 자동 정렬됬음)
    #j = 1~
    #이웃한 두 원소 arr[j]와 arr[j+1]을 비교하여 
    #arr[j]가 arr[j+1]보다 크면 arr[j+1] = arr[j]로 뒤로 보내준다
    #가장 큰 값을 오른쪽으로 보내는 과정을
    #맨끝 j = n-1까지 반복한다
    

    n = len(arr)  # 배열의 길이 n을 저장
    
    for i in range(n-1):# 0 ~ n-2까지 반복
        for j in range(n-1-i):# 맨 끝 i개는 이미 정렬되었으므로 제외
            if arr[j]>arr[j+1]:# 앞이 더 크면
                arr[j+1],arr[j] = arr[j], arr[j+1]# 두 값을 교환
    
    return arr  # 정렬된 배열 반환


def insertion_sort(arr):  # 삽입 정렬 함수 정의
    """
    삽입 정렬 (Insertion Sort)
    - 아이디어: i 번째 원소를 '키(key)'로 두고, 앞쪽 정렬 구간(arr[0..i-1])에서
               key가 들어갈 적절한 위치를 찾을 때까지 원소들을 오른쪽으로 한 칸씩 밀어낸 뒤 삽입.
    - 불변식(invariant): 각 단계 i가 끝나면 arr[0..i] 구간은 항상 정렬되어 있다.
    - 시간복잡도: 최악/평균 O(n^2), 최선 O(n) (이미 거의 정렬된 경우 유리)
    """

    #insertion sort
    #i번째 원소를 키로 두고(i = )
    #앞 쪽 정렬 구간에서 key가 들어갈 적절한 위치를 찾을 때까지 원소들을 오른 쪼긍로 한 칸씩 밀어내
    #그리고 적절한 위치 찾으면 삽입

    n = len(arr)  # 배열의 길이 n을 저장

    for i in range(1, n):  # index 1의 원소부터 차례대로 삽입
        key = arr[i]# 현재 삽입할 값
        j = i -1 # 정렬된 구간의 끝 인덱스

        while j >= 0 and arr[j] > key:# key보다 큰 값은 오른쪽으로 밀기
            arr[j+1] = arr[j]# 값 이동
            j-=1# 왼쪽으로 한 칸 이동

        arr[j+1] = key # 올바른 위치에 key 삽입

    return arr  # 정렬된 배열 반환


def quick_sort(arr):
    if len(arr)<= 1:
        return arr
    
    pivot = arr[-1]

    left = []
    middle = []
    right = []

    for x in arr:
        if x < pivot:
            left.append(x)
        elif x == pivot:
            middle.append(x)
        else:
            right.append(x)
        
    return quick_sort(left) + middle + quick_sort(right)


if __name__ == "__main__":  # 메인 실행 블록

    sample = [64, 25, 12, 22, 11]  # 테스트용 배열
    
    print("Original:", sample)  # 원본 배열 출력

    print("Selection Sort:", selection_sort(sample.copy()))  # 선택 정렬 결과
    print("Bubble Sort:", bubble_sort(sample.copy()))  # 버블 정렬 결과
    print("Insertion Sort:", insertion_sort(sample.copy()))  # 삽입 정렬 결과
    print("Quick Sort:", quick_sort(sample.copy()))  # 퀵 정렬 결과
