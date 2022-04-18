# python3
# sort_big_file.py - Method to sort a very large file (20GB) with one string on each line.

import unittest

def sort_big_file(file):
    """
    Method to sort a very large file (20GB) with one string on each line.
    """
    alphabet_dict = {}

    for line in file:
        # Create keys based on the first character of the strings
        if line[0] in alphabet_dict:

            for indx, entry in enumerate(alphabet_dict[line[0]]):
                if entry == line:
                    alphabet_dict[line[0]].insert(indx, line)
                    break

                # These two conditionals don't work if there are several nearly identical (but not indentical) strings in the file.  
                elif line == entry[0:len(line)]:
                    alphabet_dict[line[0]].insert(indx, line)
                    break

                elif line[0:len(entry)] == entry:
                    alphabet_dict[line[0]].insert(indx + 1, line)
                    break

                elif entry[1] == line[1]:
                    i = 1
                    while i < len(line) and i < len(entry):
                        if ord(line[i]) < ord(entry[i]):
                            alphabet_dict[line[0]].insert(indx, line)
                            break
                        elif ord(line[i]) > ord(entry[i]):
                            alphabet_dict[line[0]].insert(indx + 1, line)
                            break
                        # TODO: Maybe add a conditional to check the lengths of line and entry
                        i += 1
                    break
                    
                elif ord(line[1]) < ord(entry[1]):
                    alphabet_dict[line[0]].insert(indx, line)
                    break
                            
                elif ord(line[1]) > ord(alphabet_dict[line[0]][-1][1]):
                    alphabet_dict[line[0]].append(line)
                    break

        else:
            alphabet_dict[line[0]] = [line]

    return sorted(alphabet_dict.values())


def example():

    test_file = [
        'big',
        'far',
        'time',
        'xylophone',
        'dinosaur',
        'test',
        'biscuit',
        'time',
        'size',
        'ax',
        'lunch',
        'give',
        'me',
        'at',
        'zebra',
        'apple',
        'day',
        'app',
        'dog',
        'axel',
        'axis',
        'axels',
        'meat',
        'bitch',
        'fix',
    ]

    alpha_dict = sort_big_file(test_file)
    print(alpha_dict)

if __name__ == "__main__":
    example()



class Test(unittest.TestCase):

    test_file = [
        'big',
        'far',
        'time',
        'xylophone',
        'dinosaur',
        'test',
        'biscuit',
        'time',
        'size',
        'ax',
        'lunch',
        'give',
        'me',
        'at',
        'zebra',
        'apple',
        'day',
        'app',
        'dog',
        'axel',
        'axis',
        'axels',
        'meat',
        'bitch',
    ]
    sorted_file = [
        'app', 
        'apple', 
        'at', 
        'ax', 
        'axel', 
        'axels', 
        'axis', 
        'big', 
        'biscuit', 
        'bitch', 
        'day', 
        'dinosaur', 
        'dog', 
        'far', 
        'give', 
        'lunch', 
        'me', 
        'meat', 
        'size', 
        'test', 
        'time', 
        'time', 
        'xylophone', 
        'zebra'
    ]


                    
                        