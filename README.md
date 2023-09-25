# Arborescence

Ce petit programme est un outil qui permet de lister les fichiers et les dossiers sous forme d'arbre.    
Pour l'instant, il liste **tous** les sous-dossiers et fichiers trouvés dans le chemin d'accès donné, je pense faire bientôt une fonction qui permettra de choisir si il affiche uniquement les sous dossiers ou également ce qu'ils contiennent, car on ne cherche pas toujours à voir tous les fichiers, et il y en a parfois des cachés, ce qui peut prendre de la place.

## Utilisation
Pour lancer le script, deux options s'offrent à vous :
- Directement dans le chemin d'accès à analyser :
> Si vous vous trouvez déjà dans le dossier à analyser dans votre invite de commandes, utilisez simplement :   
`python <chemin du programme>`   
__Exemple :__ `python C:\Users\sacha\Desktop\projets-python\arborescence\main.py`    
![](https://i.imgur.com/qyCdvtf.png)

- Dans un dossier quelconque :
> Si vous vous trouvez dans un dossier quelconque et voulez analyser un dossier précis, vous pouvez utiliser :    
`python <chemin du programme> <chemin du dossier à analyser>`    
__Exemple:__  `python C:\Users\sacha\Desktop\projets-python\arborescence\main.py C:\Users\sacha\Downloads\meteo-main`    
![](https://i.imgur.com/fWUfccQ.png)