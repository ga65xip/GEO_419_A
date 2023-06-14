# GEO 419A Abschlussaufgabe 
  Das Programm ermöglicht das Herunterladen, Entpacken, Lesen, Manipulieren sowie Visualisieren einer TIFF-Datei. Der Fokus dieses Programms liegt hierbei auf der    Automation von redundaten Aufgaben. Zusätzlich wird geprüft, ob die gewollten Schritte bereits ausgeführt wurden und somit nicht aufgeführt werden müssen.

## Installation und Vorraussetzungen
Bevor der Code ausgeführt wird, sollten folgende Abhängigkeiten installiert sein:

**'requests'**: Wird für das Herunterladen von Dateien von einer URL verwendet.  
**'tqdm'**: Liefert einen Fortschrittsbalken beim Herunterladen von Dateien.  
**'zipfile'**: Ermöglicht das Extrahieren von Dateien aus einem Zip-Archiv.  
**'numpy'**: Wird für Array-Manipulationen und Berechnungen verwendet.  
**'rasterio'**: Bietet Funktionen für die Arbeit mit GeoTIFF-Dateien.  
**'pathlib'**: Wird für die Bearbeitung von Dateipfaden und Verzeichnisoperationen verwendet.  
**'matplotlib'**: Wird zur Visualisierung der verarbeiteten GeoTIFF-Datei verwendet.  


Die Pakete können über die die bereitgestellte yml-Datei folgendermaßen installiert werden:

<div style="background-color: #f9f2f4; padding: 10px; border-radius: 5px;">
  
```shell
conda env create -f environment.yml
```

  
## Anwendung
  Das Programm benötigt eine URL zum Downloaden einer Datei. Es entpackt diese wenn nötig und logarithmiert sie. Bei der entpackten Datei muss es sich um eine .tif    handeln, damit das Programm funktioniert.
  Es ist über das Terminal, als auch eine IDE aufrufbar.
  
## Zusätzliche Informationen
  Der Code enthält mehrere Hilfsfunktionen und externe Tutorials als Referenz. Ausführliche Erklärungen und Links zu diesen Tutorials sind in den Kommentaren zum Code zu finden.
