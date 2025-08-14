from main import add

def test_add():
    assert add(3,4)==7

def test_add1():
    assert add(-3,-5)==-8

def test_add2():
    assert add(0,0)==0