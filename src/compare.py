# import the necessary packages
import os
from skimage.metrics import structural_similarity as ssim
import matplotlib.pyplot as plt
import numpy as np
import cv2


def view_results(files, outdir):
    os.makedirs(outdir, exist_ok = True)
    baseline_results(files[0], files[1], outdir)
    tuned_results(files[0], files[2], outdir)
    

def calculate_mse(imageA, imageB):
    # the 'Mean Squared Error' between the two images is the
    # sum of the squared difference between the two images;
    # NOTE: Two images have the same dimension
    error = np.sum((imageA.astype("float") - imageB.astype("float")) ** 2)
    error /= float(imageA.shape[0] * imageA.shape[1])
    
    # return the MSE, the lower the error, the more "similar" the two images are
    return error
 

def baseline_results(imageA, imageB, outdir):
    # compute the mean squared error and structural similarity
    # index for the images
    s = ssim(imageA, imageB, multichannel=True)
    m = calculate_mse(imageA, imageB)
    # setup the figure
    fig = plt.figure()
    plt.suptitle("SSIM: %.4f, MSE: %.0f" % (s, m))
    # show first image
    ax = fig.add_subplot(1, 2, 1)
    plt.imshow(imageA, cmap = plt.cm.gray)
    plt.axis("off")
    # show the second image
    ax = fig.add_subplot(1, 2, 2)
    plt.imshow(imageB, cmap = plt.cm.gray)
    plt.axis("off")
    # save figure
    plt.savefig(os.path.join(outdir, 'baseline.jpg'))
    plt.close()
    
    return
    
def tuned_results(imageA, imageC, outdir):
    # compute the mean squared error and structural similarity
    # index for the images
    s = ssim(imageA, imageC, multichannel=True)
    m = calculate_mse(imageA, imageC)
    # setup the figure
    fig = plt.figure()
    plt.suptitle("SSIM: %.4f, MSE: %.0f" % (s, m))
    # show first image
    ax = fig.add_subplot(1, 2, 1)
    plt.imshow(imageA, cmap = plt.cm.gray)
    plt.axis("off")
    # show the second image
    ax = fig.add_subplot(1, 2, 2)
    plt.imshow(imageC, cmap = plt.cm.gray)
    plt.axis("off")
    # save figure
    plt.savefig(os.path.join(outdir, 'tuned.jpg'))
    plt.close()
    
    return
