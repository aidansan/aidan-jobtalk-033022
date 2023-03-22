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

# ["Cream Cheese", "Plain", "Chicken Salad"] 
def print_linked_list(linked_list):
    '''
    Prints the values in the linked list separated by spaces
    '''
    current = linked_list.head
    
    while current is not None:
        print(current, end=' ')
        current = current.next
    print()
    # sli.do: What is the mistake?

l = LinkedList()

print('Adding to linked list')
l.add_front("Chicken Salad")
l.add_front("Plain")
l.add_front("Cream Cheese")
l.add_front("Ham + Egg")

print_linked_list(l)
# Slido: What do we think the first node's value will be?

# print('Removing from linked list')
# l.remove_front()
# print_linked_list(l)

