
def parse_input(path: str) -> tuple[list[list[int]], list[str]]:
    raw_content = ""
    with open(path, "r") as f:
        raw_content = f.read()
  
    rows = raw_content.split("\n")[:-1]
    numbers = [[int(y) for y in x.split(" ") if y] for x in rows[:-1]]
    operations = [x for x in rows[-1].split(" ") if x]
    return transform_number_matrix(numbers), operations

def transform_number_matrix(numbers: list[list[int]]) -> list[list[int]]:
    new_numbers = [
        [0] * len(numbers)
        for _ in range(len(numbers[0]))
    ]

    for x in range(len(numbers)):
        for y in range(len(numbers[x])):
            new_numbers[y][x] = numbers[x][y]

    return new_numbers

def add_numbers(numbers: list[int]) -> int:
    if len(numbers) == 0:
        return 0
    return numbers[0] + add_numbers(numbers[1:])

def multiply_numbers(numbers: list[int]) -> int:
    if len(numbers) == 0: 
        return 1
    return numbers[0] * multiply_numbers(numbers[1:])

def main() -> None:
    numbers, operations = parse_input("day6/input.inp")
    print(numbers, operations)
    
    result = 0
    for indx, operation in enumerate(operations):
        if operation == "+":
            result += add_numbers(numbers[indx])
        elif operation == "*":
            result += multiply_numbers(numbers[indx])
    print(result)


main()
