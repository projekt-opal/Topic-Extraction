# -*- coding: utf-8 -*-
"""
Created on Thu Oct 31 13:09:21 2019

@author: Jan
"""
import DataExtraction as de
import json
with open("descriptions_testing.txt",'r',encoding='utf8') as f:
        content = f.readlines()
train= de.build_full_train_data_from_lines(content)
with open('test_file.json', "w",encoding='utf-8') as myfile:
    myfile.write(train)
