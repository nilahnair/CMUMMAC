import os
import pandas as pd


def process_files():
    # Path to the dataset
    base_path='/vol/datasets/actrec/CMU_MMAC/MGX/'
    # Get list of folders in basepath
    files_path = [x for x in os.listdir(base_path)]

    # Iterate through each folder
    for p in range (len(files_path)):
        #print(files_path[p].replace("\SensorData", "\SensorData\Dataset"))
        # Extract subfolders within each folder
        sub_files_path= [x for x in os.listdir(base_path+files_path[p])]
        print(sub_files_path)
        files_df=[]
        # Iterate through all subfolders within each folder
        for q in range(len(sub_files_path)):
            # Extract files within each subfolder
            sub_sub_files_path = [x for x in os.listdir(base_path+files_path[p]+"/"+sub_files_path[q])]

            # Loop through the files and push them into array of dataframes
            for r in range(len(sub_sub_files_path)):
                print(p,q,r,base_path + files_path[p] + "/" + sub_files_path[q] + "/" + sub_sub_files_path[r] )
                compiled_path=base_path +files_path[p] + "/" + sub_files_path[q] + "/" + sub_sub_files_path[r]
                file_data = pd.read_csv(compiled_path,sep='\t',skiprows=1, )
                print('file data')
                print(file_data)
                # Renaming columns
                new_columns = list(file_data.columns)
                for i in range(len(new_columns)):
                    if new_columns[i] != 'SysTime':
                        new_columns[i] = new_columns[i]+"_ts"+str(r+1)
                file_data.columns = new_columns

                files_df.append(file_data)

            # Concatenate dfs into one df based on the SysTime Variable
            merged_df = files_df
           # print('after merge')
            #print(merged_df)
           # print(len(merged_df))
            drop_path='/data/nnair/cmu/'
            merged_df = merged_df[merged_df != 0].dropna() #dropping rows with missing values
           # print('after removing values')
           # print(merged_df)
           # print(len(merged_df))
           # print(drop_path +'test/'+files_path[p]+'/'+sub_files_path[q]+'.csv')
            # Export the DF into a file
           # print(merged_df)
           # print(len(merged_df))
            merged_df.to_csv(drop_path+'test/'+files_path[p]+'/'+sub_files_path[q]+'.csv', index=False, sep=',',)


process_files()