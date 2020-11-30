import plotly.express as px
import csv
import numpy as np

def plotFigure(data_path):
    with open(data_path) as csv_file:
        df = csv.DictReader(csv_file)
        fig= px.scatter(df,x= "Roll No", y= "Marks In Percentage")
        
        fig.show()

def getDataSource(data_path):
    Marks_In_Percenatge = []
    Days_Present = []
    with open(data_path) as csv_file: 
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            Marks In Percentage.append(float(row["Rooll No"]))
            Days Present.append(float(row["Marks In Percentage"]))

    return{"x": Marks_In_Percenatge  , "y": Days_Present}

def findCorrelation(dataSource):
    correlation= np.corrcoef(dataSource["x"],dataSource["y"])

    print("Correlation: ", correlation[0,1])

def setup():
    data_path= "./Student Marks vs Days Present.csv"
    dataSource= getDataSource(data_path)
    findCorrelation(dataSource)

setup()


