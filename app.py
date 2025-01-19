# Learning Functions:
def find_ap_term(ap: list, position: int) -> int:
    if not isinstance(ap, list) or len(ap) < 2:
        raise ValueError("`ap` must be a list with at least two terms.")
    if not isinstance(position, int) or position <= 0:
        raise ValueError("`position` must be a positive integer.")
    a = ap[0]
    common_difference = ap[1] - ap[0]
    term = a + (position - 1) * common_difference
    return term


try:
    ap_input = input(
        "Enter the numbers of the AP, separated by commas (e.g., 2,4,6,8): "
    ).strip()
    ap = list(map(int, ap_input.split(",")))
    if len(ap) < 2:
        print("An AP requires at least two terms.")
    else:
        position = int(input("Enter the position of the term you want to find: "))
        if position <= 0:
            print("Position must be a positive integer.")
        else:
            nth_term = ap_finder(ap, position)
            print(f"\nThe term at position {position} in the AP is: {nth_term}")
except ValueError:
    print("Invalid input. Please ensure you enter numbers correctly.")
