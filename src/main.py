from textnode import TextType, TextNode
import os
import shutil


def main():
    copy_static()


def copy_static():
    if os.path.exists('public'):
        print('deleting any existing \'public\' directory...')
        shutil.rmtree('public')
    print('initializing \'public\' directory...')
    os.makedirs('public')

    src = os.listdir('static')
    print('now in static folder...', src)
    for item in src:
        path = os.path.join('static', item)
        print(f'is {item} a file? checking....', os.path.isfile(path))
        if os.path.isfile(path):
            print(f'copying {item}...')
            shutil.copy(path, 'public')
        else:
            path = os.path.join(path, item)

    dst = os.listdir('public')
    print('now in public folder...', dst)


main()
