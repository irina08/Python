#!/usr/local/bin/python3
# Creator: Irina Golovko
# Name: ex5.2.py
# DATE: July 10, 2018
# DESC: Class OhNoNotTrueError
# with Custom Exception 


def __main__():
    am_i_true_or_false = [ True, None, False, "True", 0, "", 8, "False", "True", "0.0" ]
    
    for i in range(0, (len(am_i_true_or_false))):
        try:
            test = am_i_true_or_false[i]
            result = TrueOrFalse(test)
            if result == True:
                print("{} is {}.".format(test, result))
            else:
                raise(OhNoNotTrueError("{} is False.".format(test)))
        except OhNoNotTrueError as er:
            print(er)

class OhNoNotTrueError(Exception):
    pass

def TrueOrFalse(var):
    return bool(var)

if __name__ == '__main__':
    __main__()