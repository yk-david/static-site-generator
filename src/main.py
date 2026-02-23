from textnode import TextType, TextNode
import os
import shutil


def main():
    copy_static()


def copy_static():
    initialize_public() # Clean initialization of `public`
    
    current_src_path = os.path.join('static')
    current_dst_path = os.path.join('public') # initial path
    src = os.listdir('static') # source directory
    print('now in static folder...', src)
    
    for item in src:
        print('here is current source path:', current_src_path)
        current_item_path = os.path.join(current_src_path, item)
        if os.path.isfile(current_item_path):
            print(f'{item} is a file. now copying...')
            shutil.copy(current_item_path, current_dst_path)
        else:
            print(f'{item} is a folder. now copying...')
            os.makedirs(current_item_path)
            

    dst = os.listdir('public')
    print('now in public folder...', dst)


def initialize_public():
    if os.path.exists('public'):
        print('deleting any existing \'public\' directory...')
        shutil.rmtree('public')
    print('initializing \'public\' directory...')
    os.makedirs('public')


main()
