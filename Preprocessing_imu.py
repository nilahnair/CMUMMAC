# -*- coding: utf-8 -*-
"""
Created on Fri Apr  1 09:26:43 2022

@author: nilah
"""

import os
import numpy as np
import datetime
import csv

folder_name='C:/Users/nilah/OneDrive/Desktop/Work/PatRec/ICPR 2022/CMU MMAC/Sample data/'
subjects = {"S07":7, "S08": 8, "S09": 9, "S11": 11, "S12": 12, "S13": 13, "S14":14, "S15":15, "S16":16, "S17":17, "S18":18, 
            "S19":19, "S20":20, "S21": 21, "S22": 22, "S23":23, "S24":24, "S25":25, "S28":28, "S29":29, "S30":30, "S31":31, 
            "S32":32, "S33":33, "S34":34, "S35":35, "S36":36, "S37":37, "S40":40, "S41":41, "S47":47, "S48":48, "S49":49, 
            "S50":50, "S51":51, "S52":52, "S53":53, "S54":54, "S55":55}
    

def generate_data(recipes, ids, sliding_window_length, sliding_window_step, data_dir=None, usage_modus ='train'):
    
    counter_seq = 0
    counter_file_label = -1
    sensor_IDs = ["2794", "2795", "2796", "3261", "3337"]
    DMGX1_recordings = {}
    flag_time_error = False
    for r in recipes:
        for sub in ids: 
            print('\n')
            recipe_folder= folder_name + r + '/' + sub + '_' + r +'_3DMGX1/'
            print(recipe_folder)
            combine = []
            for root_d, dirs_D, files in os.walk(recipe_folder):
                for fi in files: 
                    count=0
                    print(fi)
                    with open(recipe_folder + fi, 'r') as csvfile:
                        data = []
                        #time_r = []
                        DMGX1 = csv.reader(csvfile, delimiter='\n', quotechar='|')
                        for row in DMGX1:
                            try:
                                if DMGX1.line_num < 3:
                                    print(', '.join(row))
                                else:
                                    splitrow = row[0].split("\t")
                                    if splitrow[-2].split("_")[0] == 'ERROR':
                                        '''
                                        print(splitrow[-2])
                                        splitrow[-2] = -1
                                        flag_time_error = True
                                        '''
                                        pass
                                    else:
                                        data.append(list(map(float, splitrow[:-1])))
                                    #if 723 <= DMGX1.line_num < 732:
                                    #    print(row)
                                    #print(', '.join(row))
                                    '''
                                    if int(splitrow[-1].split("_")[-1]) % 10:
                                        milli_corrected = (int(splitrow[-1].split("_")[-1]) - 1)//10 #(int(splitrow[-1].split("_")[-1]) % 10)
                                        if milli_corrected == 0:
                                            strmillis = splitrow[-1].split("_")[0] + '_' +  splitrow[-1].split("_")[1] + '_' + splitrow[-1].split("_")[2] + '_0000000'
                                        else:
                                            strmillis = splitrow[-1].split("_")[0] + '_' +  splitrow[-1].split("_")[1] + '_' + splitrow[-1].split("_")[2] + '_' + '{:06d}'.format(milli_corrected)

                                        time_r.append(datetime.datetime.strptime(strmillis, '%H_%M_%S_%f0'))
                                        if milli_corrected % 10 > 0:
                                            time_r.append(datetime.datetime.strptime(strmillis, '%H_%M_%S_%f'))
                                        else:
                                            time_r.append(datetime.datetime.strptime(strmillis, '%H_%M_%S_%f0'))
                                    else:
                                        time_r.append(datetime.datetime.strptime(splitrow[-1], '%H_%M_%S_%f0'))
                                    '''
                            except KeyboardInterrupt:
                                print('\nYou cancelled the operation.')
                        #DMGX1_recordings[fi] = [np.array(data), time_r]
                        newdat=np.array(data)
                        DMGX1_recordings[fi] =np.array(data)
                        if count==0 and newdat.size == None:
                            combine.append(0)
                        elif count == 0 and newdat.size != None:
                            combine.append(newdat.size)
                        elif count != 0 and newdat.size == None:
                           combine.append(0)
                        else:
                            combine.append(newdat.size)
                
                    if flag_time_error:
                        print("correcting sequence")    
                    count=count+1
            print(combine)        
                        
                    
    

def create_dataset():
    '''
    subjects = {"S07":7, "S08": 8, "S09": 9, "S11": 11, "S12": 12, "S13": 13, "S14":14, "S15":15, "S16":16, "S17":17, "S18":18, 
            "S19":19, "S20":20, "S21": 21, "S22": 22, "S23":23, "S24":24, "S25":25, "S28":28, "S29":29, "S30":30, "S31":31, 
            "S32":32, "S33":33, "S34":34, "S35":35, "S36":36, "S37":37, "S40":40, "S41":41, "S47":47, "S48":48, "S49":49, 
            "S50":50, "S51":51, "S52":52, "S53":53, "S54":54, "S55":55}
    '''
    #recipes = ['Sandwich', 'Eggs', 'Salad', 'Pizza', 'Brownies']
    
    train_ids = {"S07":7}
    recipes = ['Brownie']
    
    base_directory = 'C:/Users/nilah/OneDrive/Desktop/Work/PatRec/ICPR 2022/CMU MMAC/Sample data/'
    
    data_dir_train = base_directory + 'sequences_train/'
    #data_dir_val = base_directory + 'sequences_val/'
    #data_dir_test = base_directory + 'sequences_test/'

    generate_data(recipes, train_ids, sliding_window_length=100, sliding_window_step=12, data_dir=data_dir_train)
    #generate_data(recipes, val_ids, sliding_window_length=100, sliding_window_step=12, data_dir=data_dir_val)
    #generate_data(recipes, test_ids, sliding_window_length=100, sliding_window_step=12, data_dir=data_dir_test)
    print("done")
    
    #generate_CSV(base_directory, "train.csv", data_dir_train)
    #generate_CSV(base_directory, "val.csv", data_dir_val)
    #generate_CSV(base_directory, "test.csv", data_dir_test)
    #generate_CSV_final(base_directory + "train_final.csv", data_dir_train, data_dir_val)
    
if __name__ == '__main__':
    create_dataset()
    print("Done")