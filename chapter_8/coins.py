# python3
# coins.py - Function that calculates the number of ways to calculate n cents.


def calc_ways_to_count_coins(coins, n_cents):
    """
    Function that calculates the number of ways to calculate n cents.
    """
    n = 0
    coin = coins[n]
    number_of_ways, amount_list = [], []
    
    def count_coins(coin, amount, amount_list, n):
        """
        Helper recursive function that counts the coins 
        """

        # Base Case:
        if amount == 0:
            if amount_list not in number_of_ways:
                number_of_ways.append(amount_list)


        if amount - coin >= 0:
            amount -= coin
            amount_list.append(coin)
            count_coins(coin, amount, amount_list, n)
        else:
            # Go to the next largest coin in the list of coins
            if n < len(coins) - 1:
                n += 1
                coin = coins[n]
                count_coins(coin, amount, amount_list, n)

          
    count_coins(coin, n_cents, amount_list, n)
    return number_of_ways


def example():

    # US coins:
    COINS = [25, 10, 5, 1]

    num_ways = calc_ways_to_count_coins(COINS, 25)
    print(num_ways)
    print(len(num_ways))


if __name__ == "__main__":
    example()