
def parse_input(path: str) -> list[list[str]]:
    with open(path, "r") as f:
        return [[y for y in x] for x in f.read().split("\n")[:-1]]

def process_point(x: int, y: int, map: list[list[str]]) -> int:
    i = 0
    for s_x in range(-1, 2):
        for s_y in range(-1, 2):
            if s_y == 0 and s_x == 0: continue
            if s_y + y < 0 or s_x +x < 0: continue
            try:
                s_p = map[y + s_y][x+s_x]
                if s_p == "@":
                    i += 1
            except IndexError:
                continue 
    return i

def process_map(data: list[list[str]]) -> int:
    res = 0

    for x in range(len(data)):
        for y in range(len(data[x])):
            if data[y][x] == "@":
                if process_point(x,y, data) < 4:
                    res += 1
                else:
                    print(x,y, process_point(x,y,data))

    return res


def main() -> None:
    data = parse_input("day4/test.inp")
    res = process_map(data)
    print(res)


main()


