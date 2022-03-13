# python3
# hash_table.py - Hash Table implementation that handles collisisons using a linked list.


class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None


class HashTable:
    def __init__(self):
        self.MAX = 1000
        self.items = [None for i in range(self.MAX)]

    def _gen_hash(self, key):
        if key == None:
            hash = 0
        elif key == '':
            hash = 0 
        elif type(key) == int:
            hash = key
        elif type(key) == bool:
            if key == True:
                hash = 1
            else:
                hash = 0
        elif type(key) == str:
            hash_list = [ord(ch) for ch in key]
            hash = round(sum(hash_list) * hash_list[0])
        elif type(key) == list or type(key) == dict:
            raise KeyError(f"Type {type(key)} is not hashable.")
        
        return hash % self.MAX

    def add_item(self, key, value):
        """
        Add or update item in hash table.
        """
        hash = self._gen_hash(key)
        new_node = Node(key, value)
        if self.items[hash] == None:
            self.items[hash] = new_node
        else:
            node = self.items[hash]
            if node.key == new_node.key:
                node.value = new_node.value
                return node.value
            while node.next != None:
                node = node.next
                if node.key == new_node.key:
                    node.value = new_node.value
                    return node.value
            node.next = new_node
            new_node.prev = node
            return new_node.value
        
    def get_value(self, key):
        """
        Returns a value for a key if it exists in the HashTable.
        """
        hash = self._gen_hash(key)
        if self.items[hash] != None:
            node = self.items[hash]
            if node.key == key:
                return node.value
            while node.next != None:
                node = node.next
                if node.key == key:
                    return node.value

        raise KeyError(f"{key} is not contained within this dictionary.")

    

def example():

    hash_table = HashTable()
    hash_table.add_item('apple', 10)

    for x in range(1, 10001):
        hash_table.add_item(f'apple {x}', x)

    for x in range(1, 10001, 1000):
        hash_table.get_value(f'apple {x}')


if __name__ == "__main__":
    example()
