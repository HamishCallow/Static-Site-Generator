import os
import shutil

def copy_static(source, dest):
    if os.path.exists(dest):
        shutil.rmtree(dest)
    os.mkdir(dest)
    for content in os.listdir(source):
        source_path = os.path.join(source, content)
        dest_path = os.path.join(dest, content)
        if os.path.isfile(source_path):
            shutil.copy(source_path, dest_path)
        else:
            os.mkdir(dest_path)
            copy_static(source_path, dest_path)

