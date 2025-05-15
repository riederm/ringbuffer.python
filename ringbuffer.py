class Ringbuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.buffer = [None] * capacity
        self.start = 0  # Points to the oldest element
        self.end = 0    # Points to the next write position
        self.size = 0

    # Returns the number of elements stored in the ring.
    def get_number_of_elements(self):
        return self.size

    # Add an element to the ringbuffer. If the buffer is full, the oldest element is overwritten.
    def add(self, element):
        self.buffer[self.end] = element
        if self.size == self.capacity:
            # Buffer is full, move start forward (overwrite oldest)
            self.start = (self.start + 1) % self.capacity
        else:
            self.size += 1
        self.end = (self.end + 1) % self.capacity

    # Returns the oldest element in the ringbuffer and removes it from the buffer.
    def remove(self):
        if self.size == 0:
            return None
        element = self.buffer[self.start]
        self.buffer[self.start] = None
        self.start = (self.start + 1) % self.capacity
        self.size -= 1
        return element
