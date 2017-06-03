# -*- coding: utf-8 -*-
x = 'a b c d e f g h i j k l m n o p q r s t u v w x y z'.split(' ')
y = 'n o p q r s t u v w x y z a b c d e f g h i j k l m'.split(' ')
X = map(lambda x: x.upper(), x)
Y = map(lambda x: x.upper(), y)
dict_caesar = dict(zip(x + X, y + Y))


def caesar(string):
    result = []
    for i in range(len(string)):
        if string[i] in dict_caesar.keys():
            result.append(dict_caesar[string[i]])
        else:
            result.append(string[i])
    return ''.join(result)


print(caesar(raw_input()))
