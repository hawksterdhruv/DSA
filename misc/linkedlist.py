head = None


class Node:
    def __init__(self, data):
        # print(f"node created {data}")
        self.data = data
        self.next = None


# def new_node(data):
# return None(data)

# def iterate(head):
#     current = head
#     while current:
#         print(current.data)
#         current=current.next


# def get_tail(head):
#     current = head
#     if not current:
#         return None
#     else:
#         while current.next:
#             current = current.next

#         return current


def insert(data):
    global head
    new_node = Node(data)
    # current = head
    if head is None:
        # print("head")
        head = new_node
        return head
    else:
        # print("else")
        current = head
        while current.next:
            current = current.next
        current.next = new_node
        return head


if __name__ == "__main__":
    for i in range(10):
        insert(i)

    current = head
    while current:
        print(current.data)
        current = current.next
