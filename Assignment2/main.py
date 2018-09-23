import helpers as hp
import os
import sys


if __name__ == '__main__':
    try:
        _, url, to_file = sys.argv
    except:
        try:
            _, url, = sys.argv
            to_file = os.path.basename(url)
            hp.download(url, to_file)
        except Exception as ex:
            print('Error ', ex)
            sys.exit(1)    
    hp.download(url, to_file)
    #linesOfData = len(hp.textToJson('BobRoss.txt'))
    jsonData = hp.textToJson('BobRoss.txt')
    print("How many lines does the .txt file have? = ", len(jsonData))
    print("How many times does the .txt file write RUINED ? ", hp.amountRuined(jsonData))    