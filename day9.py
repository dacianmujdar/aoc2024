from collections import deque


class CustomQueue:
    """
    Custom queue that gets value in form of (value, frequency). The API allows individuals pop, pop_left of the value
    takes care of the frequency internally.
    """
    def __init__(self, q):
        self.q = q
        self.remainder_nr_left = 0
        self.remainder_value_left = 0
        self.remainder_nr_right = 0
        self.remainder_value_right = 0

    def pop_left(self):
        if self.remainder_nr_left:
            self.remainder_nr_left -= 1
            return self.remainder_value_left
        if not self.q:
            # If there are leftovers in right, use that
            if self.remainder_nr_right:
                self.remainder_nr_right -= 1
                return self.remainder_value_right
            return 0
        self.remainder_value_left, self.remainder_nr_left = self.q.popleft()

        self.remainder_nr_left -= 1
        return self.remainder_value_left

    def pop_right(self):
        if self.remainder_nr_right:
            self.remainder_nr_right -= 1
            return self.remainder_value_right
        if not self.q:
            return 0
        self.remainder_value_right, self.remainder_nr_right = self.q.pop()

        self.remainder_nr_right -= 1
        return self.remainder_value_right

    def empty(self):
        return not self.q and not self.remainder_nr_right and not self.remainder_nr_left


if __name__ == '__main__':
    with open("./input/day9.txt", "r") as f:
        text = f.read().strip()

    q = CustomQueue(deque())
    for i in range(0, len(text), 2):
        id = int(i/2)
        # We put in queue (value, frequency)
        q.q.append((id, int(text[i])))

    index = 0
    total = 0
    i = 0

    result = []
    while not q.empty():
        nr = int(text[i])
        pop_op = q.pop_left if i % 2 == 0 else q.pop_right
        end_index = index + nr
        while index < end_index and not q.empty():
            total += index * pop_op()
            index += 1
        i += 1

    print(total)
