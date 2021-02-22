import pandas as pd
from sklearn.model_selection import train_test_split
import numpy as np

iris = pd.read_csv("iris.csv")
contagem_classes = iris['class'].value_counts()

x, _, y, _ = train_test_split(iris.iloc[:,0:4], iris.iloc[:,4], test_size = 0.5, stratify = iris.iloc[:,4])

yValueCounts = y.value_counts()



#Amostragem Estratificada - Base: Infert
infert = pd.read_csv('infert.csv')
contagem_education = infert['education'].value_counts()

p1 =  int((120 / 248)*100)
p2 = int((116 / 248)*100)
p3 = int((12 / 248)*100)

x1, _, y1, _ = train_test_split(infert.iloc[:, 2:9], infert.iloc[:,1], test_size = 0.6, stratify = infert.iloc[:,1])
contagem_education_nova = y1.value_counts()
