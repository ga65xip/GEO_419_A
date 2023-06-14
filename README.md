# GEO 419A Abschlussaufgabe 
  Das Programm ermöglicht das Herunterladen, Entpacken, Lesen, Manipulieren sowie Visualisieren einer TIFF-Datei. Der Fokus dieses Programms liegt hierbei auf der    Automation von redundaten Aufgaben. Zusätzlich wird geprüft, ob die gewollten Schritte bereits ausgeführt wurden und somit nicht aufgeführt werden müssen.

## Vorraussetzungen
Bevor der Code ausgeführt wird, sollten folgende Abhängigkeiten installiert sein:

**'requests'**: Wird für das Herunterladen von Dateien von einer URL verwendet.  
**'tqdm'**: Liefert einen Fortschrittsbalken beim Herunterladen von Dateien.  
**'zipfile'**: Ermöglicht das Extrahieren von Dateien aus einem Zip-Archiv.  
**'numpy'**: Wird für Array-Manipulationen und Berechnungen verwendet.  
**'rasterio'**: Bietet Funktionen für die Arbeit mit GeoTIFF-Dateien.  
**'pathlib'**: Wird für die Bearbeitung von Dateipfaden und Verzeichnisoperationen verwendet.  
**'matplotlib'**: Wird zur Visualisierung der verarbeiteten GeoTIFF-Datei verwendet.  

### Installation
Die Pakete können mit **'conda'** über die die bereitgestellte yml-Datei folgendermaßen installiert werden:

<div style="background-color: #f9f2f4; padding: 10px; border-radius: 5px;">
  
```shell
conda env create -f environment.yml
```

  
## Anwendung
  Das Programm benötigt eine URL zum Downloaden einer Datei. Es entpackt diese wenn nötig und logarithmiert sie. Bei der entpackten Datei muss es sich um eine .tif    handeln, damit das Programm funktioniert.
  Es ist über das Terminal, als auch eine IDE aufrufbar. Zum Ausführen des Programms muss lediglich **'start_program'** Funktion aufgerufen und der Speicherpfad eingegeben werden.  
    
  
  <div style="background-color: #f9f2f4; padding: 10px; border-radius: 5px;">
  
```shell
  if __name__ == '__main__':
    user_input = str(input('Input your save path: '))
    user_save_path = Path(user_input)
    start_program(user_save_path)
 ```

  
  Der Code führt die folgenden Schritte aus:

1) Lädt eine Zip-Datei von einer angegebenen URL herunter, wenn sie im Speicherpfad nicht vorhanden ist.
2) Entpackt die heruntergeladene Datei, wenn die erforderliche GeoTIFF-Datei nicht im Speicherpfad vorhanden ist.
3) Plottet die Daten und erstellt eine log-transformierte GeoTIFF-Datei, wenn die Datei nicht im Speicherpfad vorhanden ist.
4) Zeigt die resultierende GeoTIFF-Datei an.

Das Programm durchläuft diese Schritte in einer Schleife, bis alle erforderlichen Dateien im Speicherpfad vorhanden sind.
  
## Zusätzliche Informationen
  Der Code enthält mehrere Hilfsfunktionen und externe Tutorials als Referenz. Ausführliche Erklärungen und Links zu diesen Tutorials sind in den Kommentaren zum Code zu finden.
