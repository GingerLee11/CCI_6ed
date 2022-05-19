# python3
# rand7_from_rand5.py - Creates a function that generates a random integer between 0 - 6 using rand(0, 4).

from random import randint

def rand7_from_rand_5():
    """
    Creates a function that generates a random integer between 0 - 6 using rand(0, 4).
    """
    random_int = randint(0, 4)
    x = None
    nums = [0, 1, 2, 3, 4, 5, 6]
    for j in range(len(nums)):
        indx = randint(0, 4)
        nums = nums[indx:] + nums[:indx]
    i = 0
    while random_int != x:
        x = randint(0, 4)
        num = nums[i]
        if i == 7:
            i = 0
    
    return num


def example():

    rand_gen_nums = []

    for i in range(100000):
        n = rand7_from_rand_5()
        rand_gen_nums.append(n)
    
    probabilities = {}
    differences = {}
    expected_probability = 1 / 7
    for i in range(0, 7):
        nums = [n for n in rand_gen_nums if n == i]
        prob = len(nums) / len(rand_gen_nums)
        probabilities[i] = prob
        differences[i] = prob - expected_probability

    print(probabilities)
    print(differences)


if __name__ == "__main__":
    example()
