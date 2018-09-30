import csv

def dataToArray(file):
    with open(file) as fp:
        csvReader = csv.reader(fp)
        next(csvReader)
        data = []
        for textLine in csvReader:
            year, _, cause, state, death, _ = textLine
            year, death, = int(year), int(death)
            if state != "United States":
                    data.append([year, cause, state, death])
    return data