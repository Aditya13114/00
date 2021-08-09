import csv
import plotly.express as px
import numpy as np

def getDataSource(data_path):
    marksinpercentage = []
    dayspresent = []

    with open(data_path) as f:
        csv_reader = csv.DictReader(f)

        for row in csv_reader:
            marksinpercentage.append(float(row["Marks In Percentage"]))
            dayspresent.append(float(row["Days Present"]))

    return{'x':marksinpercentage, 'y':dayspresent}

def calculateCorelation(data_source):
    c = np.corrcoef(data_source['x'],data_source['y'])
    #print(c)
    print(c[0,1])

def setup():
    data_path = "marks.csv"

    dataSource = getDataSource(data_path)
    calculateCorelation(dataSource)


setup()

        
