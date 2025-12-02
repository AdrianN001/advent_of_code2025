
def parse_input(path: str) -> list[str]: 
    with open(path, "r") as file:
        return file.read().split("\n")[:-1]

def rotate_dial(current: int, direction: str, amount: int) -> int:
    if current == 100:  current = 0
    if current == -1:   current = 99
    if amount == 0:     return current
    
    if direction == "L":
        return rotate_dial(current-1, "L", amount-1)
    else:
        return rotate_dial(current+1, "R", amount-1)


def main() -> None:
    inp_data = parse_input("day1/input1.inp")
    
    state = 50
    zero = 0
    for line in inp_data:
        direction = line[0]
        amount = int(line[1:])
        if amount > 100:
            amount = amount % 100
            zero += amount // 100
        state = rotate_dial(state, direction, amount)
        if state == 0:
            zero += 1
    print(state, zero)


if __name__ == "__main__":
    main()
