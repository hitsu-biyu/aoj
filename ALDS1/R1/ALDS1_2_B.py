def SelectionSort(A, N):
    count = 0
    for i in range(N):
        minj = i
        for j in range(i, N):
            if A[j] < A[minj]:
                minj = j
        if A[i] > A[minj]:
            A[i], A[minj] = A[minj], A[i]
            count += 1 
    print(' '.join(map(str, A)))
    print(count)

N = int(input())
A = list(map(int, input().split()))
SelectionSort(A, N)