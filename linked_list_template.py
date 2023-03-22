class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    # ["Cream Cheese", "Plain", "Chicken Salad"] -> ["Ham + Egg", "Cream Cheese", "Plain", "Chicken Salad"]
    def add_front(self, val):
        '''
        Adds a new list node to the front of the linked list
        '''
        # Make a new list node with the given value
        # Update the new node's "next"
        # Sli.do: What do we do next?

    # ["Ham + Egg", "Cream Cheese", "Plain", "Chicken Salad"] -> ["Cream Cheese", "Plain", "Chicken Salad"]
    def remove_front(self):
        '''
        Removes the list node from the front of the linked list, will throw an error if list is empty
        '''

def print_linked_list(linked_list):
    '''
    Prints the values in the linked list separated by spaces
    '''
    current = linked_list.head
    
    while current is not None:
        print(current.val, end=' ')
        current = current.next
    print()

def sum_linked_list(linked_list):
    '''
    Adds together all of the elements in the linked list
    '''

    # Sli.do: What variables do we need to set up / make?

    # Keep going until we reach the end

    # Add to our sum
    # Move to the next node
    return -1
    

l = LinkedList()

print('Adding 3, 6, 2, 5 to linked list')
l.add_front(3)
l.add_front(6)
l.add_front(2)
l.add_front(5)

print_linked_list(l)
# Slido: What do we think the first node's value will be?

# print('Removing from linked list')
# l.remove_front()
# print_linked_list(l)


# print('Sum of the linked list')
# print(sum_linked_list(l))
