import math
import os
import sys
import pandas as pd
from PyQt5.QtGui import QFont

from ui_subWindow import Ui_Form
from PyQt5 import QtGui
from PyQt5.QtChart import QScatterSeries, QSplineSeries
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QGridLayout, QWidget, QGraphicsLineItem, QGraphicsTextItem
from PyQt5.QtChart import QChart, QChartView, QLineSeries, QValueAxis
from PyQt5.QtCore import Qt, QPointF

def closest(mylist, Number):
    answer = []
    tag = []
    Number = float(Number)
    for i in mylist:
        answer.append(abs(Number - i))
    temp = min(answer)
    for index, key in enumerate(answer):
        if key == temp:
            tag.append(index)
    return tag

class QSubWidget(QWidget):
    def __init__(self, parent=None,paremeters=None,state=0,ui=None):
        super().__init__(parent)    #调用父类构造函数，创建窗体
        self.ui_parent = ui
        self.ui = Ui_Form()         #创建UI对象
        self.ui.setupUi(self)       #构造UI
        self.df = pd.read_excel(r'.\炉渣性能编号和成分.xlsx', index_col=None)
        self.font = QtGui.QFont()
        self.font.setFamily("宋体")
        self.font.setPointSize(9)
        self.font.setWeight(50)
        self.labelfont = QtGui.QFont()
        self.labelfont.setFamily("Arial")
        self.labelfont.setPointSize(9)
        self.labelfont.setWeight(50)
        # self.setCursor(Qt.CursorShape.CrossCursor)
        # self.showView(paremeters)
        # print(type(state))
        if '.50' in paremeters['Al2O3']:
            paremeters['Al2O3'] = paremeters['Al2O3'].replace('.50','.60')
        if '.50' in paremeters['MgO']:
            paremeters['MgO'] = paremeters['MgO'].replace('.50','.60')
        if state == 0:
            self.getMeltingData(paremeters)
        elif state == 1:
            # print('here2')
            self.showView(paremeters)
        else:
            self.showNianDu(paremeters)

    def showView(self,paremeters):
        df = pd.read_excel(r'.\炉渣性能编号和成分.xlsx', index_col=None)
        al2o3_input = paremeters['Al2O3']
        mog_input = paremeters['MgO']
        jiandu_input = paremeters['jiandu']
        zhabi = float(paremeters['zhabi'])
        s = paremeters['s']
        t = paremeters['t']
        rate_s = round(float(s) / 0.2886, 4)
        rate_zhabi = round(0.30 / float(zhabi), 4)
        al2o3 = df['Al2O3']
        closed_index1 = closest(al2o3, al2o3_input)
        result1 = df.iloc[closed_index1, :]
        #
        mgo = result1['MgO']
        closed_index2 = closest(mgo, mog_input)
        result2 = result1.iloc[closed_index2, :]
        #
        ratio_sio2_cao = round(result2['CaO'] / result2['SiO2'], 2)
        # ratio_sio2_cao.to_excel('监督.xlsx')
        # print(ratio_sio2_cao)
        closed_index3 = closest(ratio_sio2_cao, jiandu_input)
        result3 = result2.iloc[closed_index3, :]
        # 得到方案
        fangan_num = result3['方案'].values[0].split('#')[0]
        # 确定渣比
        fangan_path = '.\硫分配\拷贝脱硫\\' + str(zhabi) + '\\' + fangan_num + '.xlsx'
        # print('匹配的渣比方案路径为：', fangan_path)
        df2 = pd.read_excel(fangan_path)
        # 硫负荷
        # print(df2)
        # 找到硫负荷最接近的
        Alpha = df2['Alpha'][0:]
        closed_index4 = closest(Alpha, s)
        result4 = df2.iloc[closed_index4, :]

        # 画第一张图
        chart = QChart()  # 创建 chart
        chartView = MyChartView(chart,self)  # 创建 chartView
        # chartView.setChart(chart)  # chart添加到chartView
        chartView.setGeometry(0,0,400,400)
        chartView.setCursor(Qt.CursorShape.CrossCursor)
        # ## bottom 轴是 QLogValueAxis
        self.__axisButtom = QValueAxis()
        chart.addAxis(self.__axisButtom, Qt.AlignBottom)
        self.__axisLeft = QValueAxis()
        chart.addAxis(self.__axisLeft, Qt.AlignLeft)
        #self.__axisRight = QValueAxis()
        #chart.addAxis(self.__axisRight, Qt.AlignRight)
        seriesLeft = QLineSeries()
        #seriesRight = QLineSeries()
        #pen = seriesRight.pen()
        #pen.setColor(Qt.green)
        #pen.setWidth(4)
        #seriesRight.setPen(pen)
        pen = seriesLeft.pen()
        pen.setColor(Qt.blue)
        pen.setWidth(4)
        seriesLeft.setPen(pen)
        seriesLeft.hovered.connect(self.do_series_hovered)  # 信号 hovered
        seriesLeft.clicked.connect(self.do_series_clicked)  # 信号 clicked
        #seriesRight.hovered.connect(self.do_series_hovered)  # 信号 hovered
        #seriesRight.clicked.connect(self.do_series_clicked)  # 信号 clicked
        t_list = result4['T(C)']
        closed_index5 = closest(t_list, t)
        temp_result = result4.iloc[closed_index5, :]
        for i in range(len(result4)):
            # print(result4['T(C)'].values[i])
            seriesLeft.append(result4['T(C)'].values[i],(result4['Wt%-S(FeLQ)'].values[i]+0.005)*rate_s*rate_zhabi)
            # seriesRight.append(result4['T(C)'].values[i], result4['Wt%-S_FToxid-SLAGA#1'].values[i])
        minMag = min((result4['Wt%-S(FeLQ)']+0.005)*rate_s*rate_zhabi)
        maxMag = max((result4['Wt%-S(FeLQ)']+0.005)*rate_s*rate_zhabi)
        #minPh = min(result4['Wt%-S_FToxid-SLAGA#1'].values)
        #maxPh = max(result4['Wt%-S_FToxid-SLAGA#1'].values)
        minT = min(result4['T(C)'].values)
        maxT = max(result4['T(C)'].values)
        self.__axisLeft.setLabelFormat("%.4f")
        self.__axisLeft.setRange(minMag, maxMag)
        self.__axisLeft.setTitleText('硫含量(Wt%)')
        self.__axisLeft.setTitleFont(self.font)
        #self.__axisRight.setRange(minPh, maxPh)
        #self.__axisRight.setTitleText('硫含量(Wt%)')
        #self.__axisRight.setTitleFont(self.font)
        self.__axisButtom.setRange(1450,maxT)
        self.__axisButtom.setTitleText('&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;温度℃<br>(温度低于1450℃，无法完全达到硫平衡。)')

        self.__axisButtom.setTitleFont(self.font)
        self.__axisLeft.setLabelsFont(self.labelfont)
        #self.__axisRight.setLabelsFont(self.labelfont)
        self.__axisButtom.setLabelsFont(self.labelfont)
        chart.addSeries(seriesLeft)
        seriesLeft.attachAxis(self.__axisButtom)
        seriesLeft.attachAxis(self.__axisLeft)
        seriesLeft.setName('铁中硫含量')
        # chart.addSeries(seriesRight)
        #seriesRight.attachAxis(self.__axisButtom)
        #seriesRight.attachAxis(self.__axisRight)
        #seriesRight.setName('渣中硫含量')
        # 画第二张图
        chart2 = QChart()
        chartView2 = MyChartView(chart2,self)  # 创建 chartView
        # chartView2.setChart(chart2)  # chart添加到chartView
        chartView2.setGeometry(405,0,400,400)
        temperature = result4['T(C)'][0:]
        closed_index5 = closest(temperature, t)
        result5 = result4.iloc[closed_index5, :]
        same_jiandu = df[df['碱度R2'] == result3['碱度R2'].values[0]]
        same_jiandu_al2o3 = same_jiandu[same_jiandu['Al2O3'] == result3['Al2O3'].values[0]]
        # print(same_jiandu_al2o3['MgO'])
        fangan_same_jandu_al2o3_list = same_jiandu_al2o3['方案'].values
        #print('得到碱度和al2o3不变，mgo改变的方案序号为：', fangan_same_jandu_al2o3_list)
        mgo_last = same_jiandu_al2o3['MgO'].values
        # print('here3:',fangan_same_jandu_al2o3_list)
        zha_liu = []
        tei_liu = []
        #
        # print(fangan_same_jandu_al2o3_list)
        for item in fangan_same_jandu_al2o3_list:
            item = item.split('#')[0]
            fangan_path = '.\硫分配\拷贝脱硫\\' + str(zhabi) + '\\' + item + '.xlsx'
            #print('匹配的渣比方案路径为2：', fangan_path)
            df2 = pd.read_excel(fangan_path)
            Alpha = df2['Alpha'][0:-2]
            # print(Alpha)
            closed_index4 = closest(Alpha, s)
            result4 = df2.iloc[closed_index4, :]

            temperature = result4['T(C)'][0:]
            closed_index5 = closest(temperature, t)
            result5 = result4.iloc[closed_index5, :]
            #print('方案' + str(item) + '对应的Page:' + str(result5['-Page-'].values[0]))
            # print(result5)
            tei_liu.append((result5['Wt%-S(FeLQ)'].values[0]+0.005)*rate_s*rate_zhabi)
            zha_liu.append(result5['Wt%-S_FToxid-SLAGA#1'].values[0])
        self.__axisButtom2 = QValueAxis()
        self.__axisLeft2 = QValueAxis()
        #self.__axisRight2 = QValueAxis()
        chart2.addAxis(self.__axisButtom2, Qt.AlignBottom)
        chart2.addAxis(self.__axisLeft2, Qt.AlignLeft)
        #chart2.addAxis(self.__axisRight2, Qt.AlignRight)
        seriesLeft2 = QLineSeries()
        #seriesRight2 = QLineSeries()
        seriesLeft2.hovered.connect(self.do_series_hovered)  # 信号 hovered
        seriesLeft2.clicked.connect(self.do_series_clicked)  # 信号 clicked
        #seriesRight2.hovered.connect(self.do_series_hovered)  # 信号 hovered
        #seriesRight2.clicked.connect(self.do_series_clicked)  # 信号 clicked
        #pen = seriesRight2.pen()
        #pen.setColor(Qt.green)
        #pen.setWidth(4)
        #seriesRight2.setPen(pen)
        pen = seriesLeft2.pen()
        pen.setColor(Qt.blue)
        pen.setWidth(4)
        seriesLeft2.setPen(pen)
        for i in range(len(mgo_last)):
            seriesLeft2.append(mgo_last[i], tei_liu[i])
            #seriesRight2.append(mgo_last[i], zha_liu[i])
        minMag2 = min(tei_liu)
        maxMag2 = max(tei_liu)
        #minPh2 = min(zha_liu)
        #maxPh2 = max(zha_liu)
        self.__axisLeft2.setRange(minMag2, maxMag2)
        #self.__axisRight2.setRange(minPh2, maxPh2)
        chart2.addSeries(seriesLeft2)
        seriesLeft2.attachAxis(self.__axisButtom2)
        seriesLeft2.attachAxis(self.__axisLeft2)
        #chart2.addSeries(seriesRight2)
        #seriesRight2.attachAxis(self.__axisButtom2)
        #seriesRight2.attachAxis(self.__axisRight2)
        self.__axisLeft2.setTitleText('硫含量(Wt%)')
        #self.__axisLeft2.setTitleFont(self.font)
        #self.__axisRight2.setTitleText('硫含量(Wt%)')
        #self.__axisRight2.setTitleFont(self.font)
        self.__axisButtom2.setTitleText('氧化镁含量')
        #self.__axisButtom2.setTitleFont(self.font)
        seriesLeft2.setName('铁中硫含量')
        #seriesRight2.setName('渣中硫含量')
        self.__axisLeft2.setTitleFont(self.font)
        self.__axisLeft2.setLabelFormat("%.4f")
        #self.__axisRight2.setTitleFont(self.font)
        self.__axisButtom2.setTitleFont(self.font)
        self.__axisLeft2.setLabelsFont(self.labelfont)
        #self.__axisRight2.setLabelsFont(self.labelfont)
        self.__axisButtom2.setLabelsFont(self.labelfont)
        # # 第三张图
        # print('找碱度和硫含量的关系')
        # # print(result3)
        same_MgO = df[df['MgO'] == result3['MgO'].values[0]]
        same_MgO_al2o3 = same_MgO[same_MgO['Al2O3'] == result3['Al2O3'].values[0]]
        # print(same_MgO_al2o3['碱度R2'])
        fangan_same_MgO_al2o3_list = same_MgO_al2o3['方案'].values
        # print(fangan_same_MgO_al2o3_list)
        jiandu_last = same_MgO_al2o3['碱度R2'].values
        #print('得到mgo和al2o3不变，碱度改变的方案序号为：', fangan_same_MgO_al2o3_list)
        # print(jiandu_last)
        zha_liu = []
        tei_liu = []
        # print('=======================================')
        for item in fangan_same_MgO_al2o3_list:
            # print(item)
            item = item.split('#')[0]
            fangan_path = '.\硫分配\拷贝脱硫\\' + str(zhabi) + '\\' + item + '.xlsx'
            # print(fangan_path)
            #print('匹配的渣比方案路径为3：', fangan_path)
            df2 = pd.read_excel(fangan_path)
            Alpha = df2['Alpha'][0:]
            closed_index4 = closest(Alpha, s)
            result4 = df2.iloc[closed_index4, :]

            temperature = result4['T(C)'][0:]
            closed_index5 = closest(temperature, t)
            result5 = result4.iloc[closed_index5, :]
            #print('方案' + str(item) + '对应的Page:' + str(result5['-Page-'].values[0]))
            # print(result5)
            tei_liu.append((result5['Wt%-S(FeLQ)'].values[0]+0.005)*rate_s*rate_zhabi)
            zha_liu.append(result5['Wt%-S_FToxid-SLAGA#1'].values[0])
        chart3 = QChart()
        chartView3 = MyChartView(chart3,self)  # 创建 chartView
        # chartView3.setChart(chart3)  # chart添加到chartView
        chartView3.setGeometry(0, 405, 400, 400)
        self.__axisButtom3 = QValueAxis()
        self.__axisLeft3 = QValueAxis()
        #self.__axisRight3 = QValueAxis()
        chart3.addAxis(self.__axisButtom3, Qt.AlignBottom)
        chart3.addAxis(self.__axisLeft3, Qt.AlignLeft)
        # chart3.addAxis(self.__axisRight3, Qt.AlignRight)

        seriesLeft3 = QLineSeries()
        #seriesRight3 = QLineSeries()
        seriesLeft3.hovered.connect(self.do_series_hovered)  # 信号 hovered
        seriesLeft3.clicked.connect(self.do_series_clicked)  # 信号 clicked
        #seriesRight3.hovered.connect(self.do_series_hovered)  # 信号 hovered
        #seriesRight3.clicked.connect(self.do_series_clicked)  # 信号 clicked
        #pen = seriesRight3.pen()
        #pen.setColor(Qt.green)
        #pen.setWidth(4)
        #seriesRight3.setPen(pen)
        pen = seriesLeft3.pen()
        pen.setColor(Qt.blue)
        pen.setWidth(4)
        seriesLeft3.setPen(pen)
        for i in range(len(jiandu_last)):
            seriesLeft3.append(jiandu_last[i], tei_liu[i])
            #seriesRight3.append(jiandu_last[i], zha_liu[i])

        minMag3 = min(tei_liu)
        maxMag3 = max(tei_liu)
        #minPh3 = min(zha_liu)
        #maxPh3 = max(zha_liu)
        self.__axisLeft3.setRange(minMag3, maxMag3)
        #self.__axisRight3.setRange(minPh3, maxPh3)
        # self.__axisButtom3.setRange(1.1,1.3)
        chart3.addSeries(seriesLeft3)
        seriesLeft3.attachAxis(self.__axisButtom3)
        seriesLeft3.attachAxis(self.__axisLeft3)
        #chart3.addSeries(seriesRight3)
        #seriesRight3.attachAxis(self.__axisButtom3)
        #seriesRight3.attachAxis(self.__axisRight3)
        self.__axisLeft3.setTitleText('硫含量(Wt%)')
        #self.__axisRight3.setTitleText('硫含量(Wt%)')
        self.__axisButtom3.setTitleText('碱度')
        # self.__axisLeft3.setTitleFont(self.font)
        # self.__axisRight3.setTitleFont(self.font)
        # self.__axisButtom3.setTitleFont(self.font)
        seriesLeft3.setName('铁中硫含量')
        #seriesRight3.setName('渣中硫含量')
        self.__axisLeft3.setTitleFont(self.font)
        #self.__axisRight3.setTitleFont(self.font)
        self.__axisButtom3.setTitleFont(self.font)
        self.__axisLeft3.setLabelsFont(self.labelfont)
        #self.__axisRight3.setLabelsFont(self.labelfont)
        self.__axisButtom3.setLabelsFont(self.labelfont)
        # 第四张图
        same_MgO = df[df['MgO'] == result3['MgO'].values[0]]
        same_MgO_jiandu = same_MgO[same_MgO['碱度R2'] == result3['碱度R2'].values[0]]
        # print(same_MgO_jiandu['Al2O3'])
        fangan_same_MgO_jiandu_list = same_MgO_jiandu['方案'].values
        # print(fangan_same_MgO_jiandu_list)
        Al2O3_last = same_MgO_jiandu['Al2O3'].values
        # print(Al2O3_last)
        #print('得到mgo和碱度不变，al2o3改变的方案序号为：', fangan_same_MgO_jiandu_list)
        zha_liu = []
        tei_liu = []
        # print('=======================================')
        for item in fangan_same_MgO_jiandu_list:
            # print(item)
            item = item.split('#')[0]
            fangan_path = r'.\硫分配\拷贝脱硫\\' + str(zhabi) + '\\' + item + '.xlsx'
            #print('匹配的渣比方案路径为：', fangan_path)
            df2 = pd.read_excel(fangan_path)
            Alpha = df2['Alpha'][0:]
            closed_index4 = closest(Alpha, s)
            result4 = df2.iloc[closed_index4, :]

            temperature = result4['T(C)'][0:]
            closed_index5 = closest(temperature, t)
            result5 = result4.iloc[closed_index5, :]
            #print('方案' + str(item) + '对应的Page:' + str(result5['-Page-'].values[0]))

            tei_liu.append((result5['Wt%-S(FeLQ)'].values[0]+0.005)*rate_s*rate_zhabi)
            zha_liu.append(result5['Wt%-S_FToxid-SLAGA#1'].values[0])
        chart4 = QChart()
        chartView4 = MyChartView(chart4,self)  # 创建 chartView
        # chartView4.setChart(chart4)  # chart添加到chartView
        chartView4.setGeometry(405, 410, 400, 400)

        self.__axisButtom4 = QValueAxis()
        self.__axisLeft4 = QValueAxis()
        #self.__axisRight4 = QValueAxis()
        self.__axisLeft4.setLabelFormat("%.4f")
        chart4.addAxis(self.__axisButtom4, Qt.AlignBottom)
        chart4.addAxis(self.__axisLeft4, Qt.AlignLeft)
        # chart4.addAxis(self.__axisRight4, Qt.AlignRight)
        #
        seriesLeft4 = QLineSeries()
        #seriesRight4 = QLineSeries()
        seriesLeft4.hovered.connect(self.do_series_hovered)  # 信号 hovered
        seriesLeft4.clicked.connect(self.do_series_clicked)  # 信号 clicked
        #seriesRight4.hovered.connect(self.do_series_hovered)  # 信号 hovered
        #seriesRight4.clicked.connect(self.do_series_clicked)  # 信号 clicked
        #pen = seriesRight4.pen()
        #pen.setColor(Qt.green)
        #pen.setWidth(4)
        #seriesRight4.setPen(pen)
        pen = seriesLeft4.pen()
        pen.setColor(Qt.blue)
        pen.setWidth(4)
        seriesLeft4.setPen(pen)
        for i in range(len(Al2O3_last)):
            seriesLeft4.append(Al2O3_last[i], tei_liu[i])
            #seriesRight4.append(Al2O3_last[i], zha_liu[i])
        #

        # print(tei_liu)
        # print(zha_liu)
        minMag4 = min(tei_liu)
        maxMag4 = max(tei_liu)
        if minMag4 == maxMag4:
            minMag4 = minMag4 - 0.001
            maxMag4 = maxMag4 + 0.001
        minPh4 = min(zha_liu)
        maxPh4 = max(zha_liu)
        # print(minMag4,maxMag4,minPh4,maxPh4)
        self.__axisLeft4.setRange(minMag4, maxMag4)
        # self.__axisRight4.setRange(minPh4, maxPh4)
        # # self.__axisButtom3.setRange(1.1,1.3)
        chart4.addSeries(seriesLeft4)
        seriesLeft4.attachAxis(self.__axisButtom4)
        seriesLeft4.attachAxis(self.__axisLeft4)
        #chart4.addSeries(seriesRight4)
        #seriesRight4.attachAxis(self.__axisButtom4)
        #seriesRight4.attachAxis(self.__axisRight4)
        self.__axisLeft4.setTitleText('硫含量(Wt%)')
        # self.__axisRight4.setTitleText('硫含量(Wt%)')
        self.__axisButtom4.setTitleText('三氧化二铝')
        # self.__axisLeft4.setTitleFont(self.font)
        # self.__axisRight4.setTitleFont(self.font)
        # self.__axisButtom4.setTitleFont(self.font)
        seriesLeft4.setName('铁中硫含量')
        #seriesRight4.setName('渣中硫含量')
        self.__axisLeft4.setTitleFont(self.font)
        # self.__axisRight4.setTitleFont(self.font)
        self.__axisButtom4.setTitleFont(self.font)
        self.__axisLeft4.setLabelsFont(self.labelfont)
        #self.__axisRight4.setLabelsFont(self.labelfont)
        self.__axisButtom4.setLabelsFont(self.labelfont)
        #
    def getMeltingData(self,paremeters):
        df = self.df # 读入的表
        al2o3_input = paremeters['Al2O3']
        mog_input = paremeters['MgO']
        jiandu_input = paremeters['jiandu']
        zhabi = paremeters['zhabi']
        s = paremeters['s']
        t = paremeters['t']
        al2o3 = df['Al2O3']
        closed_index1 = closest(al2o3, al2o3_input)
        # print(closed_index1,'Al2O3')
        result1 = df.iloc[closed_index1, :]
        #
        mgo = result1['MgO']
        closed_index2 = closest(mgo, mog_input)
        result2 = result1.iloc[closed_index2, :]
        #
        ratio_sio2_cao = round(result2['CaO'] / result2['SiO2'], 2)
        closed_index3 = closest(ratio_sio2_cao, jiandu_input)
        result3 = result2.iloc[closed_index3, :]
        # 得到方案
        fangan_num = result3['方案'].values[0].split('#')[0]
        # path = D:\zhang\熔化性能
        # print(fangan_num,'方案')
        fangan_path = '.\熔化性能\\' + fangan_num + '.xlsx'
        # print(fangan_path)
        # 读取方案的excel
        df2 = pd.read_excel(fangan_path)[0:256]
        yexiangliang_lie = df2['g-xid-SLAGA#1']
        yexiangliang_lie = yexiangliang_lie[0:len(yexiangliang_lie) - 1]
        closed_index_20 = closest(yexiangliang_lie, 20)
        result_20 = df2.iloc[closed_index_20]
        closed_index_50 = closest(yexiangliang_lie, 50)
        result_50 = df2.iloc[closed_index_50]
        closed_index_80 = closest(yexiangliang_lie, 80)
        result_80 = df2.iloc[closed_index_80]
        #
        # print('开始熔化温度：',result_20['T(C)'].values,'这里')
        # print('熔化终了温度：', result_80['T(C)'].values,'这里')
        #text = '开始熔化温度：' + str(result_20['T(C)'].values[0])+'℃' + '熔化终了温度：' +str(result_80['T(C)'].values[0])+'℃'
        #self.ui_parent.label_11.setText(text)
        x = [result_20['T(C)'].values, result_50['T(C)'].values, result_80['T(C)'].values]
        y = [result_20['g-xid-SLAGA#1'].values, result_50['g-xid-SLAGA#1'].values, result_80['g-xid-SLAGA#1'].values]
        chart = QChart()  # 创建 chart
        chartView = MyChartView(chart,self)  # 创建 chartView
        # chartView.setChart(chart)  # chart添加到chartView
        chartView.setGeometry(0, 0, 550, 420)
        #scatter = QScatterSeries()
        scatter1 = QLineSeries()
        pen = scatter1.pen()
        pen.setColor(Qt.green)
        pen.setWidth(4)
        scatter1.setPen(pen)
        scatter1.hovered.connect(self.do_series_hovered)  # 信号 hovered
        scatter1.clicked.connect(self.do_series_clicked)  # 信号 clicked
        #chart.addSeries(scatter)  # 序列添加到图表
        chart.addSeries(scatter1)
        # for i in range(len(x)):
        #     #(x[i][0], y[i][0])
        #     scatter.append(x[i][0], y[i][0])
        for i in range(len(df2)-2):
            scatter1.append(df2['T(C)'][i], df2['g-xid-SLAGA#1'][i])
        #print(scatter1)
        # 创建坐标轴
        axisX = QValueAxis()  # x轴
        #print(df2['T(C)'][0:-2])
        minT = min(df2['T(C)'][0:-2])
        maxT = max(df2['T(C)'][0:-2])
        axisX.setRange(minT,maxT)  # 设置坐标轴范围
        axisX.setTitleText("Temperature(℃)")  # 轴标题
        axisY = QValueAxis()  # y轴
        axisY.setRange(-5, 110)
        axisY.setTitleText("liquidus(Wt%)")
        axisX.setTitleFont(self.labelfont)
        axisY.setTitleFont(self.labelfont)
        axisX.setLabelsFont(self.labelfont)
        axisY.setLabelsFont(self.labelfont)
        chart.setAxisX(axisX, scatter1)  # 为序列series0设置坐标轴
        chart.setAxisY(axisY, scatter1)
        #chart.setAxisX(axisX, scatter)  # 为序列series0设置坐标轴
        #chart.setAxisY(axisY, scatter)

        same_jiandu = df[df['碱度R2'] == result3['碱度R2'].values[0]]
        same_jiandu_al2o3 = same_jiandu[same_jiandu['Al2O3'] == result3['Al2O3'].values[0]]
        # print(same_jiandu_al2o3['MgO'])
        fangan_same_jandu_al2o3_list = same_jiandu_al2o3['方案'].values
        # print('得到碱度和al2o3不变，mgo改变的方案序号为：', fangan_same_jandu_al2o3_list)
        mgo_last = same_jiandu_al2o3['MgO'].values
        yexiangliang_mgo_20 = []
        yexiangliang_mgo_50 = []
        yexiangliang_mgo_80 = []
        # print('=======================================')
        for item in fangan_same_jandu_al2o3_list:
            item = item.split('#')[0]
            fangan_path = '.\熔化性能\\' + item + '.xlsx'
            # print('匹配的渣比方案路径为4：', fangan_path)
            df2 = pd.read_excel(fangan_path)
            yexiangliang_lie = df2['g-xid-SLAGA#1']
            yexiangliang_lie = yexiangliang_lie[0:len(yexiangliang_lie) - 1]

            closed_index_20 = closest(yexiangliang_lie, 20)
            result_20 = df2.iloc[closed_index_20]
            closed_index_50 = closest(yexiangliang_lie, 50)
            result_50 = df2.iloc[closed_index_50]
            closed_index_80 = closest(yexiangliang_lie, 80)
            result_80 = df2.iloc[closed_index_80]

            yexiangliang_mgo_20.append(result_20['T(C)'])
            yexiangliang_mgo_50.append(result_50['T(C)'])
            yexiangliang_mgo_80.append(result_80['T(C)'])
        chart2 = QChart()
        chartView2 = MyChartView(chart2,self)  # 创建 chartView
        # chartView2.setChart(chart2)  # chart添加到chartView
        chartView2.setGeometry(610, 0, 550, 420)
        line1 = QSplineSeries()
        line2 = QSplineSeries()
        line3 = QSplineSeries()
        pen = line1.pen()
        pen.setColor(Qt.green)
        pen.setWidth(4)
        line1.setPen(pen)
        pen = line2.pen()
        pen.setColor(Qt.blue)
        pen.setWidth(4)
        line2.setPen(pen)
        pen = line3.pen()
        pen.setColor(Qt.yellow)
        pen.setWidth(4)
        line3.setPen(pen)
        line1.hovered.connect(self.do_series_hovered)  # 信号 hovered
        line1.clicked.connect(self.do_series_clicked)  # 信号 clicked
        line2.hovered.connect(self.do_series_hovered)  # 信号 hovered
        line2.clicked.connect(self.do_series_clicked)  # 信号 clicked
        line3.hovered.connect(self.do_series_hovered)  # 信号 hovered
        line3.clicked.connect(self.do_series_clicked)  # 信号 clicked
        line1.setName("T<sub>20%</sub>")
        line2.setName("T<sub>50%</sub>")
        line3.setName("T<sub>80%</sub>")
        chart2.addSeries(line1)
        chart2.addSeries(line2)
        chart2.addSeries(line3)
        font = QFont("Arial", 15)
        chart2.legend().setFont(font)
        # 导入数据
        for i in range(len(mgo_last)):
            #print(mgo_last[i])
            #print(yexiangliang_mgo_20[i])
            line1.append(mgo_last[i],yexiangliang_mgo_20[i])
            line2.append(mgo_last[i], yexiangliang_mgo_50[i])
            line3.append(mgo_last[i], yexiangliang_mgo_80[i])
        axisX_1 = QValueAxis()  # x轴
        axisX_1.setRange(5, 7)  # 设置坐标轴范围
        axisX_1.setTitleText("MgO(Wt%)")  # 轴标题
        axisY_1 = QValueAxis()  # y轴
        axisY_1.setRange(1220, 1450)
        axisY_1.setTitleText("Temperature(℃)")
        axisX_1.setTitleFont(self.labelfont)
        axisY_1.setTitleFont(self.labelfont)
        axisX_1.setLabelsFont(self.labelfont)
        axisY_1.setLabelsFont(self.labelfont)
        chart2.setAxisX(axisX_1, line1)  # 为序列series0设置坐标轴
        chart2.setAxisY(axisY_1, line1)
        chart2.setAxisX(axisX_1, line2)  # 为序列series0设置坐标轴
        chart2.setAxisY(axisY_1, line2)
        chart2.setAxisX(axisX_1, line3)  # 为序列series0设置坐标轴
        chart2.setAxisY(axisY_1, line3)
        #第三张图
        #print('3')
        same_jiandu = df[df['碱度R2'] == result3['碱度R2'].values[0]]
        same_jiandu_mgo = same_jiandu[same_jiandu['MgO'] == result3['MgO'].values[0]]
        # # print(same_jiandu_al2o3['MgO'])
        fangan_same_jandu_mgo_list = same_jiandu_mgo['方案'].values
        #print('得到碱度和al2o3不变，mgo改变的方案序号为：', fangan_same_jandu_mgo_list)
        al2o3_last = same_jiandu_mgo['Al2O3'].values
        #
        yexiangliang_al2o3_20 = []
        yexiangliang_al2o3_50 = []
        yexiangliang_al2o3_80 = []
        # # print('=======================================')
        for item in fangan_same_jandu_mgo_list:
            item = item.split('#')[0]
            fangan_path = '.\熔化性能\\' + item + '.xlsx'
            #print('匹配的渣比方案路径为5：', fangan_path)
            df2 = pd.read_excel(fangan_path)
            yexiangliang_lie = df2['g-xid-SLAGA#1']
            yexiangliang_lie = yexiangliang_lie[0:len(yexiangliang_lie) - 1]

            closed_index_20 = closest(yexiangliang_lie, 20)
            result_20 = df2.iloc[closed_index_20]
            closed_index_50 = closest(yexiangliang_lie, 50)
            result_50 = df2.iloc[closed_index_50]
            closed_index_80 = closest(yexiangliang_lie, 80)
            result_80 = df2.iloc[closed_index_80]

            yexiangliang_al2o3_20.append(result_20['T(C)'])
            yexiangliang_al2o3_50.append(result_50['T(C)'])
            yexiangliang_al2o3_80.append(result_80['T(C)'])
        #
        chart3 = QChart()
        chartView3 = MyChartView(chart3,self)  # 创建 chartView
        # chartView3.setChart(chart3)  # chart添加到chartView
        chartView3.setGeometry(0, 440, 550, 420)
        #
        line1 = QSplineSeries()
        line2 = QSplineSeries()
        line3 = QSplineSeries()
        pen = line1.pen()
        pen.setColor(Qt.green)
        pen.setWidth(4)
        line1.setPen(pen)
        pen = line2.pen()
        pen.setColor(Qt.blue)
        pen.setWidth(4)
        line2.setPen(pen)
        pen = line3.pen()
        pen.setColor(Qt.yellow)
        pen.setWidth(4)
        line3.setPen(pen)
        line1.hovered.connect(self.do_series_hovered)  # 信号 hovered
        line1.clicked.connect(self.do_series_clicked)  # 信号 clicked
        line2.hovered.connect(self.do_series_hovered)  # 信号 hovered
        line2.clicked.connect(self.do_series_clicked)  # 信号 clicked
        line3.hovered.connect(self.do_series_hovered)  # 信号 hovered
        line3.clicked.connect(self.do_series_clicked)  # 信号 clicked
        line1.setName("T<sub>20%</sub>")
        line2.setName("T<sub>50%</sub>")
        line3.setName("T<sub>80%</sub>")
        chart3.addSeries(line1)
        chart3.addSeries(line2)
        chart3.addSeries(line3)
        font = QFont("Arial", 15)
        chart3.legend().setFont(font)
        # # 导入数据
        #print(al2o3_last)
        for i in range(len(al2o3_last)):
            #print(al2o3_last[i])
            #print(yexiangliang_al2o3_20[i])
            line1.append(al2o3_last[i], yexiangliang_al2o3_20[i])
            line2.append(al2o3_last[i], yexiangliang_al2o3_50[i])
            line3.append(al2o3_last[i], yexiangliang_al2o3_80[i])
        axisX_1 = QValueAxis()  # x轴
        axisX_1.setRange(14, 17)  # 设置坐标轴范围
        axisX_1.setTitleText("Al2O3(Wt%)")  # 轴标题
        axisY_1 = QValueAxis()  # y轴
        axisY_1.setRange(1220, 1450)
        axisY_1.setTitleText("Temperature(℃)")
        axisX_1.setTitleFont(self.labelfont)
        axisY_1.setTitleFont(self.labelfont)
        axisX_1.setLabelsFont(self.labelfont)
        axisY_1.setLabelsFont(self.labelfont)
        chart3.setAxisX(axisX_1, line1)  # 为序列series0设置坐标轴
        chart3.setAxisY(axisY_1, line1)
        chart3.setAxisX(axisX_1, line2)  # 为序列series0设置坐标轴
        chart3.setAxisY(axisY_1, line2)
        chart3.setAxisX(axisX_1, line3)  # 为序列series0设置坐标轴
        chart3.setAxisY(axisY_1, line3)

        # 第四张
        same_al2o3 = df[df['Al2O3'] == result3['Al2O3'].values[0]]
        same_al2o3_mgo = same_al2o3[same_al2o3['MgO'] == result3['MgO'].values[0]]
        # print(same_jiandu_al2o3['MgO'])
        fangan_same_al2o3_mgo_list = same_al2o3_mgo['方案'].values
        #print('得到碱度和al2o3不变，mgo改变的方案序号为：', fangan_same_al2o3_mgo_list)
        jiandu_last = same_al2o3_mgo['碱度R2'].values

        yexiangliang_jiandu_20 = []
        yexiangliang_jiandu_50 = []
        yexiangliang_jiandu_80 = []
        # print('=======================================')
        for item in fangan_same_al2o3_mgo_list:
            item = item.split('#')[0]
            fangan_path = '.\熔化性能\\' + item + '.xlsx'
            #print('匹配的渣比方案路径为6：', fangan_path)
            df2 = pd.read_excel(fangan_path)
            yexiangliang_lie = df2['g-xid-SLAGA#1']
            yexiangliang_lie = yexiangliang_lie[0:len(yexiangliang_lie) - 1]

            closed_index_20 = closest(yexiangliang_lie, 20)
            result_20 = df2.iloc[closed_index_20]
            closed_index_50 = closest(yexiangliang_lie, 50)
            result_50 = df2.iloc[closed_index_50]
            closed_index_80 = closest(yexiangliang_lie, 80)
            result_80 = df2.iloc[closed_index_80]

            yexiangliang_jiandu_20.append(result_20['T(C)'])
            yexiangliang_jiandu_50.append(result_50['T(C)'])
            yexiangliang_jiandu_80.append(result_80['T(C)'])

        chart4 = QChart()
        chartView4 = MyChartView(chart4,self)  # 创建 chartView
        # chartView4.setChart(chart4)  # chart添加到chartView
        chartView4.setGeometry(610, 440, 550, 420)
        line1 = QSplineSeries()
        line2 = QSplineSeries()
        line3 = QSplineSeries()
        pen = line1.pen()
        pen.setColor(Qt.green)
        pen.setWidth(4)
        line1.setPen(pen)
        pen = line2.pen()
        pen.setColor(Qt.blue)
        pen.setWidth(4)
        line2.setPen(pen)
        pen = line3.pen()
        pen.setColor(Qt.yellow)
        pen.setWidth(4)
        line3.setPen(pen)
        line1.hovered.connect(self.do_series_hovered)  # 信号 hovered
        line1.clicked.connect(self.do_series_clicked)  # 信号 clicked
        line2.hovered.connect(self.do_series_hovered)  # 信号 hovered
        line2.clicked.connect(self.do_series_clicked)  # 信号 clicked
        line3.hovered.connect(self.do_series_hovered)  # 信号 hovered
        line3.clicked.connect(self.do_series_clicked)  # 信号 clicked
        line1.setName("T<sub>20%</sub>")
        line2.setName("T<sub>50%</sub>")
        line3.setName("T<sub>80%</sub>")
        chart4.addSeries(line1)
        chart4.addSeries(line2)
        chart4.addSeries(line3)
        font = QFont("Arial", 15)
        chart4.legend().setFont(font)

        # # 导入数据
        #print(al2o3_last)
        for i in range(len(jiandu_last)):
            line1.append(jiandu_last[i], yexiangliang_jiandu_20[i])
            line2.append(jiandu_last[i], yexiangliang_jiandu_50[i])
            line3.append(jiandu_last[i], yexiangliang_jiandu_80[i])
        # print(tei_liu)
        axisX_1 = QValueAxis()  # x轴
        axisX_1.setRange(1.1, 1.3)  # 设置坐标轴范围
        axisX_1.setTitleText("basicity")  # 轴标题
        axisY_1 = QValueAxis()  # y轴
        axisY_1.setRange(1220, 1450)
        axisY_1.setTitleText("Temperature(℃)")
        axisX_1.setTitleFont(self.labelfont)
        axisY_1.setTitleFont(self.labelfont)
        axisX_1.setLabelsFont(self.labelfont)
        axisY_1.setLabelsFont(self.labelfont)
        chart4.setAxisX(axisX_1, line1)  # 为序列series0设置坐标轴
        chart4.setAxisY(axisY_1, line1)
        chart4.setAxisX(axisX_1, line2)  # 为序列series0设置坐标轴
        chart4.setAxisY(axisY_1, line2)
        chart4.setAxisX(axisX_1, line3)  # 为序列series0设置坐标轴
        chart4.setAxisY(axisY_1, line3)
    def showNianDu(self, paremeters):
        df = pd.read_excel('.\粘度\合并.xlsx')
        al2o3 = df['Al2O3\n [g]']
        closed_index1 = closest(al2o3, paremeters['Al2O3'])
        result1 = df.iloc[closed_index1, :]
        mgo = result1['MgO\n [g]']
        closed_index2 = closest(mgo, paremeters['MgO'])
        result2 = result1.iloc[closed_index2, :]
        ratio_sio2_cao = round(result2['CaO\n [g]'] / result2['SiO2\n [g]'], 2)
        # ratio_sio2_cao.to_excel('监督.xlsx')
        jiandu_input = paremeters['jiandu']
        last_number_jiandu = int(list(jiandu_input)[-1])
        if last_number_jiandu % 2 != 0:
            jiandu_input = round(float(jiandu_input) + 0.01, 2)
        closed_index3 = closest(ratio_sio2_cao, jiandu_input)
        # print('here1',jiandu_input)
        # print('here2', closed_index3)
        result3 = result2.iloc[closed_index3, :]
        # =
        t_list = result3['Temperature [篊]']
        closed_index4 = closest(t_list, paremeters['t'])
        niandu_result = result3.iloc[closed_index4, :]
        line1 = QSplineSeries()
        pen = line1.pen()
        pen.setColor(Qt.green)
        pen.setWidth(4)
        line1.setPen(pen)
        line1.hovered.connect(self.do_series_hovered)  # 信号 hovered
        line1.clicked.connect(self.do_series_clicked)  # 信号 clicked
        for i in range(len(result3)):
            #print(result3.iloc[i]['Temperature [篊]'],result3.iloc[i]['visc[poise]'])
            line1.append(result3.iloc[i]['Temperature [篊]'],result3.iloc[i]['visc[poise]']/10)
        #print(line1)
        chart = QChart()  # 创建 chart
        chartView = MyChartView(chart,self)  # 创建 chartView
        # chartView.setChart(chart)  # chart添加到chartView
        chartView.setGeometry(0, 0, 400, 400)
        chart.addSeries(line1)
        axisX_1 = QValueAxis()  # x轴
        axisX_1.setRange(1400,1560)  # 设置坐标轴范围
        axisX_1.setTitleText("Temperature(℃)")  # 轴标题
        axisY_1 = QValueAxis()  # y轴
        axisY_1.setRange(0.1,0.6)
        axisY_1.setTitleText("粘度 (Pa·s)")
        axisX_1.setTitleFont(self.labelfont)
        axisY_1.setTitleFont(self.font)
        axisX_1.setLabelsFont(self.labelfont)
        axisY_1.setLabelsFont(self.labelfont)
        chart.setAxisX(axisX_1, line1)  # 为序列series0设置坐标轴
        chart.setAxisY(axisY_1, line1)

        result1 = df
        mgo = result1['MgO\n [g]']
        closed_index2 = closest(mgo, paremeters['MgO'])
        result2 = result1.iloc[closed_index2, :]

        ratio_sio2_cao = round(result2['CaO\n [g]'] / result2['SiO2\n [g]'], 2)
        #ratio_sio2_cao.to_excel('监督.xlsx')
        closed_index3 = closest(ratio_sio2_cao, jiandu_input)
        result3 = result2.iloc[closed_index3, :]

        t_list = result3['Temperature [篊]']
        closed_index4 = closest(t_list, paremeters['t'])
        result4 = result3.iloc[closed_index4, :]

        line2 = QSplineSeries()
        pen = line2.pen()
        pen.setColor(Qt.green)
        pen.setWidth(4)
        line2.setPen(pen)
        line2.hovered.connect(self.do_series_hovered)  # 信号 hovered
        line2.clicked.connect(self.do_series_clicked)  # 信号 clicked
        #print(result4)
        for i in range(len(result4)):
            line2.append(result4.iloc[i]['Al2O3\n [g]'], result4.iloc[i]['visc[poise]']/10)

        chart2 = QChart()
        chartView2 = MyChartView(chart2,self)  # 创建 chartView
        # chartView2.setChart(chart2)  # chart添加到chartView
        chartView2.setGeometry(405, 0, 400, 400)
        chart2.addSeries(line2)
        minMag2 = min(result4['Al2O3\n [g]'])
        maxMag2 = max(result4['Al2O3\n [g]'])
        minPh2 = min(result4['visc[poise]']/10)
        maxPh2 = max(result4['visc[poise]']/10)
        axisX_2 = QValueAxis()  # x轴
        axisX_2.setRange(minMag2, maxMag2)  # 设置坐标轴范围
        axisX_2.setTitleText("三氧化二铝")  # 轴标题
        axisY_2 = QValueAxis()  # y轴
        axisY_2.setRange(minPh2, maxPh2)
        axisY_2.setTitleText("粘度 (Pa·s)")
        axisX_2.setTitleFont(self.font)
        axisY_2.setTitleFont(self.font)
        axisX_2.setLabelsFont(self.labelfont)
        axisY_2.setLabelsFont(self.labelfont)
        chart2.setAxisX(axisX_2, line2)  # 为序列series0设置坐标轴
        chart2.setAxisY(axisY_2, line2)

        al2o3 = df['Al2O3\n [g]']
        closed_index1 = closest(al2o3, paremeters['Al2O3'])
        result1 = df.iloc[closed_index1, :]
        result2 = result1

        ratio_sio2_cao = round(result2['CaO\n [g]'] / result2['SiO2\n [g]'], 2)
        # ratio_sio2_cao.to_excel('监督.xlsx')
        closed_index3 = closest(ratio_sio2_cao, jiandu_input)
        result3 = result2.iloc[closed_index3, :]

        t_list = result3['Temperature [篊]']
        closed_index4 = closest(t_list, paremeters['t'])
        result4 = result3.iloc[closed_index4, :]
        line3 = QSplineSeries()
        pen = line3.pen()
        pen.setColor(Qt.green)
        pen.setWidth(4)
        line3.setPen(pen)
        line3.hovered.connect(self.do_series_hovered)  # 信号 hovered
        line3.clicked.connect(self.do_series_clicked)  # 信号 clicked
        for i in range(len(result4)):
            # print(result4.iloc[i]['MgO\n [g]'], result4.iloc[i]['visc[poise]'])
            line3.append(result4.iloc[i]['MgO\n [g]'], result4.iloc[i]['visc[poise]']/10)
        chart3 = QChart()
        chartView3 = MyChartView(chart3,self)  # 创建 chartView
        # chartView3.setChart(chart3)  # chart添加到chartView
        chartView3.setGeometry(0, 405, 400, 400)
        chart3.addSeries(line3)
        minMag3 = min(result4['MgO\n [g]'])
        maxMag3 = max(result4['MgO\n [g]'])
        minPh3 = min(result4['visc[poise]']/10)
        maxPh3 = max(result4['visc[poise]']/10)
        axisX_3 = QValueAxis()  # x轴
        axisX_3.setRange(minMag3, maxMag3)  # 设置坐标轴范围
        axisX_3.setTitleText("氧化镁")  # 轴标题
        axisY_3 = QValueAxis()  # y轴
        axisY_3.setRange(minPh3, maxPh3)
        axisY_3.setTitleText("粘度 (Pa·s)")
        axisX_3.setTitleFont(self.font)
        axisY_3.setTitleFont(self.font)
        axisX_3.setLabelsFont(self.labelfont)
        axisY_3.setLabelsFont(self.labelfont)
        chart3.setAxisX(axisX_3, line3)  # 为序列series0设置坐标轴
        chart3.setAxisY(axisY_3, line3)

        al2o3 = df['Al2O3\n [g]']
        closed_index1 = closest(al2o3, paremeters['Al2O3'])
        result1 = df.iloc[closed_index1, :]

        mgo = result1['MgO\n [g]']
        closed_index2 = closest(mgo, paremeters['MgO'])
        result2 = result1.iloc[closed_index2, :]
        result3 = result2
        t_list = result3['Temperature [篊]']
        closed_index4 = closest(t_list, paremeters['t'])
        result4 = result3.iloc[closed_index4, :]
        line4 = QSplineSeries()
        pen = line4.pen()
        pen.setColor(Qt.green)
        pen.setWidth(4)
        line4.setPen(pen)
        line4.hovered.connect(self.do_series_hovered)  # 信号 hovered
        line4.clicked.connect(self.do_series_clicked)  # 信号 clicked
        for i in range(len(result4)):
            line4.append((result4.iloc[i]['CaO\n [g]']/result4.iloc[i]['SiO2\n [g]']), result4.iloc[i]['visc[poise]']/10)

        chart4 = QChart()
        chartView4 = MyChartView(chart4,self)  # 创建 chartView
        #chartView4.setChart(chart4)  # chart添加到chartView
        chartView4.setGeometry(405, 410, 400, 400)
        chart4.addSeries(line4)
        minMag4 = min(result4['CaO\n [g]']/result4['SiO2\n [g]'])
        maxMag4 = max(result4['CaO\n [g]']/result4['SiO2\n [g]'])
        minPh4 = min(result4['visc[poise]']/10)
        maxPh4 = max(result4['visc[poise]']/10)
        axisX_4 = QValueAxis()  # x轴
        axisX_4.setRange(minMag4, maxMag4)  # 设置坐标轴范围
        axisX_4.setTitleText("碱度")  # 轴标题
        axisY_4 = QValueAxis()  # y轴
        axisY_4.setRange(minPh4, maxPh4)
        axisY_4.setTitleText("粘度 (Pa·s)")
        axisX_4.setTitleFont(self.font)
        axisY_4.setTitleFont(self.font)
        axisX_4.setLabelsFont(self.labelfont)
        axisY_4.setLabelsFont(self.labelfont)
        chart4.setAxisX(axisX_4, line4)  # 为序列series0设置坐标轴
        chart4.setAxisY(axisY_4, line4)

    def do_series_hovered(self, point, state):  ##序列的hovered信号
        if state:
            hint = "X=%.2f\nY=%.3f" % (point.x(), point.y())
            self.ui.label.setText(hint)
        else:
            self.ui.label.setText("X=\n Y=")
            pass

    def do_series_clicked(self, point):  ##序列的clicked信号
        hint = "X=%.2f\nY=%.3f" % (point.x(), point.y())
        self.ui.label.setText(hint)

