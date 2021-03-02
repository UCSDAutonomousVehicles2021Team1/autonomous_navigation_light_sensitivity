# import the necessary packages
from skimage.metrics import structural_similarity as ssim
import matplotlib.pyplot as plt
import numpy as np
import cv2
import pandas as pd

def main_eda(files, outdir, **kwargs):
  
