import zipfile
import os

for root, dirs, files, in os.walk('input'):
    for file in files:
        if file.endswith('.osz'):
            oszFilePath = os.path.join(root, file)
            oszFile = os.path.join(file)
            with zipfile.ZipFile(os.path.join(root, file)) as zf:
                for file in zf.namelist():
                    if file[-4:] == ".mp3" or file[-4:] == ".ogg":
                        neededFiles = []
                        neededFiles.append(file)
                        print(neededFiles)
                        zf.extract(''.join(neededFiles), oszFile);
            os.remove(oszFilePath)
        else:
            print('No .osz files found')
