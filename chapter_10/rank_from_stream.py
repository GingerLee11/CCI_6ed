# python3
# rank_from_stream.py - Ranks integers within a stream based on how many integers are less than that specific integer.

import unittest

class IntWithRank:
    """
    Integer with a rank attribute based on how many integers are less than or equal to it.
    """
    def __init__(self, n):
        self.n = n
        self.rank = 0


class RankFromStream:
    """
    Ranks integers within a stream based on how many integers are less than that specific integer.
    """
    def __init__(self):
        self.stream = []

    def _track(self, new, old):
        """
        Tracks the rank of both the new integer coming in 
        and the old integers (in the stream) that it is compared to
        """
        if new.n < old.n:
            old.rank += 1
        elif new.n > old.n:
            new.rank += 1
        elif new.n == old.n:
            old.rank += 1
            new.rank += 1

    def is_empty(self):
        return len(self.stream) == 0
    
    def add_num(self, x):
        """
        Adds new integers to the stream
        """
        new_num = IntWithRank(x)
        if self.is_empty() == True:
            self.stream.append(new_num)
        else:
            for old_num in self.stream:
                self._track(new_num, old_num)
            self.stream.append(new_num)
        return new_num

    def get_rank_of_number(self, x):
        """
        Returns the rank of an inputted integer.
        Returns the first integer that matches the inputted integer 
        (The rank will be identical for all integer of the same integer value).
        """
        for num in self.stream:
            if num.n == x:
                return num.rank
        return None



def example():

    stream = [5, 1, 4, 4, 5, 9, 7, 13, 3]

    stream_rank = RankFromStream()
    for num in stream:
        stream_rank.add_num(num)
        print(stream_rank.get_rank_of_number(5))
    
    print(stream_rank.get_rank_of_number(1))
    print(stream_rank.get_rank_of_number(4))
    print(stream_rank.get_rank_of_number(7))
    print(stream_rank.get_rank_of_number(13))
    

class Test(unittest.TestCase):

    stream = [5, 1, 4, 4, 5, 9, 7, 13, 3]

    def generate(self):
        stream_rank = RankFromStream()
        for num in self.stream:
            stream_rank.add_num(num)
        return stream_rank

    tests = [
        (5, 5),
        (1, 0),
        (4, 3),
        (9, 7),
        (7, 6),
        (13, 8),
        (3, 1),
        (15, None),
    ]
    def test_rank_from_stream(self):
        stream = self.generate()
        for x, expected in self.tests:
            actual = stream.get_rank_of_number(x)
            assert actual == expected


if __name__ == "__main__":
    unittest.main()