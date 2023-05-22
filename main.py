from urllib.request import urlopen
import zipfile
import numpy as np
from PIL import Image
Image.MAX_IMAGE_PIXELS = None #for big TIFFS
import glob
import rasterio
from rasterio.plot import show

# URL Tutorial
#https://svaderia.github.io/articles/downloading-and-unzipping-a-zipfile/


def download_zip(url, save_path):
    filename = url.rsplit('/', 1)[1]
    # Create a new file on the hard drive
    zip_data = open('{}/{}'.format(save_path, filename), "wb")
    # Write the contents of the downloaded file into the new file
    zip_data.write(urlopen(url).read())
    # Close the newly-created file
    zip_data.close()
    print('finish')


def unzipp(path, filename):
    with zipfile.ZipFile('{}/{}'.format(path, filename), "r") as zip_ref:
        zip_ref.extractall(path)
    print('unzipped')


def plotting(save_path):
    path = glob.glob('{}/*.tif'.format(save_path))
    filename = path[0].rsplit('\\', 1)[1]
    speichername = '{}/{}'.format(save_path, filename)
    tif_arr = np.asarray(Image.open(speichername))

    # https://stackoverflow.com/questions/21752989/numpy-efficiently-avoid-0s-when-taking-logmatrix
    tif_log = 10 * np.log10(tif_arr, out=np.zeros_like(tif_arr), where=(tif_arr != 0))

    tif_result = Image.fromarray(tif_log, mode='F')  # float32
    tif_result.save('{}_log.tif'.format(speichername.rsplit('.', 1)[0]), 'TIFF')

def display_tiff(save_path):
    ds = rasterio.open(save_path)
    show((ds, 1), cmap='Greys')