class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def has_loop(head):
    slow = head
    fast = head

    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            return True
    
    return False

def create_linked_list_with_loop():
    nodes = []
    num_nodes = int(input("Enter the number of nodes: "))
    
    for i in range(num_nodes):
        data = int(input(f"Enter data for node {i + 1}: "))
        nodes.append(Node(data))
    
    for i in range(num_nodes - 1):
        nodes[i].next = nodes[i + 1]
    
    create_loop = input("Do you want to create a loop? (yes/no): ").strip().lower()
    if create_loop == 'yes':
        loop_node_index = int(input(f"Enter the index (0 to {num_nodes - 1}) of the node where the loop should start: "))
        nodes[-1].next = nodes[loop_node_index]
    
    return nodes[0] if nodes else None

# Create linked list with user input
head = create_linked_list_with_loop()

# Check for loop
if has_loop(head):
    print("The linked list has a loop.")
else:
    print("The linked list does not have a loop.")
