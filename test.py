from main import download_zip
from main import unzipp
from main import plotting
from main import display_tiff


#Setup für Download und Speicherung
#url = 'https://upload.uni-jena.de/data/641c17ff33dd02.60763151/GEO419A_Testdatensatz.zip'
#path niklas
#save_path = 'D:/Studium/GEO_419A Python Kurs/Abschlussaufgabe/Ouput/test'
#path philip
save_path = 'C:/Users/herzu/Documents/GEO419/S1A_IW_20230214T031857_DVP_RTC10_G_gpunem_A42B_VH_log.tif'

#filename = url.rsplit('/', 1)[1]
#filename_no_type = filename.split('.', 1)[0]

#Aufruf der Funktionen

#download_zip(url, save_path)
#unzipp(save_path, filename)
#plotting(save_path)
display_tiff(save_path)