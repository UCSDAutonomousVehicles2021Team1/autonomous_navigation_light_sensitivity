import os
import shutil

def move_data(source, destination):
    #Creates the directory to copy data into
    os.makedirs(destination, exist_ok = True)
    
    dest = os.shutil.move(source, destination)
    
    print('Destination path: ' + dest)
