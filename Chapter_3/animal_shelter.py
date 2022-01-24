# python3
# animal_shelter.py - Animal Shelter queue that returns the animal that has been in the shelter for the longest,
# Or the cat or dog that has been in the shelter for the longest amount of time.

from collections import deque


class ShelterQueue:
    """
    Animal Shelter queue that returns the animal that has been in the shelter for the longest,
    Or the cat or dog that has been in the shelter for the longest amount of time.
    """
    def __init__(self):
        self._animal_queue = deque()

    def enqueue(self, animal):
        self._animal_queue.append(animal)

    def dequeue_any(self):
        try:
            return self._animal_queue.popleft()
        except IndexError:
            return print("Dequeue from an empty queue.")
        

    def dequeue_dog(self):
        dog = "dog"
        try:
            self._animal_queue.remove(dog)
            return dog
        except ValueError:
            return print(f"{dog} not in deque")

    def dequeue_cat(self):
        cat = "cat"  
        try:
            self._animal_queue.remove(cat)
            return cat
        except ValueError:
            return print(f"{cat} not in deque")

    def __repr__(self):
        return f"Queue({list(self._animal_queue)}"

    def __contains__(self, animal):
        return animal in self._animal_queue

    def __iter__(self):
        yield from self._animal_queue


animals = ["cat", "dog"]

animal_shelter = ShelterQueue()

for i in range(50):
    index = i % len(animals)
    animal = animals[index] 
    # animal = {animal_type: f"{animal_type.capitalize()}: {str(i)}; Group 1"}
    animal_shelter.enqueue(animal)


'''
print(animal_shelter)
for animal in animal_shelter:
    print(animal)

for i in range(10):
    print(animal_shelter.dequeue_cat())

for i in range(10):
    index = i % len(animals)
    animal = animals[index]
    animal_shelter.enqueue(animal)

for i in range(10):
    print(animal_shelter.dequeue_dog())

for i in range(42):
    print(animal_shelter.dequeue_any())
'''