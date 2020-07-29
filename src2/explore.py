#from microtest.microtestrunner import MicroTestRunner
import sys
import test_wallet
import test_fibonacci
import test_fixture1

#print (globals())


   
def getmembers(obj, pred=None):
    res = []
    for name in dir(obj):
        val = getattr(obj, name)
        if pred is None or pred(val):
            res.append((name, val))
    res.sort()
    return res

def isfunction(obj):
    return isinstance(obj, type(isfunction))


def getargspec(obj):
    args = []
    varargs= None
    varkw =None
    defaults = None
    return args, varargs, varkw, defaults

def getsourcelines(obj):
    return 0,0

def getall(obj):
    fclass = getattr(obj, '__class__', None)

    name = getattr(obj, '__name__', None)
    code = getattr(obj, '__code__', None)
    defaults = getattr(obj, '__defaults__', None) # Important to use _void ...
    kwdefaults = getattr(obj, '__kwdefaults__', None) # ... and not None here
    annotations = getattr(obj, '__annotations__', None)
    args = getattr(obj, 'args', None)

    print(fclass)
    print(dir(fclass))
    print(dir(fclass.__bases__))
    print(fclass.__bases__.count())
    print(dir(fclass.__bases__.__class__))
    print(name)
    print(code)
    print(defaults)
    print(kwdefaults)
    print(annotations)
    print(args)

def testfunc(vara, varb):
    pass

print(vars(testfunc))


#print()
#print("-----------------")
#print(locals(test_divisible_by_3))
print("-----------------")



"""
try:
    #assert 1>2, "Test false"+"EEE"
    raise Exception('spam', 'eggs')
except AssertionError as err:
    print(err.__class__)
    print(err.args[0])
  #  print(err.__doc__)
    
    print(repr(err))           
except Exception as e:
    print(e.__class__)
    print(e.args)
    print(repr(e))           
                
#mem = getmembers(test_wallet,isfunction)
#getall(mem[0][1])
"""
@property
def test():
    pass

print(type(test))
#test = getmembers(test_divisible_by_3)

#print(mem)
#print("-----------------")
#print(getmembers(test[0][0])))


#if (hasattr(mem[0][0], 'im_func')):
#    print (getmembers.im_func)

#print (getmembers(mem[0]))