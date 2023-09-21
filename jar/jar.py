import sys
class Jar:
    def __init__(self, capacity=12):
        if capacity < 0:
            raise ValueError("wrong capacity")
        self._capacity = capacity
        self._size = 0

    def __str__(self):
        return self._size * "🍪"

    def deposit(self, n):
        if n > self._capacity or self._size + n > self._capacity:
             raise ValueError("Exceed Capacity")
        self._size += n

    def withdraw(self, n):
        if self._size < n:
             raise ValueError("There are less cookies than asked to remove")
        self._size -= n

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size


def main():
    jar = jar(4)
    jar.deposit(2)
    jar.withdraw(1)
    print(jar.capacity)
    print(jar.size)