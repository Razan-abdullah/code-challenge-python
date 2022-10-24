# Write your test here
import pytest
from http.client import ACCEPTED
from os import link
from challenge01 import *

@pytest.fixture
def linkedList2():
    
    linked= LinkedList()
    
    linked.add_new_node(10)
    
    linked.add_new_node(20)
   
    actual=linked.print()
     
    expected =[10,20]
    assert actual == expected,"Errore"
     
    

# @pytest.fixture
# def linkedList3():
#     linked = LinkedList()
#     linked.append(4)
#     linked.append(5)
#     linked.append(1)
#     linked.append(9)
#     delete (linked.head.next.next)
#     return ll.printAll()

# def test_delete(linkedList2):
#     actual = linkedList2
#     expected = [4,1,9]
#     assert actual == expected

# def test_delete_1(linkedList3):
#     actual = linkedList3
#     expected =[4,5,9]
#     assert actual == expected