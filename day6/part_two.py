
def parse_input(path: str) -> tuple[list[list[int]], list[str]]:
    raw_content = ""
    with open(path, "r") as f:
        raw_content = f.read()
  
    rows = raw_content.split("\n")[:-1]
    
    numbers = [[]]

    for x in range(len(rows[0])):
        coll_result = 0
        blank_coll = True
        for y in range(len(rows) -1):
            if rows[y][x] != ' ':
                coll_result *= 10
                coll_result += int(rows[y][x])
                blank_coll = False

        if blank_coll: numbers.append([])
        else: numbers[-1].append(coll_result)
    operations = [x for x in rows[-1].split(" ") if x]

    return numbers, operations



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
