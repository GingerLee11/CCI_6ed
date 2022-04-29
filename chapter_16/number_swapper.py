# python3
# number_swapper.py - Swaps two numbers in place. Or it swaps a number in a list.

def number_swapper_list(num_list, old_num, new_num):

    for indx, num in enumerate(num_list):
        if num == old_num:
            num_list[indx] = new_num
            return num_list

        
def num_swapper_2(a, b):
    a = b
    return a

def example():

    number_list = [x for x in range(10)]
    old_num = 5
    new_num = 42
    print(number_swapper_list(number_list, old_num, new_num))
    
    print(num_swapper_2(old_num, new_num))


if __name__ == "__main__":
    example()