class QSubDataWidget(QWidget):
    def __init__(self, parent=None,historyInfo=None,ui=None):
        super().__init__(parent)    #调用父类构造函数，创建窗体
        self.ui_parent = ui
        self.ui = Ui_Form()         #创建UI对象
        self.ui.setupUi(self)       #构造UI
        self.font = QtGui.QFont()
        self.font.setFamily("宋体")
        self.font.setPointSize(9)
        self.font.setWeight(50)
        self.labelfont = QtGui.QFont()
        self.labelfont.setFamily("Arial")
        self.labelfont.setPointSize(9)
        self.labelfont.setWeight(50)
        self.showView(historyInfo)
        self.setMouseTracking(True)


    def showView(self,historyInfo):
        T_20_list = []
        T_80_list = []
        s_tie_list = []
        s_zha_list = []
        rate_list = []
        niandu_list = []
        #print(historyInfo)
        for item in historyInfo:
            #print(item)
            T_20 = item['MeltingPerform'].split('T<sub>20%</sub>=')[1].split(';')[0].replace('↑','').replace('↓','').replace('-','')
            #print(T_20)
            T_80 = item['MeltingPerform'].split('T<sub>80%</sub>=')[1].replace('↑','').replace('↓','').replace('-','')
            #print(T_80)
            s_tie = item['SulfurDistribution'].split('[s]=')[1].split(';')[0].replace('↑','').replace('↓','').replace('-','')
            #print(s_tie)
            s_zha = item['SulfurDistribution'].split('(s)=')[1].split(';')[0].replace('↑','').replace('↓','').replace('-','')
            rate = item['SulfurDistribution'].split('Ls=')[1].replace('↑','').replace('↓','').replace('-','')
            #print(s_zha)
            niandu = item['NianDu'].split('ŋ<sub>粘度</sub>=')[1].replace('↑','').replace('↓','').replace('-','')
            #print(niandu)
            #print(T_20,T_80,s_tie,s_zha,niandu)
            T_20_list.append(float(T_20))
            T_80_list.append(float(T_80))
            s_tie_list.append(float(s_tie))
            s_zha_list.append(float(s_zha))
            rate_list.append(float(rate))
            niandu_list.append(float(niandu))

        chart = QChart()  # 创建 chart
        chartView = MyChartView(chart,self)  # 创建 chartView
        # chartView.setChart(chart)  # chart添加到chartView
        chartView.setGeometry(0, 0, 400, 400)
        # # ## bottom 轴是 QLogValueAxis
        self.__axisButtom = QValueAxis()
        self.__axisButtom.setTickCount(len(T_20_list))
        self.__axisButtom.setLabelFormat('%d')
        chart.addAxis(self.__axisButtom, Qt.AlignBottom)
        self.__axisLeft = QValueAxis()
        chart.addAxis(self.__axisLeft, Qt.AlignLeft)
        seriesLeft_1 = QLineSeries()
        seriesLeft_2 = QLineSeries()
        seriesLeft_1.hovered.connect(self.do_series_hovered)  # 信号 hovered
        seriesLeft_1.clicked.connect(self.do_series_clicked)  # 信号 clicked
        seriesLeft_2.hovered.connect(self.do_series_hovered)  # 信号 hovered
        seriesLeft_2.clicked.connect(self.do_series_clicked)  # 信号 clicked
        for i in range(len(T_20_list)):
            seriesLeft_1.append(i+1,T_20_list[i])
            seriesLeft_2.append(i+1,T_80_list[i])
        self.__axisLeft.setRange(1200, 1500)
        chart.addSeries(seriesLeft_1)
        chart.addSeries(seriesLeft_2)
        seriesLeft_1.attachAxis(self.__axisButtom)
        seriesLeft_1.attachAxis(self.__axisLeft)
        seriesLeft_2.attachAxis(self.__axisButtom)
        seriesLeft_2.attachAxis(self.__axisLeft)
        seriesLeft_1.setName('T20%')
        seriesLeft_2.setName('T80%')
        self.__axisLeft.setTitleText('温度 (℃)')
        self.__axisButtom.setTitleText('查询次数')
        self.__axisLeft.setTitleFont(self.font)
        self.__axisButtom.setTitleFont(self.font)
        self.__axisLeft.setLabelsFont(self.labelfont)
        self.__axisButtom.setLabelsFont(self.labelfont)

        chart2 = QChart()  # 创建 chart
        chartView2 = MyChartView(chart2,self)  # 创建 chartView
        # chartView2.setChart(chart2)  # chart添加到chartView
        chartView2.setGeometry(0, 410, 400, 400)
        # # ## bottom 轴是 QLogValueAxis
        self.__axisButtom2 = QValueAxis()
        self.__axisButtom2.setTickCount(len(s_tie_list))
        self.__axisButtom2.setLabelFormat('%d')
        chart2.addAxis(self.__axisButtom2, Qt.AlignBottom)
        self.__axisLeft2 = QValueAxis()
        chart2.addAxis(self.__axisLeft2, Qt.AlignLeft)
        #
        seriesLeft_tie = QLineSeries()
        seriesLeft_tie.hovered.connect(self.do_series_hovered)  # 信号 hovered
        seriesLeft_tie.clicked.connect(self.do_series_clicked)  # 信号 clicked
        # seriesLeft_tie.setColor("black")
        #
        for i in range(len(s_tie_list)):
            seriesLeft_tie.append(i + 1, s_tie_list[i])
        #
        self.__axisLeft2.setRange(0.01, 0.1)
        chart2.addSeries(seriesLeft_tie)
        seriesLeft_tie.attachAxis(self.__axisButtom2)
        seriesLeft_tie.attachAxis(self.__axisLeft2)
        seriesLeft_tie.setName('铁中硫含量')
        self.__axisLeft2.setTitleText('铁中硫含量 (wt%)')
        self.__axisButtom2.setTitleText('查询次数')
        self.__axisLeft2.setTitleFont(self.font)
        self.__axisButtom2.setTitleFont(self.font)
        self.__axisLeft2.setLabelsFont(self.labelfont)
        self.__axisButtom2.setLabelsFont(self.labelfont)
        #
        chart3 = QChart()  # 创建 chart
        chartView3 = MyChartView(chart3,self)  # 创建 chartView
        # chartView3.setChart(chart3)  # chart添加到chartView
        chartView3.setGeometry(405, 410, 400, 400)
        # # ## bottom 轴是 QLogValueAxis
        self.__axisButtom3 = QValueAxis()
        self.__axisButtom3.setTickCount(len(s_zha_list))
        self.__axisButtom3.setLabelFormat('%d')
        chart3.addAxis(self.__axisButtom3, Qt.AlignBottom)
        self.__axisLeft3 = QValueAxis()
        chart3.addAxis(self.__axisLeft3, Qt.AlignLeft)
        #
        seriesLeft_zha = QLineSeries()
        seriesLeft_zha.hovered.connect(self.do_series_hovered)  # 信号 hovered
        seriesLeft_zha.clicked.connect(self.do_series_clicked)  # 信号 clicked
        # seriesLeft_zha.setColor("green")
        #
        for i in range(len(s_zha_list)):
            seriesLeft_zha.append(i + 1, s_zha_list[i])
        #
        self.__axisLeft3.setRange(0, 1.3)
        chart3.addSeries(seriesLeft_zha)
        seriesLeft_zha.attachAxis(self.__axisButtom3)
        seriesLeft_zha.attachAxis(self.__axisLeft3)
        seriesLeft_zha.setName('渣中硫含量')
        self.__axisLeft3.setTitleText('渣中硫含量 (wt%)')
        self.__axisButtom3.setTitleText('查询次数')
        self.__axisLeft3.setTitleFont(self.font)
        self.__axisButtom3.setTitleFont(self.font)
        self.__axisLeft3.setLabelsFont(self.labelfont)
        self.__axisButtom3.setLabelsFont(self.labelfont)
        #
        chart4 = QChart()  # 创建 chart
        chartView4 = MyChartView(chart4,self)  # 创建 chartView
        # chartView4.setChart(chart4)  # chart添加到chartView
        chartView4.setGeometry(405, 0, 400, 400)
        # # ## bottom 轴是 QLogValueAxis
        self.__axisButtom4 = QValueAxis()
        self.__axisButtom4.setTickCount(len(niandu_list))
        self.__axisButtom4.setLabelFormat('%d')
        chart4.addAxis(self.__axisButtom4, Qt.AlignBottom)
        self.__axisLeft4 = QValueAxis()
        chart4.addAxis(self.__axisLeft4, Qt.AlignLeft)
        #
        seriesLeft_niandu = QLineSeries()
        seriesLeft_niandu.hovered.connect(self.do_series_hovered)  # 信号 hovered
        seriesLeft_niandu.clicked.connect(self.do_series_clicked)  # 信号 clicked
        # seriesLeft_niandu.setColor("blue")
        #
        for i in range(len(niandu_list)):
            seriesLeft_niandu.append(i + 1, niandu_list[i])
        #
        self.__axisLeft4.setRange(0.1, 0.8)
        chart4.addSeries(seriesLeft_niandu)
        seriesLeft_niandu.attachAxis(self.__axisButtom4)
        seriesLeft_niandu.attachAxis(self.__axisLeft4)
        seriesLeft_niandu.setName('粘度')
        self.__axisLeft4.setTitleText('粘度 (Pa·s)')
       # self.__axisLeft4.setTitleFont(self.font)
        self.__axisButtom4.setTitleText('查询次数')
        self.__axisButtom4.setTitleFont(self.font)
        self.__axisLeft4.setTitleFont(self.font)
        self.__axisButtom4.setTitleFont(self.font)
        self.__axisLeft4.setLabelsFont(self.labelfont)
        self.__axisButtom4.setLabelsFont(self.labelfont)

        chart5 = QChart()  # 创建 chart
        chartView5 = MyChartView(chart5, self)  # 创建 chartView
        # chartView3.setChart(chart3)  # chart添加到chartView
        chartView5.setGeometry(810, 410, 400, 400)
        # # # ## bottom 轴是 QLogValueAxis
        self.__axisButtom5 = QValueAxis()
        self.__axisButtom5.setTickCount(len(rate_list))
        self.__axisButtom5.setLabelFormat('%d')
        chart5.addAxis(self.__axisButtom5, Qt.AlignBottom)
        self.__axisLeft5 = QValueAxis()
        chart5.addAxis(self.__axisLeft5, Qt.AlignLeft)
        # #
        seriesLeft_rate = QLineSeries()
        seriesLeft_rate.hovered.connect(self.do_series_hovered)  # 信号 hovered
        seriesLeft_rate.clicked.connect(self.do_series_clicked)  # 信号 clicked
        # # seriesLeft_zha.setColor("green")
        # #
        for i in range(len(rate_list)):
            print(rate_list[i])
            seriesLeft_rate.append(i + 1, rate_list[i])
        # #
        self.__axisLeft5.setRange(0, 200)
        chart5.addSeries(seriesLeft_rate)
        seriesLeft_rate.attachAxis(self.__axisButtom5)
        seriesLeft_rate.attachAxis(self.__axisLeft5)
        seriesLeft_rate.setName('硫分配比')
        self.__axisLeft5.setTitleText('硫分配比 ((s)/[s])')
        self.__axisButtom5.setTitleText('查询次数')
        self.__axisLeft5.setTitleFont(self.font)
        self.__axisButtom5.setTitleFont(self.font)
        self.__axisLeft5.setLabelsFont(self.labelfont)
        self.__axisButtom5.setLabelsFont(self.labelfont)

    def do_series_hovered(self, point, state):  ##序列的hovered信号
        if state:
            hint = "X=%.2f\nY=%.3f" % (point.x(), point.y())
            self.ui.label.setText(hint)
        else:
            self.ui.label.setText("X=\n Y=")
            pass

    def do_series_clicked(self, point):  ##序列的clicked信号
        hint = "X=%.2f\nY=%.3f" % (point.x(), point.y())
        self.ui.label.setText(hint)


