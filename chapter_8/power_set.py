# python3
# power_set.py - Given a set, returns all the subsets within that set.


def power_set(given_set, all_subsets=None):
    """
    Given a set, returns all the subsets within that set.
    """
    if all_subsets == None:
        all_subsets = []

    subset = set()
    # Iterate through all the
    for elem in given_set:
        subset.add(elem)
        if subset not in all_subsets:
            all_subsets.append(subset)
        
        # remove current elem and return the rest of the set
        given_set.remove(elem)
        power_set(given_set, all_subsets)
        given_set.add(elem)

    
    return all_subsets


test_set = set('abc')

if __name__ == "__main__":
    print(power_set(test_set))