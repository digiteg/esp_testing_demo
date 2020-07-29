import sys
from datetime import datetime, timedelta

from microtest.microtestrunner import fixture, skip, skipif, xfail, parametrize

@fixture
def input_value():
   input = 39
   return input

@fixture
def input_value2():
   input = 39
   return input


def test_divisible_by_3(input_value,input_value2 ):
   assert input_value % 3 == 0
   assert input_value2 % 3 == 0

def test_divisible_by_6(input_value):
   assert input_value % 6 == 0



#--------------------------------------

@fixture
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
def valid_data():
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
    assert people_data == valid_data()

def test_format_data_for_excel(people_data):
    assert format_data_for_excel(people_data) == """given,family,title Alfonsa,Ruiz,Senior Software Engineer Sayid,Khan,Project Manager"""



#--------SKIP IF----------------------------

@skipif(sys.platform == 'win32',"does not run on windows")
def test_skipif1():
    assert 0                  


#----------XFAIL --------------------------


@skip("hop hop")
def test_hello():
    assert 0, "xfail"

@xfail(False)
def test_hello2():
    assert 0, "xfail 2"


@xfail("hasattr(os, 'sep')")
def test_hello3():
    assert 0

@xfail("bug 110")
def test_hello4():
    assert 0

@xfail('pytest.__version__[0] != "17"')
def test_hello5():
    assert 0

@xfail
def test_hello6():
    assert 0, "reason"

@skip
def test_hello7():
    x = []
    x[1] = 1

#----------PARAMETRIZED --------------------------

testdata = [(datetime(2001, 12, 12), datetime(2001, 12, 11), timedelta(1)),
            (datetime(2001, 12, 11), datetime(2001, 12, 12), timedelta(-1)),
            ]


@parametrize(testdata)
def test_timedistance_v0(a, b, expected):
    diff = a - b
    #print("Test: {} - {} = {}".format(a, b, diff))
    assert diff == expected