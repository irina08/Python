#!/usr/local/bin/python3

#!/usr/local/bin/python3
# NAME: student Irina Golovko
# FILE: decor.py
# DATE: 03/17/2019
# DESC: Decorate print() such that 
# (A) it refuses to print anything 
# under ten characters long and 
# (B) only five calls are allowed, 
# and demonstrate these restrictions 
# when the program is run


import functools 

# count how many times a function is called
call_count = 0

def my_dec(func):    
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
# Use keyword 'global' inside function because 
# we need to modify gloval 'call_count' variable 
# from inside the function too.        
        global call_count
        while call_count < 5:
            call_count += 1
            print("Number of calls: ", call_count)
            print ("Arguments with length more than 10 "
            + "characters passed to function:")
            return func(*args, **kwargs)       
    return wrapper 


# arguments are strings. If not a string it will 
# convert to string. If length of passed argument 
# more than 10 characters function will print 
# nothing, else - it will print the passed argument. 
@my_dec
def print_args(*args):
    for arg in args:
        if (type(arg) == str and len(arg) > 10):
            print (arg)
        elif (type(arg) != str):
            arg = str(arg)
            if len(arg) > 10:
                print (arg)
        else:
            pass

# Call function print_args() more than 5 times
# Call 1: Will print next args: truetruetrue 
# horoscope1090 horohorohorohoro
print_args("ten", "truetruetrue", 
    "horoscope1090", "true", "horohorohorohoro")
print()

# Call 2: Will print arg: tentententen
print_args("tentententen")
print()

# Call 3: Nothing to print
print_args()
print()

# Call 4: Nothing to print
print_args("Hello Tim", 1)
print()

# Call 5: Will print args: Hello Tim, Tom, Dan.
# 123456789.5678 1111111111111111
print_args("Hello Tim, Tom, Dan.", "Hello", 
    123456789.5678, 1111111111111111)
print() 

# Call 6: Even though it suppose to print arg, 
# it will print nothing because we will call 
# function 6 times
print_args("Hello Everyone")

# Call 7
print_args("tentententen")
