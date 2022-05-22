# LRU_cache.py - Data structure that maps keys and values (like a dictionary),
# but also operates like a cache, in that it evicts an item once the max size has been reached.

from random import randint

class Node:

    def __init__(self, key, value, position):
        self.key = key
        self.value = value
        self.position = position
        self.next = None


class LRUCache:
    """
    Implementation using hash function and linked lists for collisions
    """

    def __init__(self, max_size):
        self.size = 0
        self.max_size = max_size

        self.cache_positions = []
        self.cache = [None for i in range(max_size)]
        
    def hash_function(self, key):
        """
        Hash function takes the ascii value of the key and returns a hash value
        based on the max size of the data structure
        """
        hash = 0
        for char in key:
            hash += ord(str(char))
        hash = hash % self.max_size
        return hash

    def add_update_item(self, key, value):
        """
        Adds or updates an item if the key already exists
        """
        hash = self.hash_function(key)

        # This adds the item to the cache if there isn't a space already available
        if self.cache[hash] == None:
            self.cache[hash] = node = Node(key, value, self.size)
            self.cache_positions.append(key)
            self.size += 1
            # Checks if the cache is full:
            if self.is_full() == True:
                self._delete_LRU_node() 
        else:
            node = self.cache[hash]
            # If the key already exists update it
            if node.key == key:
                self.update_node(node, key, value)
            else:
                # Go through all the linked nodes to check if the
                # value already exists
                while node.next != None:
                    node = node.next
                    if node.key == key:
                        # Update node if key matches
                        node = self.update_node(node, key, value)
                        return node
                # Add the new item to the end of the other linked items
                node.next = Node(key, value, self.size)
                self.cache_positions.append(key)
                self.size += 1
                # Checks if the cache is full:
                if self.is_full() == True:
                    self._delete_LRU_node() 

        return node

    def is_full(self):
        return self.size > self.max_size


    def _update_node(self, node, key, value=None):
        """
        Updates the node, but can also be used when retrieving value using a key by leaving the value blank
        """
        if value != None:
            node.value = value

        # Update the nodes position in the cache position list
        cache_key = self.cache_positions.pop(node.position)
        node.position = self.size
        self.cache_positions.append(cache_key)

        # Update the positions for the rest of the items
        self._update_positions()
        return node

    def _delete_LRU_node(self):
        """
        Deletes the least recently used node (used means any kind of usage: adding, updating, or retrieving)
        """
        lru_key = self.cache_positions.pop(0)
        hash = self.hash_function(lru_key)
        lru_node = self.cache[hash]

        # Find the correct item within the linked list
        if lru_node.key == lru_key:
            # If there aren't any item linked to this one
            # Then the value can be set to None
            if lru_node.next == None:
                self.cache[hash] = None
            else:
                while lru_node.next != None:
                    if lru_node.next.key == lru_key:
                        lru_node = lru_node.next
                        lru_node.next = lru_node.next.next
                    lru_node = lru_node.next
        else:
            while lru_node.next != None:
                if lru_node.next.key == lru_key:
                    lru_node = lru_node.next
                    lru_node.next = lru_node.next.next
                lru_node = lru_node.next
        
        self.size -= 1
        self._update_positions()
        
    def _update_positions(self):
        """
        Updates the positions after updating, or deleting an item/node
        """
        for indx, key in enumerate(self.cache_positions):

            hash = self.hash_function(key)
            node = self.cache[hash]
            if node.key == key:
                node.position = indx
            else:
                while node.next != None:
                    node = node.next
                    if node.key == key:
                        node.position = indx
                        break

    def retrieve_value(self, key):
        """
        Retrieves a value given a key
        """
        hash = self.hash_function(key)
        node = self.cache[hash]
        if node == None:
            raise KeyError(f"{key} is not contained within the cache.")
        if node.key == key:
            self._update_node(node, key)
            return node.value
        else:
            while node.next != None:
                node = node.next
                if node.key == key:
                    self._update_node(node, key)
                    return node.value
        
        raise KeyError(f"{key} is not contained within the cache.")


    
def example():

    cache = LRUCache(10)
    dogs = [f"dog {x}" for x in range(15)]
    for indx, dog in enumerate(dogs):
        if indx >= 10:
            cache.add_update_item(str(indx), dog)
        else:
            cache.add_update_item(str(indx), dog)
            i = randint(0, indx)
            print(cache.retrieve_value(f'{i}'))


    print(cache.retrieve_value(f'2'))
    


if __name__ == "__main__":
    example()
