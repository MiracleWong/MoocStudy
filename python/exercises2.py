# -*- coding: utf-8 -*-
def Output(string):
    for char in string:
        print(char)

def Input():
    return str(input())

if __name__ == '__main__':
    while True:
        words = Input()
        Output(words)
