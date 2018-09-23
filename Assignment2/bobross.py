import helpers as hp
import os
import sys


def main():
    bobRossURL = input('Hello Link the Bob Ross Txt Here ')
    hp.download(bobRossURL)
    

if __name__ == '__main__':
    try:
        _, to_file = sys.argv
    except:
        try:
            _, url, = sys.argv
            to_file = os.path.basename(url)
            hp.download(url, to_file)
        except Exception as ex:
            print('Error ', ex)
            sys.exit(1)    
    hp.download(url, to_file)