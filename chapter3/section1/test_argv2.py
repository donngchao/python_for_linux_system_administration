from __future__ import print_function
import os
import sys


def main():
    # 向sys.argv 添加一个空字符串
    sys.argv.append("")
    filename = sys.argv[1]
    if os.path.isdir(filename):
        raise SystemExit('The ' + filename + ' is a directory !')
    elif not os.path.isfile(filename):
        raise SystemExit(filename + ' does not exists')
    elif not os.access(filename, os.R_OK):
        raise SystemExit(filename + ' is not accessible')
    else:
        print(filename + ' is accessible')


if __name__ == '__main__':
    main()

'''
[root@test]# python3 test_argv2.py test_argv2.py 
test_argv2.py is accessible
'''
