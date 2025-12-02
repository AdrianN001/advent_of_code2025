import math


def parse_input(path: str) -> list[str]:
    with open(path, "r") as f:
        return [chunk.strip() for chunk in f.read().split(",") if chunk.strip()]

def check_if_invalid(n: int) -> bool:
    s = str(n)
    L = len(s)

    pattern = str()
    matches = 0

    for i in range(1,L): 
        if (L % i) != 0:
            continue
        pattern = s[: i]

        potential_occur = L//i
        matches = (pattern * potential_occur) == s
        
        if matches and potential_occur >= 2:
            return True
    return False



def main() -> None:


    inp_data = parse_input("day2/input.inp")
    
    invalid_ids_sum = 0



    for ranges in inp_data:
        start, end = [int(x) for x in ranges.split('-')]

        for _id in range(start,end+1):
            
            if check_if_invalid(_id):
                invalid_ids_sum += _id

    print(invalid_ids_sum)



main()
