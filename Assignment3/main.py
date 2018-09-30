import downloader as dw
import os
import sys
import dataToArray as dta

if __name__ == '__main__':
    try:
        _, url, to_file = sys.argv
    except:
        try:
            _, url, = sys.argv
            to_file = os.path.basename(url)
            dw.downloader(url, to_file)
        except Exception as ex:
            print('Error ', ex)
            sys.exit(1)    
    dw.downloader(url, to_file)
    dataSet = dta.dataToArray('NCHS_-_Leading_Causes_of_Death__United_States.csv')
    print(dataSet)