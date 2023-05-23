from main import download_zip
from main import unzipp
from main import plotting
from main import display_tiff
import os

# Setup für Download und Speicherung
url = 'https://upload.uni-jena.de/data/641c17ff33dd02.60763151/GEO419A_Testdatensatz.zip'
# path niklas
# save_path = 'D:/Studium/GEO_419A Python Kurs/Abschlussaufgabe/Ouput/test'
# path philip
save_path = 'C:/Users/herzu/Documents/GEO419'

# Aufruf der Funktionen

if os.path.exists('{}/.zip'.format(save_path)):
    print('ZIP exist!')
else:
    download_zip(url, save_path)

# download_zip(url, save_path)
# unzipp(url, save_path)
# plotting(save_path)
# display_tiff()
