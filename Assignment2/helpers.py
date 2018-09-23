import requests as req
import os 
import sys
from collections import Counter
import re 

def textToJson(textData):
    jsonData = []
    with open(textData, 'r', encoding='utf8') as readFile:

        for text in readFile:
            textLine = text.rstrip(os.linesep)
            splitTwo = textLine.split(" ", 2)
            splitTimeStamp, splitName, splitMsg = splitTwo
            jsonObject = {
                "timestamp": splitTimeStamp,
                "name":splitName[:-1],
                "message":splitMsg
            }
            jsonData.append(jsonObject)
    return jsonData


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

def amountRuined(textToJson):
    amount = 0
    for data in textToJson:
        textLine = data['name'] + ' ' + data['message']
        listOfWords = textLine.split(' ')
        for word in listOfWords:
            if "ruined" in word.lower():
                amount+=1
    return amount

def uniqueUsers(textToJson):
    amount = len(set([data['name'] for data in textToJson]))
    return amount

def mostUsedWord(textToJson):
    wordAmount = {}
    for textLine in textToJson:
        for word in textLine['message'].split(" ")[1:]:
            word = word.replace("â€˜","")
            word = word.replace("!","")
            word = word.replace("â€œ","")
            word = word.replace(".","")
            word = word.replace(":","")
            word = word.replace("\"","")
            word = word.replace("*","")
            word = word.replace(",","")
            
            wordAmount[word] = wordAmount.get(word, 0) + 1

    wordCounter = Counter(wordAmount)
    return wordCounter.most_common(1)[0]