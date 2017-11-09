#!/usr/bin/env python

#this program generates a "l33t" style password based on a user given word

import string
import random

class bcolors:
    FAIL = '\033[93m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    ENDC = '\033[0m'
    ERROR = '\033[31m'
    WHITE = '\033[37m'


#if __name__ == '__main__':

    #print(bcolors.ERROR +"[*]" + bcolors.FAIL + "usage: passgen.py string" + bcolors.ENDC)
    #quit()

base = raw_input(bcolors.WHITE + "Insert a base string:\n> " + bcolors.ENDC)
counter = 0
c=0
total = len(base)

while c < total:
    if(base[counter] == 'a' or base[counter] == 'A'):
        op = random.choice([1,2,3,4])
        if(op == 1):
            base = base[:counter] + '@' + base[counter+1:]
        if(op == 2):
            base = base[:counter] + '4' + base[counter+1:]
        if(op == 3):
            base = base[:counter] + 'a' + base[counter+1:]
        if(op == 4):
            base = base[:counter] + 'A' + base[counter+1:]

    if(base[counter] == 'b' or base[counter] == 'B'):
        op = random.choice([1,2,3])
        if(op == 1):
            base = base[:counter] + '8' + base[counter+1:]
        if(op == 2):
            base = base[:counter] + 'b' + base[counter+1:]
        if(op == 3):
            base = base[:counter] + 'B' + base[counter+1:]

    if(base[counter] == 'c' or base[counter] == 'C'):
        op = random.choice([1,2,3,4])
        if(op == 1):
            base = base[:counter] + '(' + base[counter+1:]
        if(op == 2):
            base = base[:counter] + '<' + base[counter+1:]
        if(op == 3):
            base = base[:counter] + 'c' + base[counter+1:]
        if(op == 4):
            base = base[:counter] + 'C' + base[counter+1:]

    if(base[counter] == 'e' or base[counter] == 'E'):
        op = random.choice([1,2,3,4])
        if(op == 1):
            base = base[:counter] + '3' + base[counter+1:]
        if(op == 2):
            base = base[:counter] + '&' + base[counter+1:]
        if(op == 3):
            base = base[:counter] + 'e' + base[counter+1:]
        if(op == 4):
            base = base[:counter] + 'E' + base[counter+1:]

    if(base[counter] == 'g' or base[counter] == 'G'):
        op = random.choice([1,2,3])
        if(op == 1):
            base = base[:counter] + '6' + base[counter+1:]
        if(op == 2):
            base = base[:counter] + 'g' + base[counter+1:]
        if(op == 3):
            base = base[:counter] + 'G' + base[counter+1:]

    if(base[counter] == 'h' or base[counter] == 'H'):
        op = random.choice([1,2,3])
        if(op == 1):
            base = base[:counter] + '#' + base[counter+1:]
        if(op == 2):
            base = base[:counter] + 'h' + base[counter+1:]
        if(op == 3):
            base = base[:counter] + 'H' + base[counter+1:]

    if(base[counter] == 'i' or base[counter] == 'I'):
        op = random.choice([1,2,3,4,5])
        if(op == 1):
            base = base[:counter] + 'l' + base[counter+1:]
        if(op == 2):
            base = base[:counter] + '1' + base[counter+1:]
        if(op == 3):
            base = base[:counter] + '!' + base[counter+1:]
        if(op == 4):
            base = base[:counter] + 'i' + base[counter+1:]
        if(op == 5):
            base = base[:counter] + 'I' + base[counter+1:]

    if(base[counter] == 'l' or base[counter] == 'L'):
        op = random.choice([1,2,3])
        if(op == 1):
            base = base[:counter] + '1' + base[counter+1:]
        if(op == 2):
            base = base[:counter] + 'l' + base[counter+1:]
        if(op == 3):
            base = base[:counter] + 'L' + base[counter+1:]

    if(base[counter] == 'o' or base[counter] == 'O'):
        op = random.choice([1,2,3])
        if(op == 1):
            base = base[:counter] + '0' + base[counter+1:]
        if(op == 2):
            base = base[:counter] + 'o' + base[counter+1:]
        if(op == 3):
            base = base[:counter] + 'O' + base[counter+1:]
    if(base[counter] == 's' or base[counter] == 'S'):
        op = random.choice([1,2,3,4])
        if(op == 1):
            base = base[:counter] + '5' + base[counter+1:]
        if(op == 2):
            base = base[:counter] + '$' + base[counter+1:]
        if(op == 3):
            base = base[:counter] + 's' + base[counter+1:]
        if(op == 4):
            base = base[:counter] + 'S' + base[counter+1:]
    if(base[counter] == 't' or base[counter] == 'T'):
        op = random.choice([1,2,3,4])
        if(op == 1):
            base = base[:counter] + '+' + base[counter+1:]
        if(op == 2):
            base = base[:counter] + '7' + base[counter+1:]
        if(op == 3):
            base = base[:counter] + 't' + base[counter+1:]
        if(op == 4):
            base = base[:counter] + 'T' + base[counter+1:]
    if(base[counter] == 'z' or base[counter] == 'Z'):
        op = random.choice([1,2,3,])
        if(op == 1):
            base = base[:counter] + '2' + base[counter+1:]
        if(op == 2):
            base = base[:counter] + 'z' + base[counter+1:]
        if(op == 3):
            base = base[:counter] + 'Z' + base[counter+1:]

    c += 1
    counter += 1
print(bcolors.OKBLUE + "\nPassword: " + bcolors.ENDC),
print(bcolors.OKGREEN + base + "\n")
