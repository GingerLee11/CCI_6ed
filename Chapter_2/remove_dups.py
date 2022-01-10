# python3
# remove_dups.py - Remove duplicates from an unsorted linked list.


from collections import deque

def remove_dups(llist):
    """
    Remove duplicates from an unsorted linked list.
    """
    dups = {}
    for elem in llist:
        if elem not in dups:
            dups[elem] = 1
        else:
            dups[elem] += 1
            
    for elem, count in dups.items():
        if count == 1:
            continue
        else:
            while count != 1:
                llist.remove(elem)
                count -= 1
    
    return llist

d = deque('sadlkfnaalsdnvasdfaasdaaffasowaiehaaalsdkjaasdl')

remove_dups(d)