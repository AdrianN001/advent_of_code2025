
def parse_input(path: str) -> list[list[int]]:
    with open(path, "r") as f:
        return [[int(y) for y in x] for x in f.read().split("\n")[:-1]]

def get_biggest_number(bank: list[int]) -> int:

    max_n = 0
    for i in range(len(bank)):
        for j in range(i, len(bank)):
            curr = bank[i]*10 + bank[j]
            if curr > max_n and i != j:
                max_n = curr
    print(max_n)
    return max_n

def main() -> None:
    data = parse_input("day3/input.inp")
    
    result = 0 
    for line in data:
        result += get_biggest_number(line)

    print(result)


main()

