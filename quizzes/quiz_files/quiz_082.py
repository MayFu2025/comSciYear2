def merge_sort(M:list[int])->list[int]:
    if len(M) <= 1:
        return M
    N = len(M) // 2
    L = merge_sort(M[:N])
    R = merge_sort(M[N:])

    s, i, j = [], 0, 0
    while i < len(L) and j < len(R):
        if L[i] < R[j]:
            s.append(L[i])
            i += 1
        else:
            s.append(R[j])
            j += 1

    return s + L[i:] + R[j:]

print(merge_sort([3, 1, 8, 7, 2, 5]))