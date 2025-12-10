 
from functools import lru_cache

def parse_input(path: str) -> tuple[int, list, int, int] :
    raw_content = ""
    with open(path, "r") as f:
        raw_content = f.read()

    lines = raw_content.split('\n')[:-1]
    S = lines[0].index("S")

    splitters = []

    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            if char == "^":
                splitters.append((x,y))

    return S, splitters, len(lines), len(lines[0])

def read_input_raw(path: str) -> list[list[str]]:
    with open(path, "r") as f:
        return [[y for y in x] for x in f.read().split("\n")[:-1]]

def trace_bean(bean_pos: tuple, splitters: list, height: int) -> int:
    split_set = set(splitters)  # O(1) lookup

    @lru_cache(None)
    def f(x, y, rest):
        # rest = verbleibende Schritte (height)
        if rest == 0:
            return 1
        nx, ny = x, y + 1
        if (nx, ny) in split_set:
            return f(nx-1, ny, rest-1) + f(nx+1, ny, rest-1)
        else:
            return f(nx, ny, rest-1)

    sx, sy = bean_pos
    return f(sx, sy, height)

def main() -> None:
    S, splitters, height, width = parse_input("day7/input.inp")

    number_of_timeline = trace_bean((S,1), splitters, height)


    print(number_of_timeline)


main()
