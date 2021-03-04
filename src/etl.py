import os
import shutil

def move_data(source, data_fp):
    #Creates the directory to copy data into
    os.makedirs(data_fp, exist_ok = True)
    
    print("Before moving data:")
    print(os.listdir(source))
    
    dest = shutil.move(source, data_fp)
    
    print("After moving data:")
    print(os.listdir(source))
    
    print('Destination path: ' + data_fp)
