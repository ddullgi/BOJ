def solution(sequence, k):
    arr_sum = 0
    right = 0
    result = []
    l = len(sequence)
    for left in range(l):
        while right < l and arr_sum < k:
            arr_sum += sequence[right]
            right += 1

        if arr_sum == k:
            if not result:
                result = [left, right - 1]
            else:
                result = result if result[1] - result[0] <= (right - 1) - left else [left, right - 1]

        arr_sum -= sequence[left]

    return result