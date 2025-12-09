#!/bin/python3

import argparse
import os

def readFile(filename):
    lines = []
    with open(filename, 'r') as file:
        for line in file:
            current_code = line.strip()
            lines.append(current_code)
    return lines

def isNotLegitID(number):
    number_str = str(number)
    if len(number_str) % 2 == 0:
        return number_str[0:len(number_str)//2] == number_str[len(number_str)//2:]

    return False

def getListOfNSubstrings(string, n):
    list_of_strings = []
    ini = 0
    size = len(string) // n
    last = size
    while ini+size <= len(string):
        list_of_strings.append(string[ini:last])
        ini += size
        last += size
    
    return list_of_strings

def isNotLegitIDNew(number):
    if number < 10:
        return False
    number_str = str(number)
    if len(number_str) % 2 == 0:
        if number_str[0:len(number_str)//2] == number_str[len(number_str)//2:]:
            return True
    else:
        aList = [1 for x in number_str if x == number_str[0]]
        if len(aList) == len(number_str):
            return True

    for n in range(2,len(number_str)//2+1):
        list_of_substrings = getListOfNSubstrings(number_str,n)
        if list_of_substrings[0] * n == number_str:
            return True

    return False

def getInvalidIdsFromRange(ranges):
    invalid_ids = []
    for aRange in ranges.split(','):
        vector = aRange.split('-')
        start = int(vector[0])
        end = int(vector[1])
        for x in range(start,end+1):
            if isNotLegitIDNew(x):
                invalid_ids.append(x)
    
    return invalid_ids

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Process a file given as input.")
    parser.add_argument(
        '-input_file', 
        type=str, 
        help="The path to the input file"
    )
    
    args = parser.parse_args()
    lines = readFile(args.input_file)
    # It is expected only one line
    invalidIDs = getInvalidIdsFromRange(lines[0].strip())
    print(sum(invalidIDs))