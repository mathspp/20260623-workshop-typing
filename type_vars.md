## Exercise 1

```py
class Box:
    def __init__(self, value):
        self.value = value

    def get(self):
        return self.value

int_box = Box(123)
str_box = Box("abc")
reveal_type(int_box.get())  # int
reveal_type(str_box.get())  # str
```

---

## Exercise 2

```py
class Pair:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def swap(self):
        return Pair(self.b, self.a)

    def first(self):
        return self.a

    def second(self):
        return self.b

p = Pair("one", 2)
reveal_type(p.first())  # str
reveal_type(p.second())  # int
reveal_type(p.swap().swap().swap())  # Pair[int, str]
```

---

## Exercise 3

```py
class NoOverridesDict:
    def __init__(self):
        self.store = {}

    def add(self, key, value):
        if key in self.store:
            return
        self.store[key] = value

    def get(self, key):
        return self.store[key]

d = NoOverridesDict()
d.add("one", 1)
reveal_type(d.get("one"))  # int
```

---

## Exercise 4

```py
class Animal:
    ...

class Dog(Animal):
    ...

class AnimalTransporter:
    def __init__(self):
        self.animal = None

    def put(self, animal):
        self.animal = animal

    def remove(self):
        if self.animal is not None:
            animal, self.animal = self.animal, None
            return animal

cage = AnimalTransporter()
cage.put(Dog())
reveal_type(cage.animal)  # Dog
reveal_type(cage.remove())  # Dog

cage.put(3)  # mypy should complain.
```

---

## Exercise 5

```py
class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    @property
    def empty(self):
        return not self.items

stack = Stack()
stack.push(1)
stack.push(2)
reveal_type(stack.pop())  # int
reveal_type(stack.peek())  # int
reveal_type(stack.empty)  # bool
```

---

## Exercise 6

```py
class CallbackRegistry:
    def __init__(self):
        self.callbacks = []

    def register(self, callback):
        self.callbacks.append(callback)

    def trigger(self, value):
        for cb in self.callbacks:
            cb(value)

reg = CallbackRegistry()
reg.register(lambda x: print(f"Got {x}"))
reg.trigger(10)
reg.trigger("oi?")  # mypy should complain.
```

Hint: the relationship has to do with the type of the argument of the method `trigger` and the type of the argument that the functions inside `self.callbacks` expect.

---

## Exercise 7

```py
class History:
    def __init__(self):
        self.items = []

    def add(self, item):
        self.items.append(item)

    def latest(self):
        return self.items[-1]

h = History()
h.add("first")
h.add("second")
reveal_type(h.latest())  # str
```

---

## Exercise 8

```py
from collections import deque

class Queue:
    def __init__(self):
        self.items = self.deque()

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        return self.items.popleft()

    @property
    def empty(self) -> bool:
        return not self.items

queue = Queue()
queue.enqueue(5)
queue.enqueue(10)
reveal_type(queue.dequeue())  # int
```

---

## Exercise 9

```py
class LinkedListNode:
    def __init__(self, value, next_node):
        self.value = value
        self.next_node = next_node

    def safe_next(self):
        assert self.next_node is not None
        return self.next_node

node1 = LinkedListNode(1)
node2 = LinkedListNode(2, node1)
node3 = LinkedListNode(3, node2)
reveal_type(node3.safe_next().safe_next().value)  # int
```