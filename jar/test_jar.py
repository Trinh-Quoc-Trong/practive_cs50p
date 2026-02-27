from jar import Jar

import pytest

def test_init():
    jar_1 = Jar()
    assert jar_1.capacity == 12
    jar_1._capacity = 1
    assert jar_1.capacity == 1
    with pytest.raises(ValueError):
        jar_3 = Jar(-1)
    
def test_str():
    jar_2 = Jar()
    assert jar_2.__str__() == ""
    jar_3 = Jar(5)
    jar_3.deposit(2)
    assert jar_3.__str__() == "🍪🍪"
    jar_4 = Jar(11)
    jar_4.deposit(10)
    assert jar_4.__str__() == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"

def test_deposit():
    jar = Jar(10)
    jar.deposit(2)
    assert jar.size == 2
    
    # Test nhét quá sức chứa
    with pytest.raises(ValueError):
        jar.deposit(100)

def test_withdraw():
    jar = Jar(10)
    jar.deposit(5)
    jar.withdraw(2)
    assert jar.size == 3
    
    # Test lấy nhiều hơn số bánh đang có
    with pytest.raises(ValueError):
        jar.withdraw(10)

test_init()