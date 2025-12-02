zero = 0


def parse_input(path: str) -> list[str]: 
    with open(path, "r") as file:
        return file.read().split("\n")[:-1]

def rotate_dial(current: int, direction: str, amount: int) -> int:
    global zero

    for _ in range(amount):
        if direction == "L":
            current -= 1 
        else:
            current += 1 
        
        if current == 100:  current = 0
        if current == -1:   current = 99
 
        if current == 0:
            zero += 1

    return current

def main() -> None:
    global zero
    inp_data = parse_input("day1/input1.inp")
    
    state = 50
    for line in inp_data:
        direction = line[0]
        amount = int(line[1:])
        state = rotate_dial(state, direction, amount)
    print(state, zero)


if __name__ == "__main__":
    main()
