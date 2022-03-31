# python3
# permutations_without_dups.py - Computes all the permutations for a given string with unique characters.


# Approach 1: building from permutations of first n-1 characters
def get_perms(text):
    """
    Computes all the permutations for a given string with unique characters.
    """
    permutations = []
    if text is None:
        return None
    
    # base case    
    if len(text) == 0:
        permutations.append(" ")
        return permutations
    
    first = text[0] # get first letter in string
    remainder = text[1:]
    words = get_perms(remainder)
    for word in words:
        index = 0
        for char in word:
            s = insert_char_at(word, first, index)
            permutations.append(s)
            index += 1
    return permutations


def insert_char_at(word, char, i):
    start = word[:i]
    end = word[i:]
    return start + char + end


# Approach 2:
def get_perms_2(text):
    """
    Building from permutations of all n-1 character substrings
    """
    result = []
    get_perms_inner(" ", text, result)
    return result

def get_perms_inner(prefix, remainder, result):
    if len(remainder) == 0:
        result.append(prefix)
    length = len(remainder)
    for i in range(length):
        before = remainder[:i]
        after = remainder[1 + i :]
        c = remainder[i]
        get_perms_inner(prefix + c, before + after, result)


if __name__ == "__main__":
    print(get_perms('abcd'))
    print()
    print(get_perms_2('abcd'))
