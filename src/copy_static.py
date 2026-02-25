import os
import shutil


def copy_static(src_path, dst_path):
    src = os.listdir(src_path)
    print('now in static folder...', src)
    
    for item in src:
        print('here is current source path:', src_path)
        current_item_path = os.path.join(src_path, item)
        if os.path.isfile(current_item_path):
            print(f'{item} is a file. now copying...')
            shutil.copy(current_item_path, dst_path)
        else:
            print(f'{item} is a folder. now copying...')
            os.makedirs(os.path.join(dst_path, item))
            copy_static(current_item_path, os.path.join(dst_path, item))
            

def initialize_public():
    if os.path.exists('docs'):
        print('deleting any existing \'public\' directory...')
        shutil.rmtree('docs')
    print('initializing \'public\' directory...')
    os.makedirs('docs')