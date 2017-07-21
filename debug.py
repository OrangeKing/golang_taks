import sys
from behave import __main__

if __name__ == '__main__':
    __main__.main('-k --wip {}'.format(sys.argv[1]))
