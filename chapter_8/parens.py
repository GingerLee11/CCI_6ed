# python3
# parens.py - Prints out all the parenthesis combonations possible given an inputted number of parenthesis pairs.

def parens(n):
    """
    Prints out all the parenthesis combonations possible given an inputted number of parenthesis pairs.
    """
    all_paren_combos = []

    def get_paren_combos(paren, left_remaining, right_remaining):
        """
        Helper function for parens
        """
        # Base Case: 
        if len(paren) == n * 2:
            if paren not in all_paren_combos:
                all_paren_combos.append(paren)

        if left_remaining > 0:
            get_paren_combos(paren + '(', left_remaining - 1, right_remaining)
            
        if right_remaining > left_remaining:
            get_paren_combos(paren + ')', left_remaining, right_remaining -1)

    get_paren_combos("", n, n)
    return all_paren_combos


if __name__ == "__main__":
    print(parens(1))
    print(parens(2))
    print(parens(3))
    print(parens(4))
