class ListNode:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.first = None

    def append_to(self, node: ListNode, data):
        if not node.next:
            node.next = ListNode(data)
        else:
            self.append_to(node.next, data)

    def append(self, data):
        if not self.first:
            self.first = ListNode(data)
        else:
            self.append_to(self.first, data)

    def length_from(self, node: ListNode) -> int:
        if not node.next:
            return 1
        return self.length_from(node.next) + 1

    def length(self) -> int:
        if not self.first:
            return 0
        return self.length_from(self.first)

    def nth_from(self, node: ListNode, n: int):
        if n == 0:
            return node.data
        return self.nth_from(node.next, n - 1)

    def nth(self, n: int):
        if n < 0 or n >= self.length():
            raise IndexError("Bad linked list index")
        # 0 <= n < self.length()
        return self.nth_from(self.first, n)

    # TODO: Implement remove and remove_from methods
