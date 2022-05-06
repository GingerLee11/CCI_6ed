# python3
# XML_encoding.py - Takes in a string of XML elements and attributes and prints an encoded message.

import re
import unittest

def XML_encoding(XML_element, encoding_dict):
    """
    Takes in a string of XML elements and attributes and prints an encoded message.
    """
    for key in encoding_dict.keys():

        XML_element = re.sub(key, str(encoding_dict[key]), XML_element)

    num_regex = r'(\d+)'
    attri_regex = r'="(\w+)"'
    text_regex = r'(\w+)'

    msg = XML_element.split(" ")
    msg = [part for part in msg if part != ""]
    encoded_msg = ''
    for part in msg:

        num_match = re.search(num_regex, part)
        attri_match = re.search(attri_regex, part)
        text_match = re.search(text_regex, part)

        if num_match:
            # print(num_match.group(1), end=" ")
            encoded_msg += f"{num_match.group(1)} "
        elif attri_match:
            # print(attri_match.group(1), end=" ")
            encoded_msg += f"{attri_match.group(1)} "
        elif text_match:
            # print(text_match.group(1), end=" ")
            encoded_msg += f"{text_match.group(1)} "

    return encoded_msg
    

def example():

    XML_code = """
        <family lastName="McDowell" state="CA">
            <person firstName="Gayle">Some Message</person>
        </family>
    """
    encoding_dict = {
        r'</\w+>': " 0 ",
        '>': " 0 " ,
        r'(<)?family': " 1 ",
        r'(<)?person': " 2 ",
        'firstName': " 3 ",
        'lastName': " 4 ",
        'state': " 5 ",
        '\n': "",
    }
    print(XML_encoding(XML_code, encoding_dict))




class Test(unittest.TestCase):

    XML_codes = [
        """
        <family lastName="McDowell" state="CA">
            <person firstName="Gayle">Some Message</person>
        </family>
        """,

    ]
    encoded_dicts = [
        {
            r'</\w+>': " 0 ",
            '>': " 0 " ,
            r'(<)?family': " 1 ",
            r'(<)?person': " 2 ",
            'firstName': " 3 ",
            'lastName': " 4 ",
            'state': " 5 ",
            '\n': "", 
        }
    ]
    expected_strings = [
        "1 4 McDowell 5 CA 0 2 3 Gayle 0 Some Message 0 0 "
    ]

    def test_XML_encoding(self):
        for XML_code, encoded_dict, expected in zip(self.XML_codes, self.encoded_dicts, self.expected_strings):
            actual = XML_encoding(XML_code, encoded_dict)
            assert actual == expected


if __name__ == "__main__":
    unittest.main()
