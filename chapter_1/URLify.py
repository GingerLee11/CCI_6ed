# python3
# URLify.py - Takes in a string and replaces all the spaces with "%20" emulating a URL

def urlify(s):
    '''
    Takes in a string and replaces all the spaces with "%20" emulating a URL
    '''
    new_s = s.strip().replace(" ", "%20")
    return new_s

print(urlify("   Mr John Smith  "))