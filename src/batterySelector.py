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

def getMaxJoltage(record):
    string_record = str(record)
    found = False
    for i in range(9,0,-1):
        # We should not consider last character
        for j in range(0,len(string_record)-1):
            if string_record[j] == str(i):
                found = True
                break
        if found:
            break

    for k in range(9,0,-1):
        if str(k) in string_record[j+1:]:
            return i*10 + k        
    
    raise("Unknown exception")

def getMaxJoltageNew(record):
    string_record = str(record)
    record_found = []
    count = 12
    last_position = 0
    while count > 0:
        found = False
        for i in range(9,0,-1):
            # We should not consider last n characters up to 12
            for j in range(last_position,len(string_record)-count+1):
                if string_record[j] == str(i):
                    found = True
                    break
            if found:
                record_found.append(string_record[j])
                last_position = j+1
                count -= 1
                break

    return "".join(record_found)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Process a file given as input.")
    parser.add_argument(
        '-input_file', 
        type=str, 
        help="The path to the input file"
    )
    
    args = parser.parse_args()
    lines = readFile(args.input_file)
    sum_of_joltage = 0
    for line in lines:
        sum_of_joltage += int(getMaxJoltageNew(line.strip()))
    print(sum_of_joltage)