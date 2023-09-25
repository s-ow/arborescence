# Arborescence

Ce petit programme est un outil qui permet de lister les fichiers et les dossiers sous forme d'arbre.    
Vous pouvez également choisir de n'analyser que le dossier et pas les sous-dossiers. *(voir `--shallow` à la fin du README)*

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
__Exemple :__  `python C:\Users\sacha\Desktop\projets-python\arborescence\main.py C:\Users\sacha\Downloads\meteo-main`    
![](https://i.imgur.com/fWUfccQ.png)

- Pour analyser uniquement le dossier et non les sous dossiers :
> Utilisez `--shallow` à la fin de votre commande.    
__Exemple :__ `python C:\Users\sacha\Desktop\projets-python\arborescence\main.py C:\Users\sacha\Downloads\meteo-main --shallow`     
![](https://i.imgur.com/o5XYe6S.png)
