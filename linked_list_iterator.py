class LinkedList:

#     ["apple","banana","cucumber"]
# 1st cucumber

# ['apple'] -> ['banannana'] - > ['cucumber'] -> None

    def __init__(self, collection=None):
        self.head = None
        if collection:
            for item in reversed(collection):
                self.insert(item)

    # ['apple'] -> ['banannana'] - > ['cucumber'] -> None
    def __iter__(self):
        def value_generator():
            current = self.head
            while current:
                yield current.value
                current = current.next
        return value_generator()
# return the entire item
# object has no length 

    def __len__(self):
        return len(list(iter(self)))
# converts from an object from value generator() to a list
# overwriting own length in LL class but utilizing the length of a list object which has its own objects.

    def __eq__(self, other):
        return list(self) == list(other)

    def __getitem__(self, index):
        if index < 0:
            raise IndexError
        for i, item in enumerate(self):
            if i == index:
                return item
        raise IndexError

    def __str__(self):
        out = ''
        for value in self:
            out += f'[ {value } ] -> '
        out += 'None'
        return out

    def insert(self, value):
        self.head = Node(value, self.head)

    def append(self, value):
        node = Node(value)
        if not self.head:
            self.head = node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = node

class Node:
    def __init__(self, value, next_ = None):
        self.value = value
        self.next = next_


if __name__ == "__main__":

    # def gen():
    #     for i in range(10):
    #         yield i

    def gen():
        i = 0
        while True:
            yield i
            i += 1

    numb_gen = gen()

    # print(numb_gen)
    for j in range(10000):
        try:
            print(next(numb_gen))
        except StopIteration:
            print('We are all done!')

class Stack:

  def __init__(self, collection=None):
    self.top = None
    self.size = 0
    if collection:
      for thing in reversed(collection):
        self.push(thing)

  def push(self, value):
    new_node = Node(value)
    new_node.next = self.top
    self.top = new_node
    self.size += 1

  def pop(self):
    try:
      temp = self.top
      self.top = self.top.next
      self.size -= 1
      return temp.value
    except:
      if self.top == None:
        return Exception

  def peek(self):
    try:
      return self.top.value
    except:
      if self.top.value == None:
        return Exception

  def is_empty(self):
    return self.size == 0
  
  def __iter__(self):
    def value_generator():
      current = self
      while current.top:
        yield current.pop()
    return value_generator()
  
  def __len__(self):
    return len(iter(self))
  
  def __str__(self):
        out = ''
        for value in self:
            out += f'[ {value } ] -> '
        out += 'None'
        return out
  
  def __eq__(self, other):
    return list(self) == list(other)

  def __getitem__(self, index):
    if index < 0:
      raise IndexError
    for i, item in enumerate(self):
      if i == index:
        return item
      raise IndexError


if __name__ == "__main__":

    # def gen():
    #     for i in range(10):
    #         yield i

    def gen():
        i = 0
        while True:
            yield i
            i += 1

    numb_gen = gen()

    # print(numb_gen)
    for j in range(10000):
        try:
            print(next(numb_gen))
        except StopIteration:
            print('We are all done!')