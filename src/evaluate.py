import numpy as np
import os
import json
import math
from PIL import Image, ImageStat


def runtime_perfomrance_eval(baseline_fp):
    
    store_perceived = []
    for i in range(len(os.listdir(baseline_fp))):
        store_perceived.append(perceived_bn(baseline_fp, i))
    
    runtime_performance = np.std(store_perceived) ** 2
    return runtime_performance

# function to calculate 
def perceived_bn(baseline_fp, jpg):
    
    converted_num = "% s" % jpg
    if (jpg < 10):
        jpg_string = baseline_fp + '/frame000' + converted_num + '.jpg'
    else:
        jpg_string = baseline_fp + '/frame00' + converted_num + '.jpg'
    img = Image.open(jpg_string)
    stat = ImageStat.Stat(img)
    r,g,b = stat.rms
    
    return math.sqrt(0.241*(r**2) + 0.691*(g**2) + 0.068*(b**2))
  


    
