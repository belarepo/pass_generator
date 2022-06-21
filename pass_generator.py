#!/usr/bin/python3

from secrets import choice as pick
from string import ascii_letters , digits , punctuation
"""
This script makes random strong passwords with arbitrary length.
"""
CHARSET = list(ascii_letters + digits + punctuation)

def generator():
    
    for _ in range(3):
        
        try:
            
            length = int(input("Type in the length of password or enter 0 to exit: "))
            if length == 0: return
            if length > 200: raise Exception
        except:
            
            if _ == 2:
                
                print("The script faild!")
                return
            
            print("***Please enter a valid length from 1 to 200 or type 0 to exit***")
        else: break
    
    
    passwd = ""
    for _ in range(length):
        char = pick(CHARSET)
        passwd += char
        
    print(passwd)

    char , passwd = '',''  #Cleaner

generator()
