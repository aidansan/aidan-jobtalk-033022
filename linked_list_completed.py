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
        new_node = ListNode(val)
        # Update the new node's "next"
        new_node.next = self.head
        # Sli.do: What do we do next?
        self.head = new_node

    # ["Ham + Egg", "Cream Cheese", "Plain", "Chicken Salad"] -> ["Cream Cheese", "Plain", "Chicken Salad"]
    def remove_front(self):
        '''
        Removes the list node from the front of the linked list, will throw an error if list is empty
        '''
        self.head = self.head.next

# ["Cream Cheese", "Plain", "Chicken Salad"] 
def print_linked_list(linked_list):
    '''
    Prints the values in the linked list separated by commas
    '''
    # Make a reference to the start of the linked list
    current = linked_list.head
    
    # Keep going until we reach the end of the list
    while current is not None:
        # Print out current value
        print(current.val, end=', ')
        # Make sure to move to the next node
        current = current.next
    print()
    # sli.do: What is the mistake? forgetting to access val

def sum_linked_list(linked_list):
    # Setup variables
    current = linked_list.head
    s = 0
    # Keep going until the end of the list
    while current is not None:
        # Adding to our sum
        s += current.val
        # Moving to the next node
        current = current.next
    return s
    # What is the mistake in the code? infinite loop

def main():
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

    l2 = LinkedList()
    l2.add_front(5)
    l2.add_front(3)
    l2.add_front(7)
    print(sum_linked_list(l2))
if __name__ == '__main__':
    main()
