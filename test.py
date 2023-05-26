from main import start_program
from pathlib import Path
# Setup für Download und Speicherung
# Philip
# save_path = 'C:/Users/herzu/Documents/GEO419'
# Niklas
path = r'D:\Studium\GEO_419A Python Kurs\Abschlussaufgabe\Ouput\test'
save_path = Path(r'{}'.format(path))
start_program(save_path)
