#!/usr/local/bin/python3
# NAME: Irina Golovko
# FILE: lab3.1.py
# DATE: week 3 - June 25 - July 02 2018
# DESC: Using of the palindrome() function

import re

valid_palindromes  = [ "Dennis, Nell, Edna, Leon, Nedra, Anita, \
Rolf, Nora, Alice, Carol, Leo, Jane, Reed, Dena, Dale, Basil, Rae, \
Penny, Lana, Dave, Denny, Lena, Ida, Bernadette, Ben, Ray, Lila, \
Nina, Jo, Ira, Mara, Sara, Mario, Jan, Ina, Lily, Arne, Bette, Dan, \
Reba, Diane, Lynn, Ed, Eva, Dana, Lynne, Pearl, Isabel, Ada, Ned, Dee, \
Rena, Joel, Lora, Cecil, Aaron, Flora, Tina, Arden, Noel, and Ellen sinned.",
"Depardieu, go razz a rogue I draped.",
"Desserts I stressed.",
"Detartrated.",
"Devo met a Mr., eh, DNA and her mate moved.",
"Di as dad said.",
"Did I draw Della too tall, Edward? I did?",
"Dior droid.",
"DNA-land.",
"Do geese see god?",
"Do good? I? No. Evil anon I deliver. I maim nine more hero-men in \
Saginaw, sanitary sword a-tuck, Carol, I. Lo! Rack, cut a drowsy rat \
in Aswan. I gas nine more hero-men in Miami. Reviled, \
I (Nona) live on. I do, O God.",
'"Do nine men interpret?" "Nine men," I nod.'
]

invalid_palindromes =  ["abracadabra!",
"Mister, mister, on a see-saw with your sister.",
"Almost every sentence is NOT a palindrome! How unfair!"]

# Test with not a list
inv = {"abracadabra!",
"Mister, mister, on a see-saw with your sister."}

# palindrome function
def palindrome(string):
    word_characters = re.sub('\W','',string.lower())
    return word_characters.lower() == word_characters[::-1].lower()
    
# more detailed output
# use '\033[1m' and '\033[0m' to print bold text in the
# Linux/Unix console, but keep in mind: in the script 'lab3.1.py' 
# it would be like this: [1m Less detailed outputs: [0m
print('\033[1m' + "More detailed outputs:" + '\033[0m')
for i in [valid_palindromes, invalid_palindromes, inv]:
    if isinstance(i, list):
        for ii in i:
            if palindrome(ii):
                print('"{}"'.format(ii), '\033[1m', "is a palindrome.", \
                '\033[0m')
            else:
                print('"{}"'.format(ii), '\033[1m', "is not a palindrome.", \
                '\033[0m')
    else: 
        print('"{}"'.format(i), '\033[1m', "not a list.", '\033[0m')        
print()

# less detailed output
print('\033[1m', "Less detailed outputs:", '\033[0m')
for i in [valid_palindromes, invalid_palindromes, inv]:
    if isinstance(i, list):
        for ii in i:
            print(palindrome(ii))
    else: 
        print('"{}"'.format(i), "not a list.")