from main import start_program
from pathlib import Path

path = r'Hier den Pfad einfügen'
save_path = Path(r'{}'.format(path))

start_program(save_path)
