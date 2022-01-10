# python3
# one_away.py - Checks to see if two string are one character off from each other. 

from itertools import tee, islice, chain, zip_longest

def previous_and_next(some_iterable):
    prevs, items, nexts = tee(some_iterable, 3)
    prevs = chain([None], prevs)
    nexts = chain(islice(nexts, 1, None), [None])
    return zip(prevs, items, nexts)

def one_away(s1, s2):
    """
    Checks to see if two string are one character off from each other.
    """

    # TODO: Strip the white space in front of and behind the characters

    if abs(len(s1) - len(s2)) > 1:
        return print("More than one away.")
    if len(s1) > len(s2):
        s2 = s2 + ' '
    elif len(s2) > len(s1):
        s1 = s1 + ' '
    # Define the off_count to see how far off the strings are
    off_count = 0
    string_case = ''
    # Create previous and next values for both strings
    for (prev1, item1, nxt1), (prev2, item2, nxt2) in zip_longest(previous_and_next(s1), previous_and_next(s2)):
        # Adjust the indicies after a removal or insertion string edit
        if string_case == 'Removal':
            item2 = prev2
        elif string_case == "Insertion":
            item1 = nxt1

        # If the two characters match, then continue
        if item1 == item2:
            continue
        elif (item1 == None) | (item2 == None):
            break

        # Replacement case, one char difference
        elif item1 != item2:
            # Removal case, where the second string has one more than the first
            # EX: pale,  paale
            if item1 == prev2:
                off_count += 1
                string_case = 'Removal'
                # item1 = prev1
            # Insertion case, where second string has one less than the first
            # EX: pale,  ple
            elif nxt1 == item2:
                off_count += 1
                string_case = 'Insertion'
                # item1 = nxt1
            
            # Replacement case, this is only hit if none of the other conditionals are met
            else:
                off_count += 1
     
    if off_count > 1:
        return print("More than one away.")
    elif off_count == 1:
        return print("One away.")
    elif off_count == 0:
        return print("Exact match.")


one_away('bake', 'bale')
one_away('baleee', 'baleeeeees')
one_away('bake', 'pale')
one_away('pale', 'ple')
one_away('paale', 'pale')
one_away('bake', 'bake')
one_away('cakes', 'cake')
one_away('cake', 'cakes')
one_away('bbbb', 'pppp')
one_away('bb', 'b')
one_away('bb', 'bp')
one_away(' bb', 'bp')
one_away(' bb', 'bb')

