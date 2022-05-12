# python3
# pattern_matching.py

import re

def pattern_matcher(pattern, value):

    
    dup_regex = re.compile(r"(.+)\1+")
    mo = re.match(dup_regex, value)

    match_dict = {}

    if mo:  
        value_2 = re.sub(mo.group(1), '', value)
        match_dict[mo.group(1)] = 'a'
        mo_2 = re.match(dup_regex, value_2)
        if mo_2:
            match_dict[mo_2.group(1)] = 'b'
        
            final_value = value
            for key in match_dict.keys():
                final_value = re.sub(key, match_dict[key], final_value)

                return final_value == pattern
        
        else:
            # Check to see if the pattern will sub to the same combination as value:
            mo_pattern = re.match(dup_regex, pattern)
            if mo_pattern:
                pattern_2 = re.sub(mo_pattern.group(1), '', pattern)
                match_dict[mo_pattern.group(1)] = 'a'

                final_value = value
                final_pattern = pattern
                for key in match_dict.keys():
                    final_value = re.sub(key, match_dict[key], final_value)
                    final_pattern = re.sub(key, match_dict[key], final_pattern)

                return final_value == final_pattern
    
    if pattern == 'ab' or pattern == 'ba':
        if len(value) >= 2 and mo == None:
            return True
    
    return False
        


        
def simple_pattern_matcher(pattern, value, pattern_dict):
    """
    Pattern matcher with a dictionary
    """
    final_value = value
    for key in pattern_dict.keys():
        final_value = re.sub(key, pattern_dict[key], final_value)

    return pattern == final_value

    

    

def example():

    pattern = 'abaaab'
    value = 'catgocatcatcatgo'
    print(pattern_matcher(pattern, value))
    pattern_dict = {
        'cat': 'a',
        'go': 'b',
    }
    print(simple_pattern_matcher(pattern, value, pattern_dict))


if __name__ == "__main__":
    example()
