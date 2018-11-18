#!/usr/local/bin/python3
# NAME: Irina Golovko
# FILE: count_words.py
# DATE: June 27, 2018
# DESC: count the words in a string. 
# Words are strings of word characters 
# matching the regular expression \w.

def ______function_______(string):
    import re
    tmp = {}
    # Simple regex splits on non-word characters
    words = re.split('\W+',string.lower())

    # Regex to split on word boundaries
    # words = re.split(r"\b[a-zA-Z'-]+\b", string.lower())
    
    for word in words:
        if word in tmp:
            tmp[word] += 1
        else:
            tmp[word] = 1
    return tmp


test_me = """cried his the as a one under first \
established wall and For bitterly eyes he the of \
had and the in from its and one tried appears by \
to in which their himself however once express given \
dark hands ages end and his hands paupers the the \
himself impious To surface in he It assembled all of \
a by crouching to prediction came even was handkerchief \
close and suppose on order out the to waking waistcoat \
impious to seals hard There profane anon the when \
himself other character the to the There dismal prophetic \
He still by closer prophetic room he and and individual been \
luxury ever and of the and articles was commission that of \
and loneliness before of times under to gentleman for \
character profane of more in s tried the corner future \
decided solitary s in namely the week close his pocket by \
for little tremble the after and to once the of and this wall \
pocket Oliver and been if that in To protection from assembled \
Oliver the of council sleep little appears of and closer \
individual solemnly on solitary first s if hook a corner when \
start for drawing of prediction and sage board sleep to not of \
a a of surface in the week solemnly unreasonable if darkness the \
with one pronounced childishness if even sight obstacle all feat \
waistcoat the in to dismal had gloom Oliver articles for surrounded \
a paupers being bitterly offence the spread at shut a handkerchiefs \
order crouching the himself for tying suppose board in youth and of \
ever unreasonable had end long to sight one hands noses at feel only \
respect room respect all a he start for closer were offence day prisoner \
obstacle to board and and a in in wall he waking For a white the a becoming \
noses handkerchiefs consigned its entertained mercy have and feeling and \
that established and and long to pocket gentleman wisdom given remained \
he more to mercy ever namely shut came there a gloom the their of which \
his the in entertained obstacle times and seals future s of being hands \
express performance of by It had performance commission hard to other and \
the the would white and all as of He ever tremble drawing board the removed \
of night council feel greater wisdom asking for and after in a feeling luxury \
prisoner handkerchief and have cried remained not and by attaching cold the had \
the before the had anon which and pronounced the greater was obstacle only to \
there ages with his wall was the dark would however this been for that the the \
loneliness of to and a been his still removed Oliver night protection hook tying \
childishness pocket of the asking that day him surrounded in were him attaching \
sage youth feat becoming and and eyes the which darkness closer out cold that \
the decided the the  consigned spread"""

print(______function_______(test_me))




