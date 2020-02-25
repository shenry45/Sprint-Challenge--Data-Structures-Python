from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()


    def append(self, item):
        # Head is oldest, Tail is newest
        # if storage is error or None
        if self.storage.length < 0 or item is None:
            return

        # storage is less than limit
        elif self.storage.length < self.capacity:
            self.storage.add_to_tail(item)
            # first item is set to oldest
            if self.storage.length == 1:
                self.current = self.storage.tail

        # storage is at limit, replace oldest
        else:
            # start at head, check next item
            if self.current.next:

                next_node = self.current.next

                # add new node to list
                self.storage.add_to_tail(item)

                if self.current == self.storage.head:
                    # move tail to head
                    self.storage.move_to_front(self.storage.tail)
                else:
                    # move to current node next
                    self.current.insert_before(self.storage.tail.value)
                    self.storage.length += 1
                    # delete tail
                    self.storage.delete(self.storage.tail)

                # delete current node
                self.storage.delete(self.current)

                # update current
                self.current = next_node

            # at the end of list
            else:
                # adds new node to list
                self.storage.add_to_tail(item)
                # delete current node
                self.storage.delete(self.current)
                # update current
                self.current = self.storage.head


    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []

        def looper(node):
            # add node to list_buffer_contents
            list_buffer_contents.append(node.value)

            if node.next:
                return looper(node.next)
            else:
                return

        looper(self.storage.head)

        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
