
def parse_input(path: str) -> tuple[list[list[int]], list[int]]:
    raw_content = ""
    with open(path, "r") as f:
        raw_content = f.read()
    
    raw_ranges_list, raw_items_list = [x.split("\n") for x in raw_content.split("\n\n")]

    ranges_list = [[int(y) for y in x.split("-")] for x in raw_ranges_list]
    items_list  = [int(x) for x in raw_items_list[:-1]]

    return ranges_list, items_list


def main() -> None:
    ranges, items = parse_input("day5/input.inp")
    fresh = 0
    for item in items:

        for r_start, r_end in ranges:

            if item >= r_start and item <= r_end:
                fresh += 1
                break

    print(fresh)

main()
