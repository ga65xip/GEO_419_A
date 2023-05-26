import requests
from tqdm import tqdm
from urllib.request import urlopen
import zipfile
import numpy as np
import glob
import rasterio
from pathlib import Path
import matplotlib.pyplot as plt

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
    zip_name = url.split('/')[-1]  # get zip name from Path
    block_size = 1024  # 1 Kibibyte
    print(f'Downloading {zip_name}...')
    site = urlopen(url)
    meta = site.info()
    # Streaming, so we can iterate over the response and add progress bar
    response = requests.get(url, stream=True)
    total_size_in_bytes = int(meta['Content-Length'])
    progress_bar = tqdm(total=total_size_in_bytes, unit='iB', unit_scale=True)
    with open('{}/{}'.format(save_path, zip_name), 'wb') as file:
        for data in response.iter_content(block_size):
            progress_bar.update(len(data))
            file.write(data)
    progress_bar.close()
    print('Download complete!')  # print after completing Function


def unzip(url, save_path):
    zip_name = url.rsplit('/', 1)[1]
    # open zipfile and extract to save path
    with zipfile.ZipFile('{}/{}'.format(save_path, zip_name), 'r') as zip_ref:
        zip_ref.extractall(save_path)
    print('Unzipped!')  # print after completing Function


def plotting(save_path):
    # create setup variables
    path = glob.glob('{}/*.tif'.format(save_path))
    filename = path[0].rsplit('\\', 1)[1]
    file_path = '{}/{}'.format(save_path, filename)
    # open file with rasterio as numpy array
    with rasterio.open(file_path) as src:
        tif_arr = src.read(1)
        profile = src.profile
    # write and save manipulated tif
    tif_log = 10 * np.log10(tif_arr, out=np.zeros_like(tif_arr), where=(tif_arr != 0))  #
    tif_log = np.where(tif_log == 0, -999, tif_log)
    log_file_path = '{}_log.tif'.format(file_path.rsplit('.', 1)[0])
    profile.update(dtype=rasterio.float32, count=1)
    with rasterio.open(log_file_path, 'w', **profile) as dst:
        dst.write(tif_log, 1)
    print('Finished calculating!')  # print after completing Function


def display_tiff(result):
    ds = rasterio.open(result)
    fig, ax = plt.subplots()
    im = ax.imshow(ds.read(1), cmap='Greys', vmin=-50, vmax=15, extent=(ds.bounds.left, ds.bounds.right,
                                                                        ds.bounds.bottom, ds.bounds.top))
    ax.set_xlabel('X Coordinate')
    ax.set_ylabel('Y Coordinate')
    fig.colorbar(im, ax=ax, label='VH-Backscatter [dB]')
    plt.show()


def start_program(save_path):
    url = 'https://upload.uni-jena.de/data/641c17ff33dd02.60763151/GEO419A_Testdatensatz.zip'
    zip_name = url.rsplit('/', 1)[1]
    zip_file = Path('{}/{}'.format(save_path, zip_name))
    geotif = Path(r'{}/S1A_IW_20230214T031857_DVP_RTC10_G_gpunem_A42B_VH.tif'.format(save_path))
    result = Path(r'{}/S1A_IW_20230214T031857_DVP_RTC10_G_gpunem_A42B_VH_log.tif'.format(save_path))
    finished = 'false'

    while finished != 'true':
        if not zip_file.is_file():
            print('Download ZIP!')
            download_zip(url, save_path)
        elif not geotif.is_file():
            print('Unzip needed!')
            unzip(url, save_path)
        elif not result.is_file():
            print('Plotting needed!')
            plotting(save_path)
        else:
            finished = 'true'
            print('Display result!')
            display_tiff(result)


if __name__ == "__main__":
    text = str(input("Input your save path: "))
    start_program(text)
