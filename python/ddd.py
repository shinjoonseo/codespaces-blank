# 퀵 정렬

# 입력: 리스트 a

# 출력: 없음(입력으로 주어진 a가 정렬됨)

# 리스트 a의 어디부터(start) 어디까지(end)가 정렬 대상인지

# 범위를 지정하여 정렬하는 재귀 호출 함수

def quick_sort_sub(a, start, end):

    # 종료 조건: 정렬 대상이 1개 이하면 정렬할 필요 없음

    if end - start <= 0:

        return

    # 기준 값을 정하고 기준 값에 맞춰 리스트 안에서 각 자료의 위치를 맞춤

    # [기준 값보다 작은 값들, 기준 값, 기준 값보다 큰 값들]

    pivot = a[end]    # 편의상 리스트의 마지막 값을 기준 값으로 정합

    print(a[end])

    i = start

    for j in range(start, end):

        if a[j] <= pivot:

            print(a[i], a[j])

            a[i], a[j] = a[j], a[i]

            print(a[i], a[j])

            i += 1

    a[i], a[end] = a[end], a[i]

    # 재귀 호출 부분

    quick_sort_sub(a, start, i - 1) # 기준 값보다 작은 그룹을 재귀 호출로 다시 정렬

    quick_sort_sub(a, i + 1, end)   # 기준 값보다 큰 그룹을 재귀 호출로 다시 정렬