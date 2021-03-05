import os
import shutil

def load_data(single_source, lap_source, single_data_fp, lap_data_fp):
    #Creates the directory to copy data into
    os.makedirs(data_fp, exist_ok = True)
    
    print("Data in my single image data folder:")
    print(os.listdir(single_source))
    
    print("Data in my collective lap data folder:")
    print(os.listdir(lap_source))
    
    for i in os.listdir(single_source):
        shutil.copy(single_source + i, single_data_fp)
    
    for j in os.listdir(lap_source):
        shutil.copytree(lap_source + j, lap_data_fp)
    print('After loading data: ' + str(os.listdir(single_data_fp)))
