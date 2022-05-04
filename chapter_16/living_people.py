# python3
# living_people.py - Calculates the year with the highest population
# and returns both that year and the population

from random import randint

def living_people(list_of_people):
    """
    Calculates the year with the highest population
    and returns both that year and the population.
    """
    birth_dict = {}
    death_dict = {}
    total_pop = 0
    pop_by_year = {}
    none_count = 0
    # Creates dictionaries for each year of how many people were born and how many died
    for birth, death in list_of_people:
        if birth not in birth_dict:
            birth_dict[birth] = 1
        else:
            birth_dict[birth] += 1
        if death is not None:
            if death not in death_dict:
                death_dict[death] = 1
            else:
                death_dict[death] += 1
        else:
            none_count += 1
        
        
    max_pop = 0
    max_year = 1900
    # Goes through all the years from 1900 to 2000 (including 2000)
    for curr_year in range(1900, 2001):

        total_pop += birth_dict[curr_year]
        total_pop -= death_dict[curr_year]

        pop_by_year[curr_year] = total_pop

        if total_pop > max_pop:
            max_pop = total_pop
            max_year = curr_year

    return max_year, max_pop


def example():

    people = []
    for x in range(100000):

        birth = randint(1900, 2000)
        # Creates a more realistic scenario where not everyone
        # Dies at the turn of the century
        # An even more accurate simulation would be to use life
        # expectancy for each decade or year to predict the max population.
        #if birth < 1950:
        death = randint(birth, 2000)
        # else:
        #     death = None
        person = (birth, death)
        people.append(person)

    max_year, max_pop = living_people(people)
    print(f"The year with the max living population of {max_pop} people was {max_year}.")


if __name__ == "__main__":
    example()
