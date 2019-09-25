# Kay Hutchinson 9/24/19

# CPS SPML Class Smart Watch Project
# Smart Watch Feature Extractor
# Write a program to extract features from the accelerometer data (formatted csv files generated suing the Wada.jar tool).
# For each one second of data (window), compute the mean and standard deviation for each axis (X, Y, Z).
# Ignore the last incomplete second of data
# Save the features along with a label (hand_wash/no_hand_wash) to a .csv file, one line for each window.
# Order of entries is:
#     mean_x, std_x, mean_y, std_y, mean_z, std_z, Activity
# where Activity is 'hand_wash' or 'no_hand_wash'

import csv
import pandas as pd
from datetime import datetime

#filename = "data/G5NZCJ017647206-Kay-left-hand_wash-soap-2019-09-21-07-12-36.wada"
filename = "csv-data/G5NZCJ017647206-Kay-left-hand_wash-soap-2019-09-21-07-12-36.csv"

f = open('./sample-features.csv', 'w')

with open(filename) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    print(csv_reader)
    counter = 0
    for row in csv_reader:
        #convert millisecond timestamp to seconds
        tsecs = float(row[0].strip())/1000.0
        #convert timestamp to dat/time format
        print(datetime.fromtimestamp(tsecs).strftime('%m:%d:%y %H:%M:%S'))
        #print(datetime.fromtimestamp(ts).strftime('%S'))
        f.write(datetime.fromtimestamp(tsecs).strftime('%m:%d:%y %H:%M:%S') + '\n')
        counter = counter + 1
        '''
        if(counter == 0):
            prev = datetime.fromtimestamp(ts).strftime('%S')
            current = datetime.fromtimestamp(ts).strftime('%S')
        
        current = datetime.fromtimestamp(ts).strftime('%S')
        
        if(current != prev):
            print("Changed {} to {}".format(prev, current))
            prev = current
            
        counter = counter + 1
        '''
        #print("Count :", counter)
'''     
   
df = pd.read_csv(filename)
print(df)
print (len(df))

for i in range(0,len(df),1000):
    print (i)
    mean_ = df.iloc[i:i+1000].mean()
    st_dev = df.iloc[i:i+1000].std()
    print ("index_1 {} index_2 {} mean {} stdev {}".format(i, i+1000, mean_, st_dev))
    print(' ')
    
'''
