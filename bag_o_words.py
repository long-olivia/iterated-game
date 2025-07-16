import os
import sys
import json
import re

'''i want to go through each prompt pairing. and then i want to do a bag of words for each round
and then see which words are most prevalent.
'''

#open all files
def prepare(directory):
    base_dir="."
    path=os.path.join(base_dir, directory)
    files=os.listdir(path)
    for file_name in files:
        file_path=os.path.join(path, file_name)
        with open(file_path, 'r') as f:
            data=json.load(f)
            bag_it_up(data)
        

#implement bag of words
#TODO: need to see if I"m missing anything else for negations. Then, implement bag of word algorithm.

            

