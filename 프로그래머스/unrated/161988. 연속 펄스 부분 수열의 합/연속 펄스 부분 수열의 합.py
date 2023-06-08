def solution(sequence):
    l = len(sequence)
    psum = [0] * (l + 1)
    for i in range(l):
        psum[i + 1] = psum[i] + sequence[i] * (-1) ** i
    
    return max(psum) - min(psum)