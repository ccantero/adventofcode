#!/bin/python3

import argparse
import os

def getPassword(filename):
    ACTUAL_POSITION = 50
    POSITIONS = [ACTUAL_POSITION]
    
    with open(filename, 'r') as file:
        for line in file:
            # Process each line here
            current_code = line.strip()
            direction = current_code[0]
            code = int(current_code[1:])
            if 'L' in current_code:
                ACTUAL_POSITION -= code
            elif 'R' in current_code:
                ACTUAL_POSITION += code
            else:
                raise("Incorrect code {}".format(current_code))
            
            while ACTUAL_POSITION < 0 or ACTUAL_POSITION > 99:
                if ACTUAL_POSITION < 0:
                    ACTUAL_POSITION += 100
                elif ACTUAL_POSITION > 100:
                    ACTUAL_POSITION -= 100
                elif ACTUAL_POSITION == 100:
                    ACTUAL_POSITION = 0

            POSITIONS.extend([ACTUAL_POSITION])

    return len([ x for x in POSITIONS if x == 0 ])

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Process a file given as input.")
    parser.add_argument(
        '-input_file', 
        type=str, 
        help="The path to the input file"
    )
    
    args = parser.parse_args()
    print("Password is {}".format(getPassword(args.input_file)))