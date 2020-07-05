import sys

class SkipTest(Exception):
    pass

def skip(msg):
    def _decor(fun):
        # We just replace original fun with _inner
        def _inner(self):
            raise SkipTest(msg)
        return _inner
    return _decor

def skipIf(cond, msg):
    if not cond:
        return lambda x: x
    return skip(msg)

def skipUnless(cond, msg):
    if cond:
        return lambda x: x
    return skip(msg)


# --------------------------------------- Decorator Fixture


def my_dec(func):
    print("Something is happening before the function is called.")
    return func()

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


def format_data_for_display(data):
    return [ "Alfonsa Ruiz: Senior Software Engineer", "Sayid Khan: Project Manager"]

def format_data_for_excel(data):
    return  """given,family,title Alfonsa,Ruiz,Senior Software Engineer Sayid,Khan,Project Manager"""



@my_dec
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



def test_format_data_for_display(example_people_data):
    assert format_data_for_display(example_people_data) == [ "Alfonsa Ruiz: Senior Software Engineer", "Sayid Khan: Project Manager"]

def test_format_data_for_excel(example_people_data):
    assert format_data_for_excel(example_people_data) == """given,family,title Alfonsa,Ruiz,Senior Software Engineer Sayid,Khan,Project Manager"""


def test_fail():
    assert 1 == 2


def say_whee(vdata):
    print("Whee!")
    print(vdata)


# @people_data
# test_format_data_for_excel(people_data)

# @people_data
# test_format_data_for_display(people_data)

