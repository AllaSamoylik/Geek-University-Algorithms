# Разбор алгоритма Хаффмана

import heapq
from collections import Counter
from collections import namedtuple


# Описываются узлы, у которых будут другие узлы
class Node(namedtuple("Node", ["left", "right"])):
    def walk(self, code, acc):
        # Рекурсивный обход дерева по узлам до листов с расстановкой 0/1 у левых/правых ветвей
        self.left.walk(code, acc + "0")
        self.right.walk(code, acc + "1")


# Описываются листья, в которых будут символы (узлов нет)
class Leaf(namedtuple("Leaf", ["char"])):
    # Выдача окончательного кода из нулей/единиц для листа с символом после обхода ветвей к нему
    def walk(self, code, acc):
        code[self.char] = acc or "0"


def huffman_encode(s):
    h = []
    # В тексте подсчитываются символы и раставляются в список по частоте упоминания со сквозной нумерацией
    for ch, freq in Counter(s).items():
        h.append((freq, len(h), Leaf(ch)))

    # Список преобразовывается в кучу
    heapq.heapify(h)
    count = len(h)
    # Достаются 2 листа с самыми редкими символами, добавляются сюда же, образуя новый узел с двумя узлами.
    # Частоты складываются и сохраняются в новом узле, в соответствии с новым значением
    # определяется место для вставки узла.
    # Сквозная нумерация продолжается, также записывается в узел.
    # Повторяем изымание/объединение/добавление, пока все узлы не соберутся в один узел-корень.
    while len(h) > 1:
        freq1, _count1, left = heapq.heappop(h)
        freq2, _count2, right = heapq.heappop(h)
        heapq.heappush(h, (freq1 + freq2, count, Node(left, right)))
        count += 1

    # Обходим дерево со сбором нулей и единиц по всем ветвям к каждому листу-символу.
    # Единственный собранный узел-корень отдаём как точку отсчета для рекурсии.
    code = {}
    if h:
        [(_freq, _count, root)] = h
        root.walk(code, "")
    return code


for val in huffman_encode('all the best!').values():
    print(val, end=' ')
