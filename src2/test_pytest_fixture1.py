import sys
import pytest

@pytest.fixture
def input_value():
   input = 39
   return input


def test_divisible_by_3(input_value):
   assert input_value % 3 == 0

def test_divisible_by_6(input_value):
   assert input_value % 6 == 0


#--------------------------------------

@pytest.fixture
def people_data():
    return [
        {
            "given_name": "Alfonsa",
            "family_name": "Ruiz",
            "title": "Senior Software Engineer",
        },
        {
            "given_name": "Sayid",
            "family_name": "Khan",
            "title": "Project Manager",
        }
    ]

# Dummy formater
def format_data_for_display(data):
     return [
        {
            "given_name": "Alfonsa",
            "family_name": "Ruiz",
            "title": "Senior Software Engineer",
        },
        {
            "given_name": "Sayid",
            "family_name": "Khan",
            "title": "Project Manager",
        }
    ]

def format_data_for_excel(data):
    return  """given,family,title Alfonsa,Ruiz,Senior Software Engineer Sayid,Khan,Project Manager"""

# test data format
def test_format_data_for_display(people_data):
    assert format_data_for_display(people_data) == people_data

def test_format_data_for_excel(people_data):
    assert format_data_for_excel(people_data) == """given,family,title Alfonsa,Ruiz,Senior Software Engineer Sayid,Khan,Project Manager"""



#--------SKIP IF----------------------------

@pytest.mark.skipif(sys.platform == 'win32',
                    reason="does not run on windows")
def test_skipif1():
    assert 0                  


#----------XFAIL --------------------------

xfail = pytest.mark.xfail

@xfail
def test_hello():
    assert 0

@xfail(run=False)
def test_hello2():
    assert 0

@xfail("hasattr(os, 'sep')")
def test_hello3():
    assert 0

@xfail(reason="bug 110")
def test_hello4():
    assert 0

@xfail('pytest.__version__[0] != "17"')
def test_hello5():
    assert 0

def test_hello6():
    pytest.xfail("reason")

@xfail(raises=IndexError)
def test_hello7():
    x = []
    x[1] = 1