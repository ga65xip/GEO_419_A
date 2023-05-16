from urllib.request import urlopen
import zipfile

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


url = 'https://upload.uni-jena.de/data/641c17ff33dd02.60763151/GEO419A_Testdatensatz.zip'
save_path = 'D:/Studium/GEO_419A Python Kurs/Abschlussaufgabe/Ouput/test'
filename = url.rsplit('/', 1)[1]



