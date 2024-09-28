import zipfile
import os

audio = 'audio.mp3'

for root, dirs, files, in os.walk('input'):
    for file in files:
        if file.endswith('.osz'):
            os.makedirs(os.path.join(file))
            with zipfile.ZipFile(os.path.join(root, file)) as zf:
                for name in zf.namelist():
                    if audio in zf.namelist():
                        zf.extract(audio, os.path.join(file))
                    else:
                        zf.extract('audio.ogg', os.path.join(file))
            os.remove(os.path.join(root, file))