class MyChartView(QChartView):
    def __init__(self, chart, parent=None):
        super().__init__(chart, parent)

        # 创建虚线
        self.line_item = QGraphicsLineItem()
        # self.line_item.setPen(Qt.DashLine)
        chart.scene().addItem(self.line_item)
        self.line_item.hide()

        # 创建显示坐标的文本项
        self.text_items = []
        for i in range(6):
            self.text_item = QGraphicsTextItem()
            self.text_item.setPos(QPointF(50, 50))
            chart.scene().addItem(self.text_item)
            self.text_item.hide()
            self.text_items.append(self.text_item)

    def mouseMoveEvent(self, event):
        # 获取鼠标位置
        pos = event.pos()
        chart_pos = self.chart().mapToValue(pos)
        # 更新虚线的位置
        self.line_item.setLine(pos.x(), self.chart().plotArea().top(),
                               pos.x(), self.chart().plotArea().bottom())
        self.line_item.show()

        # 查找与虚线相交的线段的坐标
        intersection_points = self.find_intersection(chart_pos)

        # 显示交点坐标
        if len(intersection_points) != 0:
            # print(len(intersection_points))
            for index,intersection_point in enumerate(intersection_points):
                if self.chart().mapToPosition(intersection_point).x()<225:
                    self.text_items[index].setPlainText(f"({intersection_point.x()}, {intersection_point.y()})")
                    self.text_items[index].setPos(self.chart().mapToPosition(intersection_point))
                    self.text_items[index].show()
                else:
                    self.text_items[index].setPlainText(f"({intersection_point.x()}, {intersection_point.y()})")
                    realy_pos = self.chart().mapToPosition(intersection_point)
                    x = realy_pos.x() -100
                    y = realy_pos.y()
                    self.text_items[index].setPos(QPointF(x, y))
                    self.text_items[index].show()
        else:
            self.text_items[0].hide()
            self.text_items[1].hide()
            self.text_items[2].hide()
            self.text_items[3].hide()
            self.text_items[4].hide()
            self.text_items[5].hide()


    def leaveEvent(self, event):
        # 鼠标离开图表时隐藏虚线和文本项
        self.line_item.hide()
        self.text_items[0].hide()
        self.text_items[1].hide()
        self.text_items[2].hide()

    def find_intersection(self, mouse_point):
        # 查找与虚线相交的线段的坐标
        intersection_points = []
        for index in range(len(self.chart().series())):
            series = self.chart().series()[index]
            points = series.points()
            for i in range(len(points) - 1):
                p1 = points[i]
                p2 = points[i + 1]
                # 判断虚线是否在图表范围内
                if self.is_point_on_line(mouse_point, p1, p2):
                    intersection_point = self.intersection_point(mouse_point, p1, p2)
                    intersection_points.append(intersection_point)
                    break
        return intersection_points

    def is_point_on_line(self, point, line_start, line_end):
        # 判断点是否在线段上
        x_min = min(line_start.x(), line_end.x())
        x_max = max(line_start.x(), line_end.x())
        return x_min <= point.x() <= x_max


    def intersection_point(self, mouse_point, line_start, line_end):
        # 返回交点坐标
        x2, y2 = line_start.x(), line_start.y()
        x3, y3 = line_end.x(), line_end.y()
        x1, y1 = mouse_point.x(), mouse_point.y()

        u = (((x1 - x3) * (y2 - y3))/(x2-x3)) + y3

        intersection_x = round(x1,2)
        intersection_y = round(u,4)
        return QPointF(intersection_x, intersection_y)

if  __name__ == "__main__":        ##用于当前窗体测试
    app = QApplication(sys.argv)    #创建GUI应用程序
    form= QSubWidget()                #创建窗体
    form.show()
    sys.exit(app.exec_())