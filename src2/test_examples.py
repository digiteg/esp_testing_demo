import sys
import timeit
from fixtures import my_dec




@noparam
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

@property
def data():
    print("property run")
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

@data.setter
def data(val):
    pass

# ------------------------

def format_data_for_display(data):
    return [ "Alfonsa Ruiz: Senior Software Engineer", "Sayid Khan: Project Manager"]

def format_data_for_excel(data):
    return  """given,family,title Alfonsa,Ruiz,Senior Software Engineer Sayid,Khan,Project Manager"""

def say_whee(vdata):
    print("Whee!")
    print(vdata)


def func():
    pass

execution_time = timeit.timeit(func, number=1)
print(execution_time)


# ------------------------

def test_uppercase():
    assert "loud noises".upper() == "LOUD NOISES"


def test_reversed():
    assert list(reversed([1, 2, 3, 4])) == [4, 3, 2, 1]


def test_some_primes():
    assert 37 in {
        num
        for num in range(1, 50)
        if num != 1 and not any([num % div == 0 for div in range(2, num)])
    }


def test_format_data_for_display(people_data):
    assert format_data_for_display(people_data) == [ "Alfonsa Ruiz: Senior Software Engineer", "Sayid Khan: Project Manager"]

def test_format_data_for_excel(people_data):
    assert format_data_for_excel(people_data) == """given,family,title Alfonsa,Ruiz,Senior Software Engineer Sayid,Khan,Project Manager"""


def test_fail():
    assert 1 == 2

def test_error():
    1/0


print(data)
#@people_data
test_format_data_for_display(data)

# @people_data
# test_format_data_for_display(people_data)

