from urllib.request import urlopen
import zipfile
import numpy as np
from PIL import Image
Image.MAX_IMAGE_PIXELS = None #for big TIFFS
import glob
import rasterio
from rasterio.plot import show

# URL Tutorial Download & Unzipping Files
# https://svaderia.github.io/articles/downloading-and-unzipping-a-zipfile/

# Numpy Working with 0's
# https://stackoverflow.com/questions/21752989/numpy-efficiently-avoid-0s-when-taking-logmatrix

# Read and Show TIFFs
# https://www.kaggle.com/code/yassinealouini/working-with-tiff-files

# url = Link to File
# save_path = path to folder where the file is stored
# file_path = direct path to file

def download_zip(url, save_path):
    filename = url.rsplit('/', 1)[1]
    # Create a new file on the hard drive
    zip_data = open('{}/{}'.format(save_path, filename), "wb")
    # Write the contents of the downloaded file into the new file
    zip_data.write(urlopen(url).read())
    # Close the newly-created file
    zip_data.close()
    print('finish')


def unzipp(url, save_path):
    zipname = url.rsplit('/', 1)[1]
    with zipfile.ZipFile('{}/{}'.format(save_path, zipname), "r") as zip_ref:
        zip_ref.extractall(save_path)
    print('unzipped')


def plotting(save_path):
    path = glob.glob('{}/*.tif'.format(save_path))
    filename = path[0].rsplit('\\', 1)[1]
    file_path = '{}/{}'.format(save_path, filename)
    tif_arr = np.asarray(Image.open(file_path))


    tif_log = 10 * np.log10(tif_arr, out=np.zeros_like(tif_arr), where=(tif_arr != 0))

    tif_result = Image.fromarray(tif_log, mode='F')  # float32
    tif_result.save('{}_log.tif'.format(file_path.rsplit('.', 1)[0]), 'TIFF')
    global result_path
    result_path = '{}_log.tif'.format(file_path.rsplit('.', 1)[0])
    print('finished plotting')


def display_tiff():
    ds = rasterio.open(result_path)
    show((ds, 1), cmap='Greys')
