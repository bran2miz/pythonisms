class Node:
  def __init__(self, data, next=None):
    self.data = data 
    self.next = next

class Stack:

  def __init__(self, values=None):
    self.top = None
    self.size = 0
    if values:
      for item in values:
        self.push(item)

  def push(self, data):
    node = Node(data)
    node.next = self.top
    self.top = node
    self.size += 1

  def isEmpty(self):
    return self.top == None

  def pop(self):
    try:
      temp= self.top
      self.top = self.top.next
      self.size -= 1
      return temp.data
    except: 
      if self.top is None:
       raise Exception('Trying to pop from an empty stack')

  def size(self):
    return self.size

  def peek(self):
    if self.isEmpty():
      raise Exception('Trying to peek from an empty stack')
    return self.top.data

  def __iter__(self):
    def reversed_generator():
      current = self
      while current.top:
        yield current.pop()
    return reversed_generator()

  def __len__(self):
    return len(iter(self))

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
    string = ''
    for value in self:
      string += f'[{value}] -> '
    string += 'None'
    return string

if __name__ == '__main__':

  def generator():
    i = 0
    while True:
      yield i 
      i += 1

  number_generator = generator()

  for j in range(1000000):
    try:
      print(next(number_generator))
    except StopIteration:
      print('All Set')