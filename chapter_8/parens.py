# python3
# parens.py - Prints out all the parenthesis combonations possible given an inputted number of parenthesis pairs.

def parens(paren_pairs):
    """
    Prints out all the parenthesis combonations possible given an inputted number of parenthesis pairs.
    """
    all_paren_combos = []
    get_paren_combos("", paren_pairs, paren_pairs, all_paren_combos)
    return all_paren_combos


def get_paren_combos(paren, left, right, all_paren_combos):
    """
    Helper function for parens
    """
    # Sanity check
    # if right < left:
        # raise Exception("Left parenthesis must be opened before right parenthesis.")

    left_count = left
    right_count = right

    
    for i in range(left_count, 0, -1):
        paren += '(' * i
        left_count -= i
        paren += ')' * i
        right_count -= i

        # Base Case: 
        if left_count == 0 and right_count == 0:
            if paren not in all_paren_combos:
                all_paren_combos.append(paren)
        else:
            get_paren_combos(paren[i] + paren[2 * i], left - 1, right - 1, all_paren_combos)
        


if __name__ == "__main__":
    print(parens(1))
    print(parens(2))
    print(parens(3))
