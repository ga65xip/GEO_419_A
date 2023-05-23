from main import download_zip
from main import unzipp


#Setup für Download und Speicherung
url = 'https://upload.uni-jena.de/data/641c17ff33dd02.60763151/GEO419A_Testdatensatz.zip'
#path niklas
save_path = 'D:/Studium/GEO_419A Python Kurs/Abschlussaufgabe/Ouput/test'
#path philip
#save_path = 'C:/Users/herzu/Documents/GEO419'

filename = url.rsplit('/', 1)[1]
filename_no_type = filename.split('.', 1)[0]

#Aufruf der Funktionen

#download_zip(url, save_path)
unzipp(save_path, filename)
