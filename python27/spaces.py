#!/usr/bin/python

# Python 3 example

import re

def spaces(thestr):
    ''' Count the number of spaces '''
    return len(thestr.split(' ')) - 1

if __name__ == '__main__':
#def main():
    thestr = (input("Enter a String: ")).strip()
    print(str(thestr))
    print("The number of spaces is: ", spaces(str(thestr)))
    
    no_multi_spaces = re.sub(" +", " ",thestr)
    print(str(no_multi_spaces))
    print("The number of spaces is: ", spaces(str(no_multi_spaces)))

print('\nAll Done!\n')