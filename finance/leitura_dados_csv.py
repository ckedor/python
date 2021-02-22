# -*- coding: utf-8 -*-
"""
Created on Tue Jun  2 19:21:00 2020

@author: ChristianKedor
"""

import pandas as pd

#Uma forma para formatar a data do CSV (como vai ser lido)
#date_parser_1 = lambda x: pd.datetime.strptime(x, "%Y.%m.%d %H:%M")
#mydata = pd.read_csv("VALE3H1.csv", sep=',', parse_dates=[0], date_parser=date_parser_1)


diretorio_dados = "D:\\Studies\\Udemy - Python para Finanças\\Dados\\"

header_names = ["Datetime", "Open", "High", "Low", "Close", "Volume", "Tick Volume"]
vale3h1 = pd.read_csv(diretorio_dados+ "VALE3H1.csv", names=header_names)

data_02 = pd.read_csv(diretorio_dados + "Data_02.csv", index_col='Date')
data_03 = pd.read_excel(diretorio_dados + "Data_03.xlsx")
data_03 = data_03.set_index('Year')


