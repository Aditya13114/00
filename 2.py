import csv 
import plotly.express as px

with open("1.csv") as f:
    df = csv.DictReader(f)

    #for row in df:
        #print(row)

    fig = px.scatter(df, x= "Roll No", y= "Days Present")
    fig.show()


with open("2.csv") as f:
    df = csv.DictReader(f)

    #for row in df:
        #print(row)

    fig = px.scatter(df, x = "Coffee in ml", y = "sleep in hours")
    fig.show()




 