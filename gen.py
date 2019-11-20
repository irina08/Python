#!/usr/local/bin/python3

#!/usr/local/bin/python3
# NAME: student Irina Golovko
# FILE: gen.py
# DATE: 02/09/2019
# DESC: Write a generator that yields one absolute 
# file path at a time from access_log 

import re

def absolute_filepath_generator():

    log = '/etc/httpd/logs/access_log'
    
    # For this assignment I decided to stay with POST request because it gives us 
    # a full URL to the file. For example, URL http://hills.ccsf.cc.ca.us/~otangdec/cnit132/addguest.html ,
    # gives us a full path to file: /students/otangdec/public_html/cnit132/addguest.html, 
    # because on hills all files for web should be put in home dir under "public_html" folder.
    # Usually students(under /students/name...) and teachers (under /users/name....) use it.
    # We will assume that only students and teachers cah post request.
    
    # Get element[10] from line in the file 'access_log' if line contains "POST"
    # Remove "" from element[10]: "http://hills...." using [1:-1]: it give us new string 
    # which contains elements from 2 to (last - 1)
    list_url = [line.split(" ")[10][1:-1] for line in open(log) if "POST" in line]
   
    # Convert list to set because set doesn't contain dublicates.
    set_url = set(list_url)
    
    # Create list for teachers. For example, command "ls -la | awk '{ print $9 }'"
    # gives us users name under '/users' dir. 
    teacher = [ 'abornste', 'abrick', 'aclee', 'aghazai', 'amarrs', 'amittal', 
    'amoghtan', 'aochtins', 'arathi', 'asoto', 'awong', 'ballen', 'bbutler', 
    'bcataldo', 'bgeis', 'bstapleton', 'cblair', 'cbrown', 'cclark', 'ccolom', 
    'cconner', 'cdasilva', 'chale', 'chd', 'chhung', 'ckamiya', 'clamha', 'cmetzler', 
    'cpersiko', 'dbass', 'dcox', 'deyeston', 'dfrezzo', 'dharden', 'dhurwich', 
    'dlabrecq', 'dmahalingam', 'doleary', 'dputnam', 'drahman', 'dsgoldma', 
    'dstevens', 'dtaha', 'ebell', 'ecline', 'egentry', 'emorag', 'evargas', 
    'eyoung', 'fko', 'gboyd', 'git', 'grwoo', 'hibrahim', 'hkwok', 'hrabinowitz', 
    'hyip', 'igordon', 'ileiva', 'iwalimun', 'jagonzal', 'jbohan', 'jfield', 'jhong', 
    'jjah', 'jjones', 'jlim', 'jlmaster', 'jorobinson', 'jpotter', 'jrhall', 'jrogers', 
    'jschatz', 'jseckman', 'jskolnic', 'jstrick2', 'jtam', 'jtang', 'jwu', 'kbeyer', 
    'kfreedma', 'lbaca', 'lgiambat', 'lkao', 'lkoffman', 'llannon', 'lmeade', 'lmuniz', 
    'lrosenba', 'lszajko', 'mantonic', 'maxkelly', 'mbeales', 'mbravo', 'mcho', 'mclancy', 
    'mhtam', 'mluttrel', 'mmoore', 'mpetty', 'mpico', 'msieglit', 'natkinso', 'nwebb', 
    'pchytrow', 'plee', 'pthiry', 'pwood', 'ralva', 'rbasra', 'rendres', 'rlam', 
    'rmcateer', 'rnishihi', 'rtaha', 'rwicke', 'sabensoh', 'sbarger', 'sbowne', 'shathawa', 
    'sho', 'sijohnson', 'skahahu', 'slouie', 'smateen', 'smcfarla', 'sraskin', 'srubin', 
    'ssoberan', 'svasudev', 'tboegel', 'tcorbie', 'tharring', 'tjones', 'trauenbu', 
    'tryan', 'unassigned_instructor', 'uwostner', 'wbaptist', 'wfong', 'whong', 'wkaufmyn' ]
        
    # Split every element of set by delimeters: '/', '~', '?' (for elements like 
    # Index.php?login=username in order to get just clean filename)
    # Compare name(element[4]) with elements from 'teacher' list
    # If it's a teacher, use path like /users/name/public_html/......
    # Else we will assume that it's a student, use path like /students/name/public_html/....
    # part 1
    for i in set_url:
        part_url = re.split(r'[/~?]', i)
        filepath = "/students/" + part_url[4] + "/public_html" 
        
        # part2
        if part_url[4] in teacher:
            filepath = "/users/" + part_url[4] + "/public_html"

        # Skip all elements like "login=username" follow by '?'
        # because they are not a part of filepath
        # part 3
        for j in part_url[5:]:
            if "=" not in j:
                filepath = filepath + "/" + j 
            else:
                break

        # Use a yield statement: the state of the function is “saved” from the last call 
        # and can be picked up the next time you call a generator function.
        # Outputs would be like:
        # /students/idubinin/public_html/cnit132/index.html
        # or /users/cdasilva/public_html/cnit132/index.php
        # part 4
        yield filepath
        
        # We can leave filepath like full url. In this case
        # remove list of 'teacher', skip part 1, 2 , 3,
        # rewrite  part 4:
        # for el in ss:
        #   url = re.split(r'[?]', el)
        #   filepath = url[0]
        #   yield filepath
        # Outputs would be like: 
        # http://hills.ccsf.cc.ca.us/~tjones/addguest.html

        # Or we can leave homedir of student or teacher like ~name/
        # In this case we don't need to use any collection of teachers name
        # We need to remove list of 'teacher' and rewrite 'part 1' like:
        # for i in set_url:
            # part_url = re.split(r'[/?]', i)
            # filepath = part_url[4] + "/public_html" 
        # Than skip 'part 2' and follow to 'part 3' and 'part 4'
        # In this case outputs will be like this:
        # ~idubinin/public_html/cnit132/index.html
        

# Each time when you call function absolute_filepath_generator() using next()
# it will give us a new absolute file path. We can only consume all the values 
# of a generator once. When we call next(generator_function) after reaching 
# last element it will give us an error: 
# Traceback (most recent call last): .... StopIteration
abs_filepath = absolute_filepath_generator()
print(next(abs_filepath))
print(next(abs_filepath))
print(next(abs_filepath))
print(next(abs_filepath))
print(next(abs_filepath))


    



