# python3
# string_compression.py - Takes in a string and returns the compressed version with single characters followed by an integer count of that character.

def string_compression(s):
    '''
    Takes in a string and returns the compressed version with single characters followed by an integer count of that character.
    '''

    char_count = 1
    s_comp = ''
    cur_char = ''
    for char in s:
        # For the first current character which will be a blank
        if cur_char == '':
            cur_char = char
        elif char == cur_char:
            char_count += 1
        else:
            s_comp += cur_char + str(char_count)
            char_count = 1
        cur_char = char

    # For the last char and char count after the four loop
    s_comp += cur_char + str(char_count)

    # Only return the compressed string if it is actually shorter than the original string.
    if len(s_comp) < len(s):
        return print(s_comp)
    else: return print(s)


string_compression('aabcccccaaa')
string_compression('abcdefghijklmnopqrstuvwxyz')
string_compression('awefasdkdkdkdkdddddddddddddddddddddddddddddddddddddddddddqaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')
