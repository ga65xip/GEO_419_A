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
    """
    Download ZipFile from url and save to path.

    Parameters
    ----------
    url: str
        Link to download file.
    save_path: Path
        Location to store the file.

    Returns
    -------
    result_download_zip: Path
        Location of ZipFile.
    """
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
    print('Download complete!')  # print after completing function
    download_zip_path = Path(r'{}/{}'.format(save_path, zip_name))  # define output
    return download_zip_path


def unzip(url, save_path):
    """
    Extract files from ZipFile.

    Parameters
    ----------
    url: str
        Extract folder name.
    save_path: Path
        Location to folder.

    Returns
    -------
    None
    """
    zip_name = url.rsplit('/', 1)[1]
    # open zipfile and extract to save path
    with zipfile.ZipFile('{}/{}'.format(save_path, zip_name), 'r') as zip_ref:
        zip_ref.extractall(save_path)
    print('Unzipped!')  # print after completing function


def plotting(save_path):
    """
    Load tif as array, perform calculations, write to new tif.

    Parameters
    ----------
    save_path: Path
        Location to folder.

    Returns
    -------

    """
    # create setup variables
    path = glob.glob('{}/*.tif'.format(save_path))  # searching for tif file in folder
    filename = path[0].rsplit('\\', 1)[1]
    file_path = '{}/{}'.format(save_path, filename)

    # open file with rasterio as numpy array
    with rasterio.open(file_path) as src:
        tif_arr = src.read(1)
        profile = src.profile
    # write and save manipulated tif
    tif_log = 10 * np.log10(tif_arr, out=np.zeros_like(tif_arr), where=(tif_arr != 0))  # log10 without zeros
    tif_log = np.where(tif_log == 0, -999, tif_log)  # set zeros/NaN to -999
    log_file_path = Path('{}_log.tif'.format(file_path.rsplit('.', 1)[0]))  # define output name & path
    profile.update(dtype=rasterio.float32, count=1)
    with rasterio.open(log_file_path, 'w', **profile) as dst:
        dst.write(tif_log, 1)
    print('Finished calculating!')  # print after completing function
    return log_file_path


def display_tif(result):
    """
    Display tif using matplotlib.

    Parameters
    ----------
    result: Path
        Location of previous calculated log file

    Returns
    -------
    None
    """
    # open tif and display result
    tif = rasterio.open(result)
    fig, ax = plt.subplots()
    image = ax.imshow(tif.read(1), cmap='Greys', vmin=-50, vmax=15, extent=(tif.bounds.left, tif.bounds.right,
                                                                            tif.bounds.bottom, tif.bounds.top))
    ax.set_xlabel('X Coordinate')
    ax.set_ylabel('Y Coordinate')
    fig.colorbar(image, ax=ax, label='VH-Backscatter [dB]')
    plt.show()


def start_program(save_path, finished=False):
    """
    Executes the previously created functions if needed, otherwise skip the function.

    Parameters
    ----------
    save_path: Path
        User defined Input to store the files.
    finished: bool, optional
        Flag indicating if the program execution is completed. Default is False.

    Returns
    -------
    bool
        True if the program execution is completed, False otherwise.
    """

    # create setup variables
    url = 'https://upload.uni-jena.de/data/641c17ff33dd02.60763151/GEO419A_Testdatensatz.zip'
    zip_name = url.rsplit('/', 1)[1]
    zip_file = Path('{}/{}'.format(save_path, zip_name))
    geotif = Path(r'{}/S1A_IW_20230214T031857_DVP_RTC10_G_gpunem_A42B_VH.tif'.format(save_path))
    result = Path(r'{}/S1A_IW_20230214T031857_DVP_RTC10_G_gpunem_A42B_VH_log.tif'.format(save_path))

    # iterate over functions until finished is true
    while not finished:
        if not zip_file.is_file():  # check for existence of file
            print('Download ZIP!')
            download_zip(url, save_path)
        elif not geotif.is_file():
            print('Unzip needed!')
            unzip(url, save_path)
        elif not result.is_file():
            print('Plotting needed!')
            plotting(save_path)
        else:
            finished = True
            print('Display result!')  # print when finished
            display_tif(result)

    return finished


# main block
if __name__ == "__main__":
    text = str(input("Input your save path: "))
    user_save_path = Path(r'{}'.format(text))
    start_program(user_save_path)
