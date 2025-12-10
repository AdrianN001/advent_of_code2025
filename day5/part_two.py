
def parse_input(path: str) -> tuple[list[list[int]], list[int]]:
    raw_content = ""
    with open(path, "r") as f:
        raw_content = f.read()
    
    raw_ranges_list, raw_items_list = [x.split("\n") for x in raw_content.split("\n\n")]

    ranges_list = [[int(y) for y in x.split("-")] for x in raw_ranges_list]
    items_list  = [int(x) for x in raw_items_list[:-1]]

    return ranges_list, items_list

def get_range_length(merged_range: list[int]) -> int:
    a,b = merged_range
    return b-a +1

def main() -> None:
    ranges, items = parse_input("day5/input.inp")

    ranges.sort(key=lambda x: x[0])
    print(ranges)

    merged_ranges = []

    for curr_range in ranges:
        if len(merged_ranges) == 0: 
            merged_ranges.append(curr_range)
            continue
        
        for indx, merged_range in enumerate(merged_ranges):
            range_start, range_end = merged_range
            if curr_range[0] <= range_end+1:
                merged_ranges[indx][1] = max(merged_ranges[indx][1], curr_range[1])
                break 
        else:
            merged_ranges.append(curr_range)
    
    print(sum(get_range_length(x) for x in merged_ranges))

main()
