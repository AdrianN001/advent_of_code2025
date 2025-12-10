 
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


def main() -> None:
    S, splitters, height, width = parse_input("day7/input.inp")
    raw_map = read_input_raw("day7/input.inp")

    beans = [(S, 1)]

    n_of_breaks = 0

    for new_height in range(1, height):
        
        potential_new_beans = [(x[0], new_height) for x in beans ]
        actual_new_beans = []

        for potential_new_bean in potential_new_beans:
            for splitter in splitters: 
                if potential_new_bean == splitter:
                    actual_new_beans.append((splitter[0]-1, splitter[1]))
                    actual_new_beans.append((splitter[0]+1, splitter[1]))
                    n_of_breaks += 1
                    break 
            else:
                actual_new_beans.append(potential_new_bean)

        for x, y in actual_new_beans:
            raw_map[y][x] = "|"
        print("\n".join(["".join(x) for x in raw_map]))


        beans = list(set(actual_new_beans))
    
    print(n_of_breaks)
    print(len(beans)) 



    print(S, splitters, height, width)


main()
