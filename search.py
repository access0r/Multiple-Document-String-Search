#string search comparator
#using openai
#create a python script that does the following
#
#open <doc_a>
#search for a matching string in doc_b
#each line in doc_a has one string
#! 
#include command line flag arguments 
#--doc_a for doc_a file input, --doc_b for doc_b file input, --o, for write results to file


import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--doc_a', required=True, help="The file to search from")
parser.add_argument('--doc_b', required=True, help="The file to search in")
parser.add_argument('--o', required=True, help="The file to write the results to")

args = parser.parse_args()

result_file = open(args.o, 'w')

with open(args.doc_a, 'r') as doc_a:
    for line in doc_a:
        line = line.rstrip()
        with open(args.doc_b, 'r') as doc_b:
            found = False
            for b_line in doc_b:
                if line in b_line:
                    found = True
            if found:
                result_file.write(line + '\n')

result_file.close()
