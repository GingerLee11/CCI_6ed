# python3
# power_set.py - Given a set, returns all the subsets within that set.


def power_set(given_set):
    """
    Given a set, returns all the subsets within that set.
    """
    all_subsets = [[]]

    def get_subsets(current_set, remaining_set):
        # base case
        if len(remaining_set) == 0:  
            return

        # Iterate and recurse through each element
        for i in range(len(remaining_set)):
            if current_set + [remaining_set[i]] not in all_subsets:
                all_subsets.append(current_set + [remaining_set[i]])
                # This will return the last appended subset as the current set
                # And the remaining set as one less than before
                get_subsets(current_set + [remaining_set[i]], remaining_set[i + 1 :])
            

    get_subsets([], given_set)
    return all_subsets


test_set = list('abcde')

if __name__ == "__main__":
    print(power_set(test_set))