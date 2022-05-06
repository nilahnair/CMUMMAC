# -*- coding: utf-8 -*-
"""
Created on Fri May  6 07:32:55 2022

@author: nilah
"""
import os
import pandas as pd
import numpy as np
import csv
#import csv_reader


sandwich= {'S07':0, 'S08':1, 'S09':2, 'S12':3, 'S13':4, 'S15':5, 'S16':6, 'S17':7, 'S18':8, 'S19':9, 
           'S20':10,'S21':11, 'S22':12, 'S23':13, 'S25':14, 'S28':15, 'S29':16, 'S30':17, 'S31':18, 
           'S32':19, 'S34':20, 'S35':21, 'S36':22, 'S41':23, 'S47':24, 'S49':25, 'S50':26, 'S51':27,
           'S52':28, 'S53':29, 'S54':30, 'S55':31}

eggs= {'S07':0, 'S08':1, 'S09':2, 'S11':3, 'S12':4, 'S13':5, 'S14':6, 'S15':7, 'S16':8, 'S17':9, 
       'S18':10, 'S19':11,'S20':12,'S21':13, 'S25':14, 'S28':15, 'S29':16, 'S30':17, 'S31':18, 
       'S32':19, 'S34':20, 'S35':21, 'S36':22, 'S40':23, 'S47':24, 'S48':25, 'S49':26, 'S50':27, 
       'S51':28, 'S52':29, 'S53':30, 'S54':31, 'S55':32}

salad= {'S07':0, 'S08':1, 'S09':2, 'S11':3, 'S12':4, 'S13':5, 'S14':6, 'S15':7, 'S16':8, 'S17':9, 
       'S18':10, 'S19':11, 'S20':12,'S21':13, 'S22':14, 'S23':15, 'S25':16, 'S28':17, 'S29':18, 
       'S30':19, 'S31':20, 'S32':21, 'S34':22, 'S35':23, 'S36':24, 'S40':25, 'S41':26, 'S47':27, 
       'S48':28, 'S49':29, 'S50':30, 'S51':31, 'S52':32, 'S53':33, 'S54':34, 'S55':35}

pizza= {'S07':0, 'S08':1, 'S09':2, 'S11':3, 'S12':4, 'S14':5, 'S15':6, 'S16':7, 'S17':8, 
       'S18':9, 'S19':10, 'S20':11,'S21':12, 'S22':13, 'S25':14, 'S28':15, 'S29':16, 
       'S30':17, 'S31':18, 'S32':19, 'S34':20, 'S35':21, 'S36':22, 'S40':23, 'S41':24, 'S47':25, 
       'S48':26, 'S49':27, 'S50':28, 'S51':29, 'S52':30, 'S53':31, 'S54':32, 'S55':33}

brownie={'S07':0, 'S08':1, 'S09':2, 'S11':3, 'S12':4, 'S13':5, 'S14':6, 'S15':7, 'S16':8, 'S17':9, 
       'S18':10, 'S19':11, 'S20':12,'S21':13, 'S22':14, 'S24':15, 'S25':16, 'S28':17, 'S29':18, 
       'S30':19, 'S31':20, 'S32':21,'S33':22, 'S34':23, 'S35':24, 'S40':25, 'S47':26, 
       'S48':27, 'S49':28, 'S50':29, 'S51':30, 'S53':31, 'S54':32, 'S55':33}

all_recipie= {'S07':0, 'S08':1, 'S09':2, 'S12':3, 'S15':4, 'S16':5, 'S17':6, 'S18':7, 'S19':8, 
           'S20':9,'S21':10, 'S25':11, 'S28':12, 'S29':13, 'S30':14, 'S31':15, 'S32':16, 'S34':17, 
           'S35':18, 'S47':19, 'S49':20, 'S50':21, 'S51':22, 'S53':23, 'S54':24, 'S55':25}

