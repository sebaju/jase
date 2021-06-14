import os
import shutil
import zipfile
import jasrc

def zipit(prefix):
    name = jasrc.conf()['name']
    with zipfile.ZipFile(f'{name}.zip', 'w') as zip:
        for r, d, f in os.walk(prefix):
            for a in f:
                zip.write(os.path.join(r,a), os.path.relpath(os.path.join(r, a), os.path.join(f'{prefix}/assets', '..')))

    shutil.rmtree(prefix)

    if jasrc.tempconf()[1] == 'True':
        shutil.move(f'{name}.zip', jasrc.conf()['mcf'])

