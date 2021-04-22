class CircularArray:
    def __init__(self, length):
        self.values = [None for _ in range(length)]
        self.max_length = length
        self.head = 0
        self.size = 0
        self.tail = 0

    def insert_front(self, value):
        self.create_new_array_if_overflow()
        self.head = self.head - 1
        if self.head == -1:
            self.head = self.size - 1
        self.values[self.head] = value
        self.size += 1

    def create_new_array_if_overflow(self):
        if self.size == self.max_length:
            self.max_length *= 2
            new_array = [None for _ in range(self.max_length)]
            for i in range(len(self.values) - 1):
                new_array[i] = self.values[(self.head + i) % self.max_length]
            self.values = new_array
            self.head = 0
            self.tail = self.max_length - 1

    def insert_back(self, value):
        self.create_new_array_if_overflow()
        self.tail += 1
        if self.tail == self.max_length:
            self.head = 0
        self.values[self.tail] = value
        self.size += 1
