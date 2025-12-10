
def parse_input(path: str) -> list[list[int]]:
    with open(path, "r") as f:
        return [[int(y) for y in x] for x in f.read().split("\n")[:-1]]

# greedy
def get_biggest_number(bank: list[int]) -> int:
    remaining_digits = 12
    window_start = 0

    result = 0

    while remaining_digits != 0: 
        
        local_max = -1
        
        i = window_start
        while i < len(bank) - remaining_digits+1:
            if bank[i] > local_max:
                local_max = bank[i]
                window_start = i+1
            i += 1

        result *= 10
        result += local_max

        remaining_digits -= 1
    
    return result

def main() -> None:
    data = parse_input("day3/input.inp")
    
    result = 0 
    for line in data:
        result += get_biggest_number(line)

    print(result)


main()

