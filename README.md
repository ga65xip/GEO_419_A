# GEO 419A Abschlussaufgabe 
  Das Programm ermöglicht das Herunterladen, Entpacken, Lesen, Manipulieren sowie Visualisieren einer TIFF-Datei. Der Fokus dieses Programms liegt hierbei auf der    Automation von redundaten Aufgaben. Zusätzlich wird geprüft, ob die gewollten Schritte bereits ausgeführt wurden und somit nicht aufgeführt werden müssen.

## Installation
<div style="background-color: #f9f2f4; padding: 10px; border-radius: 5px;">
  
```shell
  conda env create -f GEO419A.yml
  <button onclick="navigator.clipboard.writeText('conda env create -f environment.yml')">Kopieren</button>

</div>

  
## Anwendung
  Das Programm benötigt ein URL zum Downloaden einer Datei. Es entpackt diese wenn nötig und logarithmiert sie. Bei der entpackten Datei muss es sich um eine .tif    handeln, damit das Programm funktioniert.
  Es ist über das Terminal, als auch eine IDE aufrufbar.
