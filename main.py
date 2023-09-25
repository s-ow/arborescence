import os
import sys

BLEU = "\033[36m"
MAGENTA = "\033[35m"
RESET = "\033[0m"

def arbo(path, niveau=0):
    # Parcourir le répertoire
    try:
        for fichier in os.listdir(path):

            full_path = os.path.join(path, fichier)

            if os.path.isdir(full_path):

                # Afficher le nom du répertoire
                print("    " * niveau + BLEU + "\u21b3 " + os.path.basename(fichier) + "/" + RESET)

                # Appeler arbo dans le répertoire trouvé
                arbo(full_path, niveau + 1)

        # Parcourir les fichiers
        for fichier in os.listdir(path):
            full_path = os.path.join(path, fichier)
            if os.path.isfile(full_path):

                # Afficher le nom du fichier
                print("    " * niveau + MAGENTA + "\u2192 " + os.path.basename(fichier) + RESET)
    except:
        pass

# Exécution du programme
if len(sys.argv) != 2:
    directory = os.getcwd()
else:
    directory = sys.argv[1]

if os.path.exists(directory):
    print(f"\n\n{directory}")

    arbo(directory)

    print("\n\n")
else:
    print("\nCe dossier n'existe pas.\n")