import pandas as pd
import numpy as np
from collections import Counter
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['Kaiti']

class Groundwater_assessment(object):
    def __init__(self,input_file_name,output_file_name,inputsheetname):
        self.input_file_name = input_file_name
        self.output_file_name = output_file_name
        self.inputsheetname = inputsheetname

    def water_assess(self):#2017标准
        groundwater_data = pd.read_excel(self.input_file_name, sheet_name=self.inputsheetname, index_col=0,header=0)
        colsl = []
        for cols in groundwater_data.columns[:]:
            if cols == u'pH':
                for col in list(groundwater_data[cols].iloc[:]):
                    if col >= 6.5 and col <= 8.5:
                        col = 1
                    elif col >= 5.5 and col < 6.5:
                        col = 4
                    elif col > 8.5 and col <= 9.0:
                        col = 4
                    else:
                        col = 5
                    colsl.append(col)
            elif cols == u'总大肠菌群':
                for col in list(groundwater_data[cols].iloc[:]):
                    if col <= 3:
                        col = 1
                    elif col > 3 and col <= 100:
                        col = 4
                    else:
                        col = 5
                    colsl.append(col)
            if cols == u'菌落总数':
                for col in list(groundwater_data[cols].iloc[:]):
                    if col <= 100:
                        col = 1
                    elif col > 100 and col <= 1000:
                        col = 4
                    else:
                        col = 5
                    colsl.append(col)

            if cols == u'色度':
                for col in list(groundwater_data[cols].iloc[:]):
                    if col <= 5:
                        col = 1
                    elif col > 5 and col <= 15:
                        col = 3
                    elif col > 15 and col <= 25:
                        col = 4
                    else:
                        col = 5
                    colsl.append(col)
            elif cols == u'嗅和味':
                for col in list(groundwater_data[cols].iloc[:]):
                    if col =='无':
                        col = 1
                    else:
                        col = 5
                    colsl.append(col)
            elif cols == u'浑浊度':
                for col in list(groundwater_data[cols].iloc[:]):
                    if col <= 3:
                        col = 1
                    elif col > 3 and col <= 10:
                        col = 4
                    else:
                        col = 5
                    colsl.append(col)
            elif cols == u'肉眼可见物':
                for col in list(groundwater_data[cols].iloc[:]):
                    if col == '无':
                        col = 1
                    else:
                        col = 5
                    colsl.append(col)

            elif cols == u'总硬度(mg/L)':
                for col in list(groundwater_data[cols].iloc[:]):
                    if col <= 150:
                        col = 1
                    elif col > 150 and col <= 300:
                        col = 2
                    elif col > 300 and col <= 450:
                        col = 3
                    elif col > 450 and col <= 650:
                        col = 4
                    else:
                        col = 5
                    colsl.append(col)
            elif cols == u'溶解性总固体(mg/L)':
                for col in list(groundwater_data[cols].iloc[:]):
                    if col <= 300:
                        col = 1
                    elif col > 300 and col <= 500:
                        col = 2
                    elif col > 500 and col <= 1000:
                        col = 3
                    elif col > 1000 and col <= 2000:
                        col = 4
                    else:
                        col = 5
                    colsl.append(col)
            elif cols == u'硫酸盐(mg/L)':
                for col in list(groundwater_data[cols].iloc[:]):
                    if col <= 50:
                        col = 1
                    elif col > 50 and col <= 150:
                        col = 2
                    elif col > 150 and col <= 250:
                        col = 3
                    elif col > 250 and col <= 350:
                        col = 4
                    else:
                        col = 5
                    colsl.append(col)
            elif cols == u'氯化物(mg/L)':
                for col in list(groundwater_data[cols].iloc[:]):
                    if col == -2:
                        col = 1
                    elif col <= 50:
                        col = 1
                    elif col > 50 and col <= 150:
                        col = 2
                    elif col > 150 and col <= 250:
                        col = 3
                    elif col > 250 and col <= 350:
                        col = 4
                    else:
                        col = 5
                    colsl.append(col)
            elif cols == u'铁(mg/L)':
                for col in list(groundwater_data[cols].iloc[:]):
                    if col == -2:
                        col = 1
                    elif col <= 0.1:
                        col = 1
                    elif col > 0.1 and col <= 0.2:
                        col = 2
                    elif col > 0.2 and col <= 0.3:
                        col = 3
                    elif col > 0.3 and col <= 2.0:
                        col = 4
                    else:
                        col = 5
                    colsl.append(col)
            elif cols == u'锰(mg/L)':
                for col in list(groundwater_data[cols].iloc[:]):
                    col = col / 1000
                    if col == -2:
                        col = 1
                    elif col <= 0.05:
                        col = 1
                    elif col > 0.05 and col <= 0.1:
                        col = 3
                    elif col > 0.1 and col <= 1.5:
                        col = 4
                    else:
                        col = 5
                    colsl.append(col)
            elif cols == u'铜(mg/L)':
                for col in list(groundwater_data[cols].iloc[:]):
                    col = col / 1000
                    if col == -2:
                        col = 1
                    elif col <= 0.01:
                        col = 1
                    elif col > 0.01 and col <= 0.05:
                        col = 2
                    elif col > 0.05 and col <= 1.0:
                        col = 3
                    elif col > 1.0 and col <= 1.50:
                        col = 4
                    else:
                        col = 5
                    colsl.append(col)
            elif cols == u'锌(mg/L)':
                for col in list(groundwater_data[cols].iloc[:]):
                    col = col / 1000
                    if col == -2:
                        col = 1
                    elif col <= 0.05:
                        col = 1
                    elif col > 0.05 and col <= 0.5:
                        col = 2
                    elif col > 0.5 and col <= 1.0:
                        col = 3
                    elif col > 1.0 and col <= 5.0:
                        col = 4
                    else:
                        col = 5
                    colsl.append(col)
            elif cols == u'铝(mg/L)':
                for col in list(groundwater_data[cols].iloc[:]):
                    #col = col / 1000
                    if col == -2:
                        col = 1
                    elif col <= 0.01:
                        col = 1
                    elif col > 0.01 and col <= 0.05:
                        col = 2
                    elif col > 0.05 and col <= 0.2:
                        col = 3
                    elif col > 0.2 and col <= 0.5:
                        col = 4
                    else:
                        col = 5
                    colsl.append(col)
            elif cols == u'挥发性酚类(mg/L)':
                for col in list(groundwater_data[cols].iloc[:]):
                    if col == -2:
                        col = 1
                    elif col <= 0.001:
                        col = 1
                    elif col > 0.001 and col <= 0.002:
                        col = 3
                    elif col > 0.002 and col <= 0.01:
                        col = 4
                    else:
                        col = 5
                    colsl.append(col)
            elif cols == u'阴离子表面活性剂(mg/L)':
                for col in list(groundwater_data[cols].iloc[:]):
                    if col == -2:
                        col = 1
                    elif col <= 0.1:
                        col = 2
                    elif col > 0.1 and col <= 0.3:
                        col = 3
                    else:
                        col = 5
                    colsl.append(col)
            elif cols == u'耗氧量(mg/L)':
                for col in list(groundwater_data[cols].iloc[:]):
                    if col == -2:
                        col = 1
                    elif col <= 1.0:
                        col = 1
                    elif col > 1.0 and col <= 2.0:
                        col = 2
                    elif col > 2.0 and col <= 3.0:
                        col = 3
                    elif col > 3.0 and col <= 10.0:
                        col = 4
                    else:
                        col = 5
                    colsl.append(col)

            elif cols == u'氨氮(mg/L)':
                for col in list(groundwater_data[cols].iloc[:]):
                    #col = col*14/17
                    if col == -2:
                        col = 1
                    elif col <= 0.02:
                        col = 1
                    elif col > 0.02 and col <= 0.1:
                        col = 2
                    elif col > 0.1 and col <= 0.5:
                        col = 3
                    elif col > 0.5 and col <= 1.5:
                        col = 4
                    else:
                        col = 5
                    colsl.append(col)

            elif cols == u'硫化物(mg/L)':
                for col in list(groundwater_data[cols].iloc[:]):
                    if col == -2:
                        col = 1
                    elif col <= 0.005:
                        col = 1
                    elif col > 0.005 and col <= 0.01:
                        col = 2
                    elif col > 0.01 and col <= 0.02:
                        col = 3
                    elif col > 0.02 and col <= 0.1:
                        col = 4
                    else:
                        col = 5
                    colsl.append(col)

            elif cols == u'钠(mg/L)':
                for col in list(groundwater_data[cols].iloc[:]):
                    if col == -2:
                        col = 1
                    elif col <= 100:
                        col = 1
                    elif col > 100 and col <= 150:
                        col = 2
                    elif col > 150 and col <= 200:
                        col = 3
                    elif col > 200 and col <= 400:
                        col = 4
                    else:
                        col = 5
                    colsl.append(col)

            elif cols == u'亚硝酸盐(mg/L)':
                for col in list(groundwater_data[cols].iloc[:]):
                    col = col * 14 / 46
                    if col == -2:
                        col = 1
                    elif col == -1:
                        col = 0
                    elif col <= 0.001:
                        col = 1
                    elif col > 0.001 and col <= 0.01:
                        col = 2
                    elif col > 0.01 and col <= 1.0:
                        col = 3
                    elif col > 1.0 and col <= 4.8:
                        col = 4
                    else:
                        col = 5
                    colsl.append(col)

            elif cols == u'硝酸盐(mg/L)':
                for col in list(groundwater_data[cols].iloc[:]):
                    ol = col * 14 / 62
                    if col == -2:
                        col = 1
                    elif col == -1:
                        col = 0
                    elif col <= 2.0:
                        col = 1
                    elif col > 2.0 and col <= 5.0:
                        col = 2
                    elif col > 5.0 and col <= 20.0:
                        col = 3
                    elif col > 20.0 and col <= 30.0:
                        col = 4
                    else:
                        col = 5
                    colsl.append(col)

            elif cols == u'氰化物(mg/L)':
                for col in list(groundwater_data[cols].iloc[:]):
                    if col == -2:
                        col = 1
                    elif col == -1:
                        col = 0
                    elif col <= 0.001:
                        col = 1
                    elif col > 0.001 and col <= 0.01:
                        col = 2
                    elif col > 0.01 and col <= 0.05:
                        col = 3
                    elif col > 0.05 and col <= 0.1:
                        col = 4
                    else:
                        col = 5
                    colsl.append(col)



            elif cols == u'碘化物(mg/L)':
                for col in list(groundwater_data[cols].iloc[:]):
                    if col == -2:
                        col = 1
                    elif col == -1:
                        col = 0
                    elif col <= 0.04:
                        col = 1
                    elif col > 0.04 and col <= 0.08:
                        col = 3
                    elif col > 0.08 and col <= 0.5:
                        col = 4
                    else:
                        col = 5
                    colsl.append(col)

            elif cols == u'汞(mg/L)':
                for col in list(groundwater_data[cols].iloc[:]):
                    #col=col/1000
                    if col == -2:
                        col = 1
                    elif col == -1:
                        col = 0
                    elif col <= 0.0001:
                        col = 1
                    elif col > 0.0001 and col <= 0.001:
                        col = 3
                    elif col > 0.001 and col <= 0.002:
                        col = 4
                    else:
                        col = 5
                    colsl.append(col)

            elif cols == u'砷(mg/L)':
                for col in list(groundwater_data[cols].iloc[:]):
                    #col=col/1000
                    if col == -2:
                        col = 1
                    elif col == -1:
                        col = 0
                    elif col <= 0.001:
                        col = 1
                    elif col > 0.001 and col <= 0.01:
                        col = 3
                    elif col > 0.01 and col <= 0.05:
                        col = 4
                    else:
                        col = 5
                    colsl.append(col)

            elif cols == u'硒(mg/L)':
                for col in list(groundwater_data[cols].iloc[:]):
                    #col = col / 1000
                    if col == -2:
                        col = 1
                    elif col == -1:
                        col = 0
                    elif col <= 0.01:
                        col = 1
                    elif col > 0.01 and col <= 0.1:
                        col = 4
                    else:
                        col = 5
                    colsl.append(col)

            elif cols == u'镉(mg/L)':
                for col in list(groundwater_data[cols].iloc[:]):
                    col = col/1000
                    if col == -2:
                        col = 1
                    elif col == -1:
                        col = 0
                    elif col <= 0.0001:
                        col = 1
                    elif col > 0.0001 and col <= 0.001:
                        col = 2
                    elif col > 0.001 and col <= 0.005:
                        col = 3
                    elif col > 0.005 and col <= 0.01:
                        col = 4
                    else:
                        col = 5
                    colsl.append(col)

            elif cols == u'铬（六价）(mg/L)':
                for col in list(groundwater_data[cols].iloc[:]):
                    if col == -2:
                        col = 1
                    elif col == -1:
                        col = 0
                    elif col <= 0.005:
                        col = 1
                    elif col > 0.005 and col <= 0.01:
                        col = 2
                    elif col > 0.01 and col <= 0.05:
                        col = 3
                    elif col > 0.05 and col <= 0.1:
                        col = 4
                    else:
                        col = 5
                    colsl.append(col)

            elif cols == u'铅(mg/L)':
                for col in list(groundwater_data[cols].iloc[:]):
                    col = col / 1000
                    if col == -2:
                        col = 1
                    elif col == -1:
                        col = 0
                    elif col <= 0.005:
                        col = 1
                    elif col > 0.005 and col <= 0.01:
                        col = 3
                    elif col > 0.01 and col <= 0.1:
                        col = 4
                    else:
                        col = 5
                    colsl.append(col)

            elif cols == u'三氯甲烷(ug/L)':
                for col in list(groundwater_data[cols].iloc[:]):
                    if col == -2:
                        col = 1
                    elif col == -1:
                        col = 0
                    elif col <= 0.5:
                        col = 1
                    elif col > 0.5 and col <= 6:
                        col = 2
                    elif col > 6 and col <= 60:
                        col = 3
                    elif col > 60 and col <= 300:
                        col = 4
                    else:
                        col = 5
                    colsl.append(col)

            elif cols == u'四氯化碳(ug/L)':
                for col in list(groundwater_data[cols].iloc[:]):
                    if col == -2:
                        col = 1
                    elif col == -1:
                        col = 0
                    elif col <= 0.5:
                        col = 1
                    elif col > 0.5 and col <= 2.0:
                        col = 3
                    elif col > 2.0 and col <= 50:
                        col = 4
                    else:
                        col = 5
                    colsl.append(col)

            elif cols == u'苯(ug/L)':
                for col in list(groundwater_data[cols].iloc[:]):
                    if col == -2:
                        col = 1
                    elif col == -1:
                        col = 0
                    elif col <= 0.5:
                        col = 1
                    elif col > 0.5 and col <= 1.0:
                        col = 2
                    elif col > 1.0 and col <= 10.0:
                        col = 3
                    elif col > 10.0 and col <= 120.0:
                        col = 4
                    else:
                        col = 5
                    colsl.append(col)

            elif cols == u'甲苯(ug/L)':
                for col in list(groundwater_data[cols].iloc[:]):
                    if col == -2:
                        col = 1
                    elif col == -1:
                        col = 0
                    elif col <= 0.5:
                        col = 1
                    elif col > 0.5 and col <= 140.0:
                        col = 2
                    elif col > 140.0 and col <= 700.0:
                        col = 3
                    elif col > 700.0 and col <= 1400.0:
                        col = 4
                    else:
                        col = 5
                    colsl.append(col)
            elif cols == u'钡(mg/L)':
                for col in list(groundwater_data[cols].iloc[:]):
                    col = col / 1000
                    if col == -2:
                        col = 1
                    elif col == -1:
                        col = 0
                    elif col <= 0.01:
                        col = 1
                    elif col > 0.01 and col <= 0.1:
                        col = 2
                    elif col > 0.1 and col <= 0.7:
                        col = 3
                    elif col > 0.7 and col <= 4:
                        col = 4
                    else:
                        col = 5
                    colsl.append(col)
            elif cols == u'钴(mg/L)':
                for col in list(groundwater_data[cols].iloc[:]):
                    col = col / 1000
                    if col == -2:
                        col = 1
                    elif col == -1:
                        col = 0
                    elif col <= 0.005:
                        col = 1
                    elif col > 0.005 and col <= 0.05:
                        col = 3
                    elif col > 0.05 and col <= 0.1:
                        col = 4
                    else:
                        col = 5
                    colsl.append(col)
            elif cols == u'镍(mg/L)':
                for col in list(groundwater_data[cols].iloc[:]):
                    col = col / 1000
                    if col == -2:
                        col = 1
                    elif col == -1:
                        col = 0
                    elif col <= 0.002:
                        col = 1
                    elif col > 0.002 and col <= 0.02:
                        col = 3
                    elif col > 0.02 and col <= 0.1:
                        col = 4
                    else:
                        col = 5
                    colsl.append(col)
            elif cols == u'锑(mg/L)':
                for col in list(groundwater_data[cols].iloc[:]):
                    col = col / 1000
                    if col == -2:
                        col = 1
                    elif col == -1:
                        col = 0
                    elif col <= 0.0001:
                        col = 1
                    elif col > 0.0001 and col <= 0.0005:
                        col = 2
                    elif col > 0.0005 and col <= 0.005:
                        col = 3
                    elif col > 0.005 and col <= 0.01:
                        col = 4
                    else:
                        col = 5
                    colsl.append(col)
            elif cols == u'银(mg/L)':
                for col in list(groundwater_data[cols].iloc[:]):
                    if col == -2:
                        col = 1
                    elif col == -1:
                        col = 0
                    elif col <= 0.0001:
                        col = 1
                    elif col > 0.0001 and col <= 0.0005:
                        col = 2
                    elif col > 0.0005 and col <= 0.005:
                        col = 3
                    elif col > 0.005 and col <= 0.01:
                        col = 4
                    else:
                        col = 5
                    colsl.append(col)
            elif cols == u'氟化物(mg/L)':
                for col in list(groundwater_data[cols].iloc[:]):
                    if col == -2:
                        col = 1
                    elif col == -1:
                        col = 0
                    elif col <= 1.0:
                        col = 1
                    elif col > 1 and col <= 2:
                        col = 4
                    else:
                        col = 5
                    colsl.append(col)
        colsl = np.array(colsl).reshape(groundwater_data.values[:, :].shape[1],
                                        groundwater_data.values[:, :].shape[0])
        index = list(groundwater_data.columns[:])
        DATA = pd.DataFrame(colsl.T, index=groundwater_data.index[:], columns=index)
        return DATA

    def water_assess93kh(self):
        groundwater_data = pd.read_excel(self.input_file_name, sheet_name=self.inputsheetname, index_col=0,header=0)
        colsl = []
        for cols in groundwater_data.columns[:]:
            print(cols)
            if cols == u'pH':
                for col in list(groundwater_data[cols].iloc[:]):
                    if col >= 6.5 and col <= 8.5:
                        col = 1
                    elif col >= 5.5 and col < 6.5:
                        col = 4
                    elif col > 8.5 and col <= 9.0:
                        col = 4
                    else:
                        col = 5
                    colsl.append(col)
            elif cols == u'氨氮(mg/L)':
                for col in list(groundwater_data[cols].iloc[:]):
                    #col = col*14/18
                    if col == -2:
                        col = 1
                    elif col <= 0.02:
                        col = 1
                    elif col > 0.02 and col <= 0.2:
                        col = 3
                    elif col > 0.2 and col <= 0.5:
                        col = 4
                    else:
                        col = 5
                    colsl.append(col)
            elif cols == u'亚硝酸盐(mg/L)':
                for col in list(groundwater_data[cols].iloc[:]):
                    col = col*14/46
                    if col == -2:
                        col = 1
                    elif col == -1:
                        col = 0
                    elif col <= 0.001:
                        col = 1
                    elif col > 0.001 and col <= 0.01:
                        col = 2
                    elif col > 0.01 and col <= 0.02:
                        col = 3
                    elif col > 0.02 and col <= 0.1:
                        col = 4
                    else:
                        col = 5
                    colsl.append(col)

            elif cols == u'硝酸盐(mg/L)':
                for col in list(groundwater_data[cols].iloc[:]):
                    col = col*14/62
                    if col == -2:
                        col = 1
                    elif col == -1:
                        col = 0
                    elif col <= 2.0:
                        col = 1
                    elif col > 2.0 and col <= 5.0:
                        col = 2
                    elif col > 5.0 and col <= 20.0:
                        col = 3
                    elif col > 20.0 and col <= 30.0:
                        col = 4
                    else:
                        col = 5
                    colsl.append(col)
            elif cols == u'氰化物(mg/L)':
                for col in list(groundwater_data[cols].iloc[:]):
                    if col == -2:
                        col = 1
                    elif col == -1:
                        col = 0
                    elif col <= 0.001:
                        col = 1
                    elif col > 0.001 and col <= 0.01:
                        col = 2
                    elif col > 0.01 and col <= 0.05:
                        col = 3
                    elif col > 0.05 and col <= 0.1:
                        col = 4
                    else:
                        col = 5
                    colsl.append(col)
            elif cols == u'挥发性酚类(mg/L)':
                for col in list(groundwater_data[cols].iloc[:]):
                    if col == -2:
                        col = 1
                    elif col <= 0.001:
                        col = 1
                    elif col > 0.001 and col <= 0.002:
                        col = 3
                    elif col > 0.002 and col <= 0.01:
                        col = 4
                    else:
                        col = 5
                    colsl.append(col)
            elif cols == u'汞(mg/L)':
                for col in list(groundwater_data[cols].iloc[:]):
                    col=col/1000
                    if col == -2:
                        col = 1
                    elif col == -1:
                        col = 0
                    elif col <= 0.00005:
                        col = 1
                    elif col > 0.00005 and col <= 0.001:
                        col = 3
                    else:
                        col = 5
                    colsl.append(col)

            elif cols == u'砷(mg/L)':
                for col in list(groundwater_data[cols].iloc[:]):
                    col=col/1000
                    if col == -2:
                        col = 1
                    elif col == -1:
                        col = 0
                    elif col <= 0.005:
                        col = 1
                    elif col > 0.005 and col <= 0.01:
                        col = 2
                    elif col > 0.01 and col <= 0.05:
                        col = 3
                    else:
                        col = 5
                    colsl.append(col)

            elif cols == u'铬（六价）(mg/L)':
                for col in list(groundwater_data[cols].iloc[:]):
                    if col == -2:
                        col = 1
                    elif col == -1:
                        col = 0
                    elif col <= 0.005:
                        col = 1
                    elif col > 0.005 and col <= 0.01:
                        col = 2
                    elif col > 0.01 and col <= 0.05:
                        col = 3
                    elif col > 0.05 and col <= 0.1:
                        col = 4
                    else:
                        col = 5
                    colsl.append(col)

            elif cols == u'铅(mg/L)':
                for col in list(groundwater_data[cols].iloc[:]):
                    col = col / 1000
                    if col == -2:
                        col = 1
                    elif col == -1:
                        col = 0
                    elif col <= 0.005:
                        col = 1
                    elif col > 0.005 and col <= 0.01:
                        col = 2
                    elif col > 0.01 and col <= 0.05:
                        col = 3
                    elif col > 0.05 and col <= 0.1:
                        col = 4
                    else:
                        col = 5
                    colsl.append(col)

            elif cols == u'总硬度(mg/L)':
                for col in list(groundwater_data[cols].iloc[:]):
                    if col <= 150:
                        col = 1
                    elif col > 150 and col <= 300:
                        col = 2
                    elif col > 300 and col <= 450:
                        col = 3
                    elif col > 450 and col <= 550:
                        col = 4
                    else:
                        col = 5
                    colsl.append(col)
            elif cols == u'溶解性总固体(mg/L)':
                for col in list(groundwater_data[cols].iloc[:]):
                    if col <= 300:
                        col = 1
                    elif col > 300 and col <= 500:
                        col = 2
                    elif col > 500 and col <= 1000:
                        col = 3
                    elif col > 1000 and col <= 2000:
                        col = 4
                    else:
                        col = 5
                    colsl.append(col)
            elif cols == u'硫酸盐(mg/L)':
                for col in list(groundwater_data[cols].iloc[:]):
                    if col <= 50:
                        col = 1
                    elif col > 50 and col <= 150:
                        col = 2
                    elif col > 150 and col <= 250:
                        col = 3
                    elif col > 250 and col <= 350:
                        col = 4
                    else:
                        col = 5
                    colsl.append(col)
            elif cols == u'氯化物(mg/L)':
                for col in list(groundwater_data[cols].iloc[:]):
                    if col == -2:
                        col = 1
                    elif col <= 50:
                        col = 1
                    elif col > 50 and col <= 150:
                        col = 2
                    elif col > 150 and col <= 250:
                        col = 3
                    elif col > 250 and col <= 350:
                        col = 4
                    else:
                        col = 5
                    colsl.append(col)
            elif cols == u'镉(mg/L)':
                for col in list(groundwater_data[cols].iloc[:]):
                    col = col/1000
                    if col == -2:
                        col = 1
                    elif col == -1:
                        col = 0
                    elif col <= 0.0001:
                        col = 1
                    elif col > 0.0001 and col <= 0.001:
                        col = 2
                    elif col > 0.001 and col <= 0.01:
                        col = 3
                    else:
                        col = 5
                    colsl.append(col)

            elif cols == u'氟化物(mg/L)':
                for col in list(groundwater_data[cols].iloc[:]):
                    if col == -2:
                        col = 1
                    elif col == -1:
                        col = 0
                    elif col <= 1.0:
                        col = 1
                    elif col > 1.0 and col <= 2.0:
                        col = 4
                    else:
                        col = 5
                    colsl.append(col)

            elif cols == u'铜(mg/L)':
                for col in list(groundwater_data[cols].iloc[:]):
                    # col = col / 1000
                    if col == -2:
                        col = 1
                    elif col <= 0.01:
                        col = 1
                    elif col > 0.01 and col <= 0.05:
                        col = 2
                    elif col > 0.05 and col <= 1.0:
                        col = 3
                    elif col > 1.0 and col <= 1.50:
                        col = 4
                    else:
                        col = 5
                    colsl.append(col)

            elif cols == u'耗氧量(mg/L)':
                for col in list(groundwater_data[cols].iloc[:]):
                    # col = col / 1000
                    if col == -2:
                        col = 1
                    elif col <= 1.0:
                        col = 1
                    elif col > 1.0 and col <= 2.0:
                        col = 2
                    elif col > 2.0 and col <= 3.0:
                        col = 3
                    elif col > 3.0 and col <= 10.0:
                        col = 4
                    else:
                        col = 5
                    colsl.append(col)

            elif cols == u'阴离子表面活性剂(mg/L)':
                for col in list(groundwater_data[cols].iloc[:]):
                    if col == -2:
                        col = 1
                    elif col <= 0.1:
                        col = 2
                    elif col > 0.1 and col <= 0.3:
                        col = 3
                    else:
                        col = 5
                    colsl.append(col)

        colsl = np.array(colsl).reshape(groundwater_data.values[:, :].shape[1],
                                        groundwater_data.values[:, :].shape[0])
        index = list(groundwater_data.columns[:])
        DATA = pd.DataFrame(colsl.T, index=groundwater_data.index[:], columns=index)
        return DATA

    def class_4_5_index(self,Data):  # 提取4 5类指标
        data = Data
        class4 = []
        class5 = []
        L1 = u''
        L2 = u''
        index = data.columns
        WQ = data.values
        for i in range(WQ.shape[0]):
            sample = WQ[i]
            L4 = index[np.where(sample == 4)]
            for F4 in L4:
                L1 = L1 + F4 + u';'
            L1 = (L1.replace(u'(mg/L)', '')).replace(u'(ug/L）', '')
            class4.append(L1)
            L1 = u''

            L5 = index[np.where(sample == 5)]
            for F5 in L5:
                L2 = L2 + F5 + u';'
            L2 = (L2.replace(u'(mg/L)', '')).replace(u'(ug/L）', '')
            class5.append(L2)
            L2 = u''
        clss = np.array(class4 + class5).reshape(2, data.values.shape[0]).T
        Class_data = pd.DataFrame(clss, index=data.index, columns=['4类指标', '5类指标'])
        return Class_data

    def water_assessment(self,DATA):  # 利用F值对水样进行综合评价
        water_data = DATA
        new_water_data = []
        for wds in np.squeeze(water_data.values[:, :]):
            for wd in wds:
                if wd == 1:
                    new_water_data.append(0)
                elif wd == 2:
                    new_water_data.append(1)
                elif wd == 3:
                    new_water_data.append(3)
                elif wd == 4:
                    new_water_data.append(6)
                elif wd == 5:
                    new_water_data.append(10)
                else:
                    pass
        new_water_data = np.array(new_water_data).reshape(water_data.values.shape[0], water_data.values.shape[1])
        Fmean = np.mean(new_water_data, axis=1)
        F = np.round(np.sqrt((Fmean ** 2 + np.max(new_water_data, axis=1) ** 2) / 2),2)
        F_ = np.vstack((Fmean, F))
        wa = []
        g = []
        for f in F:
            if round(f,2) < 0.8:
                wa.append('优良')
                g.append(1)
            elif round(f,2) >= 0.8 and round(f,2) < 2.5:
                wa.append('良好')
                g.append(2)
            elif round(f,2) >= 2.5 and round(f,2) < 4.25:
                wa.append('较好')
                g.append(3)
            elif round(f,2)>= 4.25 and round(f,2) < 7.2:
                wa.append('较差')
                g.append(4)
            else:
                wa.append('极差')
                g.append(5)
        wa = np.array(wa).reshape(1, water_data.values.shape[0])
        g = np.array(g)
        F_ = np.vstack((F_, wa,g)).T
        new_water_data = pd.DataFrame(new_water_data, index=DATA.index, columns=DATA.columns)
        F_ = pd.DataFrame(F_, index=DATA.index, columns=['Fmean', 'F', 'class','分值'])
        return new_water_data, F_

    def water_huaxue(self,sheetname):
        data=pd.read_excel(self.input_file_name,sheet_name=sheetname,index_col=0,header=0)
        water_class=[]
        for num in data.index:
            yin = data.loc[num, :][:3][data.loc[num, :][:3] > 0.25].sort_values(ascending=False).index
            yang = data.loc[num, :][3:][data.loc[num, :][3:] > 0.25].sort_values(ascending=False).index
            YI = ''
            YA = ''
            for yi in yin:
                YI = YI + yi + '.'
            for ya in yang:
                YA = YA + ya + '.'
            water_class.append(YI+'-'+YA)
            return pd.Series(water_class,index=data.index)

    def data_to_excel(self):
        A = Groundwater_assessment(self.input_file_name,self.output_file_name,self.inputsheetname)
        with pd.ExcelWriter(self.output_file_name) as writer:
            Data = A.water_assess93kh()
            Data.to_excel(writer, sheet_name=self.inputsheetname+'评价结果')
            class_45 = A.class_4_5_index(Data)
            class_45.to_excel(writer, sheet_name= self.inputsheetname+'4-5类指标')
        return None

    def kuangquanwater(self):
        groundwater_data = pd.read_excel(self.input_file_name, sheet_name=self.inputsheetname, index_col=0, header=0)
        colsl = []
        for cols in groundwater_data.columns[:]:
            if cols == u'锶(mg/L)':
                for col in list(groundwater_data[cols].iloc[:]):
                    if col >=0.2:
                        col=1
                    else:
                        col=5
                    colsl.append(col)
            elif cols == u'锌(mg/L)':
                for col in list(groundwater_data[cols].iloc[:]):
                    if col >=0.2:
                        col=1
                    else:
                        col=5
                    colsl.append(col)
            elif cols == u'偏硅酸(mg/L)':
                for col in list(groundwater_data[cols].iloc[:]):
                    if col >=25.0:
                        col=1
                    else:
                        col=5
                    colsl.append(col)
            elif cols == u'硒(mg/L)':
                for col in list(groundwater_data[cols].iloc[:]):
                    if col >=0.01:
                        col=1
                    else:
                        col=5
                    colsl.append(col)
            elif cols == u'溶解性总固体(mg/L)':
                for col in list(groundwater_data[cols].iloc[:]):
                    if col >=1000.0:
                        col=1
                    else:
                        col=5
                    colsl.append(col)
            elif cols == u'浑浊度':
                for col in list(groundwater_data[cols].iloc[:]):
                    if col >10:
                        col=5
                    else:
                        col=1
                    colsl.append(col)
        colsl = np.array(colsl).reshape(groundwater_data.values[:, :].shape[1],
                                        groundwater_data.values[:, :].shape[0])
        index = list(groundwater_data.columns[:])
        DATA = pd.DataFrame(colsl.T, index=groundwater_data.index[:], columns=index)
        return DATA
if __name__=='__main__':
    #只需要修改下列三个参数
    inputpath = 'D:\\总站\\2020监测井水质报告_地研院\\2020地下水--地研院水质1(已自动还原).xlsx'#输入excel数据的绝对路径（处理之前需要将表头和数据调整为2017标准一致，表头和数据）
    sheetname = '评价数据'#输入表格名称
    outputpath = 'D:\\总站\\2020监测井水质报告_地研院\\评价.xlsx'#输出文件的绝对路径
    A = Groundwater_assessment(inputpath,outputpath,sheetname)
    #Data = pd.read_excel('D:\\总站\\国家级2020资料\\国家2020水质评价.xlsx',sheet_name='Sheet1',index_col=0,header=0)
    Data=A.water_assess()
    data45=A.class_4_5_index(Data)
    #A.data_to_excel()
    with pd.ExcelWriter(outputpath) as writer:
        Data.to_excel(writer, sheet_name='评价结果')
        data45.to_excel(writer, sheet_name='4-5类指标')



