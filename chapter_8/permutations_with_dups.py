# python3
# permutations_with_dups.py - Computes all the permutations for a given string that may contain duplicate characters. 
# No duplicate permutations


def get_perms(text):
    """
    Computes all the permutations for a given string that may contain duplicate characters. 
    No duplicate permutations are returned.
    """
    all_perms = []
    get_inner_perms(" ", text, all_perms)
    return all_perms


def get_inner_perms(prefix, remainder, all_perms):
    # Base Case
    if len(remainder) == 0:
        if prefix not in all_perms:
            all_perms.append(prefix)
    length = len(remainder)
    for i in range(length):
        before = remainder[:i]
        after = remainder[i + 1 :]
        c = remainder[i]
        get_inner_perms(prefix + c, after + before, all_perms)


if __name__ == "__main__":
    print(get_perms('ababab'))
