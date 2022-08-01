# 1. There is string s = "Python Bootcamp". Write the code that hashes string.
import hashlib

s = "Python Bootcamp"


def option_1(inp):
    print('Default method:', hash(inp))


def option_2(inp):
    print('hashlib.md5 digest:', hashlib.md5(inp.encode()).digest())


def option_3(inp):
    print('hashlib.sha1 digest:', hashlib.sha1(inp.encode()).digest())


if __name__ == '__main__':
    print('Input String:', s)
    print('Hashing...')
    option_1(s)
    option_2(s)
    option_3(s)
