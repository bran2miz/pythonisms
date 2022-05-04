
from stack_iterator import Stack, Node

import pytest

def test_for_in():
    # ['apple'] -> ['banannana'] - > ['cucumber'] -> None
    foods = Stack(("apple","banana","cucumber"))
    foods_list = [] # ['apple', 'banannana', 'cucumber']
    for food in foods:
        foods_list.append(food)
    assert foods_list == ["cucumber","banana","apple"]

# @pytest.mark.skip("pending")
def test_list_comprehension():
    foods = Stack(("apple","banana","cucumber"))
    cap_foods = [food.upper() for food in foods]
    assert cap_foods == ["CUCUMBER","BANANA","APPLE"]

# @pytest.mark.skip("pending")
def test_list_cast():
    food_list = ["apple","banana","cucumber"]
    foods = Stack(food_list)
    test_list = ['cucumber', 'banana', 'apple']
    assert list(foods) == test_list

# @pytest.mark.skip("pending")
def test_range():
    num_range = range(1,20+1)
    nums = Stack(num_range)
    assert len(list(nums)) == 20

# @pytest.mark.skip("pending")
def test_filter():
    nums = Stack(range(1,21))
    odds = [num for num in nums if num % 2]
    assert odds == [19,17,15,13,11,9,7,5,3,1]

# @pytest.mark.skip("pending")
def test_next():
    foods = Stack(["apple","banana","cucumber"])
    iterator = iter(foods)
    assert next(iterator) == "cucumber"
    assert next(iterator) == "banana"
    assert next(iterator) == "apple"

# @pytest.mark.skip("pending")
def test_stop_iteration():
    foods = Stack(["apple","banana","cucumber"])
    iterator = iter(foods)
    with pytest.raises(StopIteration):
        while True:
            food = next(iterator)

# @pytest.mark.skip("pending")
def test_str():
    foods = Stack(["apple","banana","cucumber"])
    assert str(foods) == "[cucumber] -> [banana] -> [apple] -> None"

# dunder method tests

# @pytest.mark.skip("pending")
def test_equals():
    lla = Stack(["apple","banana","cucumber"])
    llb = Stack(["apple","banana","cucumber"])
    assert lla == llb

# @pytest.mark.skip("pending")
def test_get_item():
    foods = Stack(["apple","banana","cucumber"])
    assert foods[0] == "cucumber"

# @pytest.mark.skip("pending")
def test_get_item_out_of_range():
    foods = Stack(["apple","banana","cucumber"])
    with pytest.raises(IndexError):
        foods[100]

def test_node_instance():
    node = Node(1,None)
    assert node.next == None
    assert node.data == 1

#Test One Push onto a stack
def test_stack_push_one():
    stack = Stack()
    stack.push('1')
    assert stack.top.data == '1'

def test_stack_push_one_wrong():
    stack = Stack()
    stack.push('2')
    assert stack.top.data != '3'
#Test 2 Push multiple datas onto a stack
def test_stack_push_multiple():
    stack = Stack()
    stack.push('2')
    stack.push('4')
    stack.push('6')
    assert stack.top.data == '6'

def test_stack_push_multiple_wrong():
    stack = Stack()
    stack.push('2')
    stack.push('4')
    stack.push('6')
    assert stack.top.data != '2'
#Test 3 pop off stack
def test_stack_pop_one():
    stack = Stack()
    stack.push('2')
    stack.push('4')
    stack.push('6')
    stack.pop()
    assert stack.top.data == '4'

def test_stack_pop_one_wrong():
    stack = Stack()
    stack.push('2')
    stack.push('4')
    stack.push('6')
    stack.pop()
    assert stack.top.data != '6'
#Test 4 empty a stack after multiple pops
def test_stack_pop_all():
    stack = Stack()
    stack.push('2')
    stack.push('4')
    stack.push('6')
    stack.pop()
    stack.pop()
    stack.pop()
    assert stack.top == None

def test_stack_pop_all_wrong():
    stack = Stack()
    stack.push('2')
    stack.push('4')
    stack.push('6')
    stack.pop()
    stack.pop()
    stack.pop()
    assert stack.top != '6'

#Test 5 Peek the next item on a stack
def test_peek_stack():
    stack = Stack()
    stack.push('2')
    assert stack.peek() == '2'

# @pytest.mark.skip('Pending')
def test_peek_stack_not_working():
    stack = Stack()
    stack.push('2')
    assert stack.peek() != '3'

#Test 6 instantiate an empty stack
def test_empty_stack():
    stack = Stack()
    actual = stack.isEmpty()
    expected = True
    assert actual == expected

def test_empty_stack_not_working():
    stack = Stack()
    stack.push('2')
    actual = stack.isEmpty()
    expected = True
    assert actual != expected

#Test 7 Calling pop or peek on empty stack raises exception
def test_peek_exception():
    with pytest.raises(Exception):
        stack = Stack()
        stack.peek()

def test_pop_exception():
    with pytest.raises(Exception):
        stack = Stack()
        stack.pop()