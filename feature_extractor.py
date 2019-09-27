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
import numpy as np
import collections

#filename = "data/G5NZCJ017647206-Kay-left-hand_wash-soap-2019-09-21-07-12-36.wada"
filename = "csv-data/G5NZCJ017647206-Kay-left-hand_wash-soap-2019-09-21-07-12-36.csv"

#f = open('./sample-features.csv', 'w')

def read_csv_file(filename):
    indices = []
    counts = []
    csv_reader = []
    data = []
    with open(filename) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        
        print(csv_reader)
        counter = 0
        prev = 0
        current = 0
        secs = []
        for row in csv_reader:
            #convert millisecond timestamp to seconds
            tsecs = float(row[0].strip())/1000.0
            
            ts = datetime.fromtimestamp(tsecs).strftime('%S')
            
            secs.append(ts)
            counter = counter + 1
            
        #print(secs)   
        u, indices, counts = np.unique(secs, return_index=True, return_counts=True)
        return indices, counts
    
def write_features(filename, indices, counts):
    with open(filename, 'r') as f:
        reader = csv.reader(f, delimiter=',')
        # get all the rows as a list
        data = list(reader)
        # transform data into numpy array
        data = np.array(data).astype(float)
     
    print(data)
    
    f = open('features.csv', 'w+')
    f.write("mean_x,std_x,mean_y,std_y,mean_z,std_z")
    f.write('\n')
    
    for i in range(0,len(counts)):
        
        mean_x = np.mean(data[indices[i]:indices[i]+counts[i]][:,1])
        mean_y = np.mean(data[indices[i]:indices[i]+counts[i]][:,2])
        mean_z = np.mean(data[indices[i]:indices[i]+counts[i]][:,3])
        std_x = np.std(data[indices[i]:indices[i]+counts[i]][:,1])
        std_y = np.std(data[indices[i]:indices[i]+counts[i]][:,2])
        std_z = np.std(data[indices[i]:indices[i]+counts[i]][:,3])
        print("Range {} and {}".format(indices[i], indices[i]+counts[i]))
        print("{},{},{},{},{},{}".format(mean_x,std_x,mean_y,std_y,mean_z,std_z))
        f.write("{},{},{},{},{},{}".format(mean_x,std_x,mean_y,std_y,mean_z, std_z))
        f.write('\n')
        
    f.close()
        
if __name__ == "__main__":
    
    filename = "csv-data/G5NZCJ017647206-Kay-left-hand_wash-soap-2019-09-21-07-12-36.csv"
    indices, counts = read_csv_file(filename)
    features_file = "features.csv"
    write_features(filename, indices, counts)
    
