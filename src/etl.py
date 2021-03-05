import os
import shutil

def copy_data(source, data_fp):
    #Creates the directory to copy data into
    os.makedirs(data_fp, exist_ok = True)
    
    print("Data in my source folder:")
    print(os.listdir(source))
    
    for i in os.listdir(source)[:-1]:
        shutil.copy(i, data_fp)
   
    print('After copying: ' + os.listdir(data_fp))
