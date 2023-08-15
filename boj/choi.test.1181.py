from dataclasses import dataclass
from typing import Any, Self
from boj.ex1181 import Comparable
from ex1181 import Heap
from unittest import TestCase, main
from random import randint


class CustomComparator(Comparable):
    key: int

    def __init__(self, key=None):
        self.key = key if key else 0

    def __lt__(self, other: Self) -> bool:
        return self.key < other.key


class Test(TestCase):
    MAX_N = 20_000

    def setUp(self) -> None:
        self.heap = Heap(CustomComparator)
        self.ls = [randint(-1000, 1000) for _ in range(self.MAX_N)]
        for e in self.ls:
            self.heap.insert(CustomComparator(e))

    def test_heap_insert(self):
        self.assertEqual(self.MAX_N, len(self.heap))

    def test_heap_pop(self):
        sorted_list = sorted(self.ls)
        for i in range(self.MAX_N):
            self.assertTrue(self.heap.peek())
            self.assertEqual(sorted_list[i], self.heap.peek().key)
            self.heap.pop()
        self.assertIsNone(self.heap.peek())


if __name__ == "__main__":
    main()
