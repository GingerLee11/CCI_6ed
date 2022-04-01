# python3
# parens.py - Prints out all the parenthesis combonations possible given an inputted number of parenthesis pairs.

def parens(paren_pairs):
    """
    Prints out all the parenthesis combonations possible given an inputted number of parenthesis pairs.
    """
    all_paren_combos = []
    get_paren_combos(" ", paren_pairs, paren_pairs, all_paren_combos)
    return all_paren_combos


def get_paren_combos(paren, left, right, all_paren_combos):
    """
    Helper function for parens
    """
    # Sanity check
    if right < left:
        raise Exception("Left parenthesis must be opened before right parenthesis.")
    
    # Base Case: 
    if left == 0 and right == 0:
        if paren not in all_paren_combos:
            all_paren_combos.append(paren)
            


    left_count = left
    right_count = right

    while left_count != 0:
        paren += '(' 
        # left_parens = paren[:left]
        left_count -= 1
        get_paren_combos(paren, left_count, right_count, all_paren_combos)
    
    while right_count != 0:
        paren += ')'
        # right_parens = paren[right:]
        right_count -= 1
        get_paren_combos(paren, left_count, right_count, all_paren_combos)


if __name__ == "__main__":
    print(parens(1))
    print(parens(2))
