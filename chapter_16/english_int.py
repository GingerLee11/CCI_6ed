# pythonn3
# english_int.py - Takes in an integer and returns the text English representation of that integer.

from math import floor, log

def english_int(int_to_text_dict, n):
    """
    Takes in an integer and returns the text English representation of that integer.
    """
    text = ''
    num = str(n)
    converted = 0
    length = len(num)
    group_length = len(num) % 3
    if group_length == 0:
        group_length = 3
    # Splits all numbers into groups of 3s:
    # hundreds, thousands, millions, billions, trillions...
    group_of_3_dict = {
        1: 'thousand',
        2: 'million',
        3: 'billion',
        4: 'trillion',
    }

    # Goes through the groups of three until the ones place is reached
    while converted < length:
        group = num[converted: group_length + converted]
        hundreds = floor(int(group) / 100)
        # Appending text for the hundreds place
        if hundreds > 0:
            text += int_to_text_dict[hundreds]
            text += ' '
            text += 'hundred'
            text += ' '
        
        # Text for the tens place is more complicated in English because of 11, 12, 13 ... 19
        # Check for the first group
        if len(group) > 1:
            tens_group = group[len(group) - 2 : len(group)]
            tens = floor(int(tens_group) / 10)
            # "-teens check"
            if tens >= 2:
                tens = str(tens)
                tens += '0'
                text += int_to_text_dict[int(tens)]
                text += ' '
            
                # Ones for this group:
                ones = group[-1]
                if ones != '0':
                    text += int_to_text_dict[int(ones)]
                    text += ' '
            # If the number is in the teens or less than 10
            else:
                if int(tens_group) != 0:
                    text += int_to_text_dict[int(tens_group)]
                    text += ' '
        
        else:
            text += int_to_text_dict[int(group)]
            text += ' '

        # Appending the group unit (e.g. thousand, million, billion...)
        group_unit = length - converted
        # Check to make sure the group is greater than 999
        if group_unit > 3:
            group_num = 10 ** (group_unit - 1)
            group_digit = floor(log(group_num) / log(1000))
            text += group_of_3_dict[group_digit]
            text += ' '
        
        converted += group_length
        group_length = 3

    return text


def example():

    int_to_text_dict = {
        0: 'zero',
        1: 'one',
        2: 'two',
        3: 'three',
        4: 'four',
        5: 'five',
        6: 'six',
        7: 'seven',
        8: 'eight',
        9: 'nine',
        10: 'ten',
        11: 'eleven',
        12: 'twelve',
        13: 'thirteen',
        14: 'fourteen',
        15: 'fifteen',
        16: 'sixteen',
        17: 'seventeen',
        18: 'eighteen',
        19: 'nineteen',
        20: 'twenty',
        30: 'thirty',
        40: 'fourty',
        50: 'fifty',
        60: 'sixty',
        70: 'seventy',
        80: 'eighty',
        90: 'ninety',
    }

    print(english_int(int_to_text_dict, 1234567890))
    # print(english_int(int_to_text_dict, 1019012811))
    # print(english_int(int_to_text_dict, 100000000000))
    # print(english_int(int_to_text_dict, 100000))
    # for x in range(101):
    #     if x == 100:
    #         print(english_int(int_to_text_dict, x))
    #     else:
    #         print(english_int(int_to_text_dict, x))


if __name__ == "__main__":
    example()
