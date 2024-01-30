"""Здесь надо написать тесты с использованием unittest для модуля queue."""
import unittest
from src.queue import Queue


class TestQueueClass(unittest.TestCase):
    """Тестовый класс для тестирования Очереди"""

    def setUp(self):
        self.queue = Queue()

    def test__init__(self):
        """Тест конструктора класса Очереди"""
        self.assertEqual(self.queue.head, None)
        self.assertEqual(self.queue.tail, None)

    def test__str__(self):
        """Тестируем маг. метод str"""
        self.assertEqual(self.queue.__str__(), "")
        self.queue.enqueue('data1')
        self.queue.enqueue('data2')
        self.queue.enqueue('data3')
        self.assertEqual(self.queue.__str__(), "data1\ndata2\ndata3")

    def test_enqueue(self):
        """Тестируем метод enqueue класса Очереди"""
        self.queue.enqueue('data1')
        self.assertEqual(self.queue.head.data, 'data1')
        self.queue.enqueue('data2')
        self.assertEqual(self.queue.head.next_node.data, 'data2')
        self.queue.enqueue('data3')
        self.assertEqual(self.queue.tail.data, 'data3')
        self.assertEqual(self.queue.tail.next_node, None)

    def test_dequeue(self):
        """Тестируем метод dequeue класса Очереди"""
        self.queue.enqueue('data1')
        self.queue.enqueue('data2')
        self.queue.enqueue('data3')
        self.assertEqual(self.queue.dequeue(), 'data1')
        self.assertEqual(self.queue.dequeue(), 'data2')
        self.assertEqual(self.queue.dequeue(), 'data3')
        self.assertEqual(self.queue.dequeue(), None)