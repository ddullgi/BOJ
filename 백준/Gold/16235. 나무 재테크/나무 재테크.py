def plus_age(area_data, a, k):
    n = len(area_data)
    # k년 반복
    for _ in range(k):
        # 나무가 나이를 1살 먹음
        # 양분은 나이가 적은 순서대로 먹고 먹지 못하면 죽는다
        # 죽은 나무는 나이/2 의 양분으로 바뀜 소수점은 버린다
        for y in range(n):
            for x in range(n):
                if area_data[y][x]["tree_age"]:
                    area_data[y][x]["tree_age"].sort()
                    new_tree_age = []
                    dead_nutrients = 0
                    for age in area_data[y][x]["tree_age"]:
                        if area_data[y][x]["manure"] >= age:
                            area_data[y][x]["manure"] -= age
                            new_tree_age.append(age + 1)
                        else:
                            dead_nutrients += age // 2
                    area_data[y][x]["tree_age"] = new_tree_age
                    area_data[y][x]["manure"] += dead_nutrients
                area_data[y][x]["manure"] += a[y][x]

        # 나이가 5의 배수인 나무는 인접 8칸에 나이가 1인 나무를 생성한다
        directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        for y in range(n):
            for x in range(n):
                for age in area_data[y][x]["tree_age"]:
                    if age % 5 == 0:
                        for dy, dx in directions:
                            ny, nx = y + dy, x + dx
                            if 0 <= ny < n and 0 <= nx < n:
                                area_data[ny][nx]["tree_age"].append(1)


def main():
    n, m, k = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(n)]
    area = [[{"manure": 5, "tree_age": []} for _ in range(n)] for _ in range(n)]
    for j in range(m):
        x, y, z = map(int, input().split())
        area[x - 1][y - 1]["tree_age"].append(z)

    plus_age(area, a, k)

    alive_trees = sum(len(area[y][x]["tree_age"]) for y in range(n) for x in range(n))
    print(alive_trees)

main()
