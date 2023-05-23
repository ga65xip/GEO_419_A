import requests
from tqdm import tqdm
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

# Added Progress Bar
# https://stackoverflow.com/questions/37573483/progress-bar-while-download-file-over-http-with-requests

# Numpy Working with 0's
# https://stackoverflow.com/questions/21752989/numpy-efficiently-avoid-0s-when-taking-logmatrix

# Read and Show TIFFs
# https://www.kaggle.com/code/yassinealouini/working-with-tiff-files

# url = Link to File
# save_path = path to folder where the file is stored
# file_path = direct path to file

def download_zip(url, save_path):
    zipname = url.split("/")[-1]
    block_size = 1024  # 1 Kibibyte
    print(f"Downloading {zipname}...")
    site = urlopen(url)
    meta = site.info()
    # Streaming, so we can iterate over the response.
    response = requests.get(url, stream=True)
    total_size_in_bytes = int(meta["Content-Length"])
    progress_bar = tqdm(total=total_size_in_bytes, unit='iB', unit_scale=True)
    with open('{}/{}'.format(save_path, zipname), "wb") as file:
        for data in response.iter_content(block_size):
            progress_bar.update(len(data))
            file.write(data)
    progress_bar.close()
    print("Download complete!")


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