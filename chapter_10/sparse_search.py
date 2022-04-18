# python3
# sparse_search.py - Find the location of a string in a list of strings with many blank strings interspersed.


def sparse_search(array, word):
    """
    Find the location of a string in a list of strings with many blank strings interspersed.
    """
    low = 0
    high = len(array) - 1
    mid = 0
    first_letter_indx = ord(word[0])

    while low <= high:
        mid = round((low + high) / 2)
        
        if array[mid] == word:
            return mid

        elif array[mid] == "":
            while array[mid] == "":
                if array[mid] == array[0]:
                    break
                high -= 1
                mid = round((low + high) / 2)

            while array[mid] == "":
                if array[mid] == array[-1]:
                    break
                low += 1
                mid = round((low + high) / 2)

        elif ord(array[mid][0]) < first_letter_indx:
            low = mid + 1
        
        elif ord(array[mid][0]) > first_letter_indx:
            high = mid - 1

    
def example():

    sparse_array = [
        "at", "", "", "", "ball", "", "", "car", "", "", "dad", "", ""
    ]
         
    print(sparse_search(sparse_array, "ball"))


if __name__ == "__main__":
    example()
