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

#import csv
import pandas
filename = "/home/student/Android/Sdk/platform-tools/data/G5NZCJ017647206-Kay-left-hand_wash-sanitizer-2019-09-21-11-39-15.csv"

df = pandas.read_csv(filename)
#print (len(df))
for i in range(0,len(df),1000):
    print (i)
    mean_ = df.iloc[i:i+1000].mean()
    st_dev = df.iloc[i:i+1000].std()
    print ("index_1 {} index_2 {} mean {} stdev {}".format(i, i+1000, mean_, st_dev))
    print(' ')
