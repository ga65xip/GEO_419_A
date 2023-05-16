from main import download_zip
from main import unzipp

url = 'https://upload.uni-jena.de/data/641c17ff33dd02.60763151/GEO419A_Testdatensatz.zip'
save_path = 'D:/Studium/GEO_419A Python Kurs/Abschlussaufgabe/Ouput/test'
filename = url.rsplit('/', 1)[1]
filename_no_type = filename.split('.', 1)[0]

#download_zip(url, save_path)
unzipp(save_path, filename)
