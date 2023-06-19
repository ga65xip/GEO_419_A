import requests
from tqdm import tqdm
import zipfile
import numpy as np
import rasterio
from pathlib import Path
import matplotlib.pyplot as plt

# Tutorial Download
# https://svaderia.github.io/articles/downloading-and-unzipping-a-zipfile/

# Tutorial Unzip
# https://stackoverflow.com/questions/3451111/unzipping-files-in-python

# Working with pathlib
# https://pathlib.readthedocs.io/en/pep428/

# Added Progress Bar
# https://stackoverflow.com/questions/37573483/progress-bar-while-download-file-over-http-with-requests

# Numpy Working with 0's
# https://stackoverflow.com/questions/21752989/numpy-efficiently-avoid-0s-when-taking-logmatrix

# Read and Show TIFFs
# https://www.kaggle.com/code/yassinealouini/working-with-tiff-files


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
    zip_name = Path(url).name  # get zip name from URL
    block_size = 1024  # 1 Kibibyte
    print(f'Downloading {zip_name}...')
    response = requests.get(url, stream=True)
    response.raise_for_status()  # check if the request was successful
    total_size_in_bytes = int(response.headers.get('content-length', 0))
    progress_bar = tqdm(total=total_size_in_bytes, unit='iB', unit_scale=True)
    with open(save_path / zip_name, 'wb') as file:
        for data in response.iter_content(block_size):
            progress_bar.update(len(data))
            file.write(data)
    progress_bar.close()
    print('Download complete!')  # print after completing function
    download_zip_path = save_path / zip_name  # define output
    return download_zip_path


def unzip(zip_file, save_path):
    """
    Extract files from ZipFile.

    Parameters
    ----------
    zip_file: Path
        Path to the ZipFile.
    save_path: Path
        Location to extract the files.

    Returns
    -------
    None
    """
    # open zipfile and extract to save path
    with zipfile.ZipFile(zip_file, 'r') as zip_ref:
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
    log_file_path: Path
        The path to the created manipulated tif file.
    """
    # create file path
    file_path = next(save_path.glob('*.tif'))

    # open file with rasterio as numpy array
    with rasterio.open(file_path) as src:
        tif_arr = src.read(1)
        profile = src.profile

    tif_log = 10 * np.log10(tif_arr, where=(tif_arr != 0))  # log10 without zeros
    tif_log = np.where(tif_log == 0, -999, tif_log)  # set zeros/NaN to -999
    log_file_name = f'{Path(file_path).stem}_log.tif'  # define output name & path
    log_file_path = save_path / log_file_name
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
        Location of the previously calculated log file.

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
        Indicating if the program execution is completed.

    Returns
    -------
    None

    Notes
    -----
    This function performs the following steps:
    1. Downloads a zip file from a specified url if it doesn't exist in the save_path.
    2. Unzips the downloaded file if the required tif file doesn't exist in the save_path.
    3. Plots the data and creates a log-transformed tif file if the file doesn't exist in the save_path.
    4. Displays the resulting tif file.

    The function loops through these steps until finished is True.
    """
    # create setup variables
    url = 'https://upload.uni-jena.de/data/641c17ff33dd02.60763151/GEO419A_Testdatensatz.zip'
    zip_name = Path(url).name
    zip_file = save_path / zip_name
    geotif = save_path / 'S1A_IW_20230214T031857_DVP_RTC10_G_gpunem_A42B_VH.tif'
    result = save_path / 'S1A_IW_20230214T031857_DVP_RTC10_G_gpunem_A42B_VH_log.tif'

    # iterate over functions until finished is true
    while not finished:
        if not zip_file.exists():  # check for existence of file
            print('Downloading ZIP!')
            download_zip(url, save_path)
        elif not geotif.exists():
            print('Unzipping needed!')
            unzip(zip_file, save_path)
        elif not result.exists():
            print('Plotting needed!')
            plotting(save_path)
        else:
            finished = True
            print('Displaying result!')  # print when finished
            display_tif(result)


# main block
if __name__ == '__main__':
    user_input = str(input('Input your save path: '))
    user_save_path = Path(user_input)
    start_program(user_save_path)
