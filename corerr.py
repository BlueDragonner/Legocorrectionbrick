#made by BlueDragonner
#id Discord bluedragon0002 if you have any question
#V1.0
import zipfile
import os
from tkinter import Tk, filedialog

def unzip_and_modify():
    # Ouvrir une fenêtre de dialogue pour sélectionner le fichier .io
    root = Tk()
    root.withdraw()
    io_file_path = filedialog.askopenfilename(title="Sélectionnez un fichier .io", filetypes=[("IO Files", "*.io")])

    if not io_file_path:
        print("Aucun fichier sélectionné.")
        return

    # Définir les chemins d'extraction
    extract_path = os.path.splitext(io_file_path)[0] + "_extracted"
    if not os.path.exists(extract_path):
        os.makedirs(extract_path)

    # Extraire le fichier .io
    with zipfile.ZipFile(io_file_path, 'r') as zip_ref:
        zip_ref.extractall(extract_path)
    
    # Chemins des fichiers à modifier
    model2_ldr_path = os.path.join(extract_path, "model2.ldr")
    modelv2_ldr_path = os.path.join(extract_path, "modelv2.ldr")

    # Modifier model2.ldr
    if os.path.exists(model2_ldr_path):
        with open(model2_ldr_path, 'r') as file:
            data = file.read()
        data = data.replace('rename_3023', '3023')
        with open(model2_ldr_path, 'w') as file:
            file.write(data)

    # Modifier modelv2.ldr
    if os.path.exists(modelv2_ldr_path):
        with open(modelv2_ldr_path, 'r') as file:
            data = file.read()
        data = data.replace('3023.', '3023b.')
        with open(modelv2_ldr_path, 'w') as file:
            file.write(data)

    # Recompresser le dossier modifié en un nouveau fichier .io
    modified_io_file_path = os.path.splitext(io_file_path)[0] + "_modified.io"
    with zipfile.ZipFile(modified_io_file_path, 'w') as zipf:
        for root, dirs, files in os.walk(extract_path):
            for file in files:
                file_path = os.path.join(root, file)
                arcname = os.path.relpath(file_path, extract_path)
                zipf.write(file_path, arcname)

    print(f"Modifications complétées. Fichier enregistré sous {modified_io_file_path}")

# Appeler la fonction pour exécuter le processus
unzip_and_modify()
