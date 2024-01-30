class Node:
    """Класс для узла очереди"""

    def __init__(self, data=None, next_node=None):
        """
        Конструктор класса Node

        :param data: данные, которые будут храниться в узле
        """
        self.data = data
        self.next_node = next_node


class Queue:
    """Класс для очереди"""

    def __init__(self):
        """Конструктор класса Queue"""
        self.head = None
        self.tail = None

    def enqueue(self, data):
        """
        Метод для добавления элемента в очередь

        :param data: данные, которые будут добавлены в очередь
        """
        new_data = Node(data)
        if self.head is None:
            self.head = new_data
            self.tail = self.head
        else:
            self.tail.next_node = new_data
            self.tail = new_data

    def dequeue(self):
        """
        Метод для удаления элемента из очереди. Возвращает данные удаленного элемента

        :return: данные удаленного элемента
        """
        if self.head is None:
            return None
        else:
            node = self.head
            self.head = node.next_node
            return node.data

    def __str__(self):
        """Магический метод для строкового представления объекта"""
        if self.head is None:
            return ""
        else:
            nodes = []
            node = self.head
            while node:
                nodes.append(str(node.data))
                node = node.next_node
            return '\n'.join(nodes)