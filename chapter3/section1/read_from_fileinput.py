from __future__ import print_function
import fileinput

for line in fileinput.input():
    print(line, end="")


'''
python read_from_fileinput.py ./test_argv.py ./test_argv2.py
'''