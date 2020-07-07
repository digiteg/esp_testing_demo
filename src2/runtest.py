
import microtest

import test_wallet
import test_fibonacci



def get_test_modules():
    modlist =  globals()

    test_sets = set()
    position = 0
 # retrive name obj of functions
    for module_name, obj in modlist.items():
        if module_name.startswith('test_'):  # function starts with test_
           position +=1  # add number
           test_sets.add((position, module_name,obj))   # create touple list

    return sorted(test_sets)

# test runner is a component that organizes the execution of tests and provides the result to the user.
def exec_runer():
    modlist = get_test_modules()
    
    runner = microtest.Microtest()
    
    for pos, module_name,obj in modlist:
        runner.run_test_suite(obj, True, False)




def main():
    exec_runer()


if __name__ == "__main__":
    main()