sensora=['Accel_X_ts1_x', 'Accel_Y_ts1_x', 'Accel_Z_ts1_x', 'Roll_ts1_x', 'Pitch_ts1_x', 'Yaw_ts1_x', 'Mag_X_ts1_x', 'Mag_Y_ts1_x', 'Mag_Z_ts1_x', 'Count_ts1_x', 
         'Accel_X_ts2_x', 'Accel_Y_ts2_x', 'Accel_Z_ts2_x', 'Roll_ts2_x', 'Pitch_ts2_x', 'Yaw_ts2_x', 'Mag_X_ts2_x', 'Mag_Y_ts2_x', 'Mag_Z_ts2_x', 'Count_ts2_x', 
         'Accel_X_ts3_x', 'Accel_Y_ts3_x', 'Accel_Z_ts3_x', 'Roll_ts3_x', 'Pitch_ts3_x', 'Yaw_ts3_x', 'Mag_X_ts3_x', 'Mag_Y_ts3_x', 'Mag_Z_ts3_x', 'Count_ts3_x', 
         'Accel_X_ts4_x', 'Accel_Y_ts4_x', 'Accel_Z_ts4_x', 'Roll_ts4_x', 'Pitch_ts4_x', 'Yaw_ts4_x', 'Mag_X_ts4_x', 'Mag_Y_ts4_x', 'Mag_Z_ts4_x', 'Count_ts4_x', 
         'Accel_X_ts5_x', 'Accel_Y_ts5_x', 'Accel_Z_ts5_x', 'Roll_ts5_x', 'Pitch_ts5_x', 'Yaw_ts5_x', 'Mag_X_ts5_x', 'Mag_Y_ts5_x', 'Mag_Z_ts5_x', 'Count_ts5_x']

def statistics_measurements():
    '''
    Computes some statistics over the channels for the entire training data

    returns a max_values, min_values, mean_values, std_values
    '''

    dataset_path_imu = "/data/nnair/cmu/test/Brownie/"
    files_path = [x for x in os.listdir(dataset_path_imu)]
    
    IMU=[]
    data = []

    accumulator_measurements = np.empty((0, 45))
    
    for file in files_path:
        print(file)
        print('\n')
        path= dataset_path_imu + file
        print(path)
        print('\n')
        try:
            with open(path, 'r') as csvfile:
                spamreader = csv.reader(csvfile, delimiter=';', quotechar='|')
                for row in spamreader:
                    try:
                        try:
                            if spamreader.line_num == 1:
                                # print('\n')
                                print(', '.join(row))
                            else:
                                if len(row) != 50 :
                                            idx_row = 0
                                            IMU.append(row[idx_row])
                                            idx_row += 1
                                else:
                                    idx_row = 0
                                        
                                data.append(list(map(float, row[idx_row:])))
                        except:
                            print("Error in line {}".format(row))
                    except KeyboardInterrupt:
                        print('\nYou cancelled the operation.')
        except:
            print("\n no file called file {}".format(dataset_path_imu + path))
            continue
                    
        print(len(data))
        print(len(data[1]))
        print(data.type)                      
        if len(row) != 50:
                        imu_data = {'data': data}
        else:
            try:
                print("check")
                imu_data = {'data': data}
                data_new=np.asarray(data)
                print(data_new.shape)
                print(accumulator_measurements.shape)
                accumulator_measurements = np.append(accumulator_measurements, data_new, axis=0)
                print("\nFiles loaded")
            except:
                print("\n1 In loading data,  in file {}".format(dataset_path_imu + path))
                continue
                            
    
    try:
        max_values = np.max(accumulator_measurements, axis=0)
        print("Max values")
        print(max_values)
        min_values = np.min(accumulator_measurements, axis=0)
        print("Min values")
        print(min_values)
        mean_values = np.mean(accumulator_measurements, axis=0)
        print("Mean values")
        print(mean_values)
        std_values = np.std(accumulator_measurements, axis=0)
        print("std values")
        print(std_values)
    except:
        max_values = 0
        min_values = 0
        mean_values = 0
        std_values = 0
        print("Error computing statistics")
    
    return max_values, min_values, mean_values, std_values

if __name__ == '__main__':
    
    #Computing Statistics of data
    max_values, min_values, mean_values, std_values = statistics_measurements()
    
    x = []
    x.append(list(max_values))
    x.append(list(min_values))
    x.append(list(mean_values))
    x.append(list(std_values))
    x=np.asarray(x)
    print(x)
  
    base_directory='/data/nnair/trial/'
    
    csv_dir=  base_directory+"all_normalisation_values_imu.csv"
    print(csv_dir)
    np.savetxt(csv_dir, x, delimiter="\n", fmt='%s')