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
            

def getPassword(lines):
    ACTUAL_POSITION = 50
    POSITIONS = [ACTUAL_POSITION]
    ZERO_COUNTS = 0

    for current_code in lines:
        direction = current_code[0]
        code = int(current_code[1:])
        PREV_POSITION = ACTUAL_POSITION 
        if 'L' in current_code:
            ACTUAL_POSITION -= code % 100
        elif 'R' in current_code:
            ACTUAL_POSITION += code % 100
        else:
            raise("Incorrect code {}".format(current_code))

        if ACTUAL_POSITION < 0:
            if PREV_POSITION > 0:
                ZERO_COUNTS += 1
            ACTUAL_POSITION = 100 + ACTUAL_POSITION
        elif ACTUAL_POSITION > 100:
            if PREV_POSITION > 0:
                ZERO_COUNTS += 1
            ACTUAL_POSITION = ACTUAL_POSITION - 100
        elif ACTUAL_POSITION == 100:
            ZERO_COUNTS += 1
            ACTUAL_POSITION = 0
        elif ACTUAL_POSITION == 0 and PREV_POSITION > 0:
            ZERO_COUNTS += 1

        if code // 100 >= 1:
            ZERO_COUNTS += int(code / 100)
            
        POSITIONS.extend([ACTUAL_POSITION])

    return ( POSITIONS , ZERO_COUNTS)

def test():
    test_lines = ['R1000', 'L1000', 'L50', 'R1', 'L1', 'L1', 'R1', 'R100', 'R1']
    POSITIONS, pwd2 = getPassword(test_lines)
    assert POSITIONS == [50, 50, 50, 0, 1, 0, 99, 0, 0, 1]
    assert 24 == pwd2

    test_lines = ['L68', 'L30', 'R48', 'L5', 'R60', 'L55', 'L1', 'L99', 'R14', 'L82']
    pwd1, pwd2 = getPassword(test_lines)
    assert pwd1 == [50, 82, 52, 0, 95, 55, 0, 99, 0, 14, 32]
    assert pwd2 == 6


    test_lines = ['R1000', 'L68', 'L30', 'R48', 'L5', 'R60', 'L55', 'L1', 'L99', 'R14', 'L82']
    pwd1, pwd2 = getPassword(test_lines)
    assert pwd1 == [50, 50, 82, 52, 0, 95, 55, 0, 99, 0, 14, 32]
    assert pwd2 == 16

    test_lines = [ 'L50', 'R101' ]
    POSITIONS, pwd2 = getPassword(test_lines)
    assert 2 == pwd2

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Process a file given as input.")
    parser.add_argument(
        '-input_file', 
        type=str, 
        help="The path to the input file"
    )
    
    args = parser.parse_args()
    test()

    lines = readFile(args.input_file)
    POSITIONS, pwd2 = getPassword(lines)
    assert 992 == len([ x for x in POSITIONS if x == 0 ])
    print("Password with method 1 is {}".format(992))
    print("Password with method 2 is {}".format(pwd2))