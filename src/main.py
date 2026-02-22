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
            print(f'copying folder...', path)
            os.makedirs(f'public/{item}')
            src = os.listdir(f'static/{item}')
            # print('current path:', path)
            print('current src', src)

    dst = os.listdir('public')
    print('now in public folder...', dst)


main()
