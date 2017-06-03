# -*- coding: utf-8 -*-
input_vegetables = input() 
vegetables_list = input_vegetables.split(',')
vegetables_result = []
for i in vegetables_list:
    for j in vegetables_list:
        if i != j:
            vegetables_result.append(i + j)
for i in vegetables_result:
    print i
