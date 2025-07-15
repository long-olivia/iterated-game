import os
import sys
import json
import re

'''i want to go through each prompt pairing. and then i want to do a bag of words for each round
and then see which words are most prevalent.
'''

#process negations
def prepare(directory):
    base_dir="."
    path=os.path.join(base_dir, directory)
    files=os.listdir(path)
    for file_name in files:
        file_path=os.path.join(path, file_name)
        with open(file_path, 'r') as f:
            data=json.load(f)
    return data

def negations(directory):
    data=prepare(directory)
    for i in range(1,21):
        to_negate=data[f"{i}"]
        


if __name__=="__main__":
    process_negations("TEST_CORPUS")
            

