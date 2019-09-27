# Kay Hutchinson 9/24/19
# Vanamala Venkataswamy 9/26/19

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
from datetime import datetime
import numpy as np
import os

#This function takes a processed csv file and gets count of seconds and indices
#of seconds when it changes
#Input: CSV file
#Converts milli-seconds to seconds
#Gets seconds and gets indices/counts when seconds change
#Output: incides, counts
def read_csv_file(filename):
    indices = []
    counts = []
    csv_reader = []
    with open(filename) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')

        secs = []
        for row in csv_reader:
            #convert millisecond timestamp to seconds
            tsecs = float(row[0].strip())/1000.0
            #get seconds
            ts = datetime.fromtimestamp(tsecs).strftime('%S')
            #put all the seconds in list
            secs.append(ts)

        #get indices and counts of unique seconds
        u, indices, counts = np.unique(secs, return_index=True, return_counts=True)

        return indices, counts

#This function take a CSV file, and prints out features to features.csv
#Input: csv_file, indices, counts, activity for the file (hand_wash,not_hand_wash)
#gathers means and standard deviations for x,y,z co-ordinates based on time-interval
#writes the data to features.csv file
def write_features(csv_filename, indices, counts, activity, features_file):
    with open(csv_filename, 'r') as f:
        reader = csv.reader(f, delimiter=',')
        # get all the rows as a list
        data = list(reader)
        # transform data into numpy array
        data = np.array(data).astype(float)

    f = open(features_file, 'a+')

    for i in range(0,len(counts)):

        mean_x = np.mean(data[indices[i]:indices[i]+counts[i]][:,1])
        mean_y = np.mean(data[indices[i]:indices[i]+counts[i]][:,2])
        mean_z = np.mean(data[indices[i]:indices[i]+counts[i]][:,3])
        std_x = np.std(data[indices[i]:indices[i]+counts[i]][:,1])
        std_y = np.std(data[indices[i]:indices[i]+counts[i]][:,2])
        std_z = np.std(data[indices[i]:indices[i]+counts[i]][:,3])
        f.write("{},{},{},{},{},{},{}".format(mean_x,std_x,mean_y,std_y,mean_z, std_z,activity))
        f.write('\n')

    f.close()

if __name__ == "__main__":
    directory = "/home/student/Android/Sdk/platform-tools/data"
    features_file = "features.csv"

    f = open(features_file, 'a+')
    #write header in features.csv
    f.write("mean_x,std_x,mean_y,std_y,mean_z,std_z,Activity")
    f.write('\n')

    with open(features_file, 'a+') as f:
        #for all the files in csv-data, process the csv and gather features in features.csv
        for csv_filename in os.listdir(directory):
            if csv_filename.endswith('.csv'):
                print("Processing {}".format(os.path.join(directory, csv_filename)))
                #get acitivity type from file name, hopefully the filenames are generated with actitity info
                #if filenames do not have activity info, then we may get unspecified info for y
                activity = str(os.path.join(directory, csv_filename)).split('-')
                indices, counts = read_csv_file(os.path.join(directory, csv_filename))
                write_features(os.path.join(directory, csv_filename), indices, counts, activity[4], features_file)
            else:
                continue
