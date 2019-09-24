#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 24 12:14:58 2019

@author: vanareddy
"""
import csv
from datetime import datetime

with open('csv-data/G5NZCJ017647206-Vana-left-hand_wash-none-2019-09-20-10-05-58.csv',newline='') as csvfile:
    lines = csv.reader(csvfile, delimiter=",")
     
    for line in lines:
        timestamp = line[0]
        dt_object = datetime.fromtimestamp(timestamp)
        print("dt_object =", dt_object)
        print("type(dt_object) =", type(dt_object))
        
