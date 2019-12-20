from doubly_linked_list import DoublyLinkedList
from queue import Queue

class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.size = 0
        self.queue = Queue()
        self.storage = DoublyLinkedList()

    def append(self, item):
        if self.size == self.capacity:
            popped = self.queue.dequeue() # get val out of queue
            print('popped', popped)
            value = self.storage.head
            print('value', value.value)
            while value is not None:
                if value.value == popped:
                    value.value = item
                value = value.next
            self.queue.enqueue(item)
        if self.size < self.capacity:
            self.size += 1
            self.queue.enqueue(item)
            return self.storage.add_to_tail(item)
            

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []

        # TODO: Your code here
        node = self.storage.head
        while node is not None:
            list_buffer_contents.append(node.value)
            node = node.next

        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
