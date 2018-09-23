import requests as req
import os 
import sys

# Downloads file 
def download(from_url, to_file):
    if not os.path.isfile(to_file):
        try:
            requestText = req.get(from_url, to_file)
            string_text = requestText.text
            print("File Download Startet")

            with open(to_file, 'w', encoding='utf8', newline='') as reqFile:
                reqFile.write(string_text)
        except Exception as ex:
            print('Could not download file: ', ex)
            sys.exit(1)
        print('Finished Downloading File ')
    #downloadURL = req.urlretrieve(bobRossURL, ) 

