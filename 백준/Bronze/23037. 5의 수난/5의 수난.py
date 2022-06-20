from math import pow

def solve(n: str) -> int:
    return int(sum([pow(int(x), 5) for x in n]))

if __name__ == '__main__':
    n = input()

    print(solve(n))