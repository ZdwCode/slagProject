import math
import re
import sys
from PyQt5.QtChart import QChart, QChartView, QValueAxis, QLineSeries
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtCore import pyqtSlot, Qt
from PyQt5.QtGui import QPixmap
from ui_MainWindow import Ui_Form
from subwin import QSubWidget, QSubDataWidget
from PyQt5 import QtChart, QtCore
import pandas as pd
import numpy as np
import joblib
from tensorflow.python.keras.models import load_model

# 7cd6cf
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


class QmyWidget(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)  # 调用父类构造函数，创建窗体
        self.ui = Ui_Form()  # 创建UI对象
        self.ui.setupUi(self)  # 构造UI
        # self.ui.label_24.setPixmap(QPixmap(r'.\logo2.jpg'))
        # self.ui.label_25.setPixmap(QPixmap(r'.\logo1.jpg'))
        self.df = pd.read_excel(r'.\炉渣性能编号和成分.xlsx', index_col=None)
        self.metl_model = joblib.load('./model/gradient_boosting_model_melt.joblib')
        self.visc_model = joblib.load('./model/gradient_boosting_model_visc.joblib')
        self.sulfur_model = load_model('./model/sulfur.h5')
        #self.metl_model = joblib.load('./model/gradient_boosting_model_melt.joblib')
        self.historyInfo = []
        self.historyInfo_show = []
        self.ui.label_20.connect_customized_slot(self.mylabel_clicked_20)
        self.ui.label_21.connect_customized_slot(self.mylabel_clicked_21)
        self.ui.label_22.connect_customized_slot(self.mylabel_clicked_22)
        self.divide = '***********************************************************************************************'

    ##  ========由connectSlotsByName() 自动关联的槽函数==========
    def mylabel_clicked_20(self):
        if self.ui.label_19.text() == 'None':
            return 0
        Al2O3 = self.ui.doubleSpinBox.text()
        MgO = self.ui.doubleSpinBox_3.text()
        jiandu = self.ui.doubleSpinBox_4.text()
        zhabi = self.ui.doubleSpinBox_5.text()
        s = self.ui.doubleSpinBox_6.text()
        s = float(s) * 0.078
        s = round(s, 4) # 保留四位小数
        t = self.ui.doubleSpinBox_7.text()
        paremeters = {"Al2O3": Al2O3, "MgO": MgO, "jiandu": jiandu, "zhabi": zhabi, "s": s, "t": t}
        formDoc = QSubWidget(self, paremeters, state=2, ui=self.ui)
        formDoc.setAttribute(Qt.WA_DeleteOnClose)
        formDoc.setWindowTitle("粘度")
        formDoc.setWindowFlag(Qt.Window, True)
        formDoc.setWindowOpacity(1)  # 窗口透明度
        formDoc.show()

    def mylabel_clicked_21(self):
        if self.ui.label_18.text() == 'None':
            return 0
        Al2O3 = self.ui.doubleSpinBox.text()
        MgO = self.ui.doubleSpinBox_3.text()
        jiandu = self.ui.doubleSpinBox_4.text()
        zhabi = self.ui.doubleSpinBox_5.text()
        s = self.ui.doubleSpinBox_6.text()
        s = float(s) * 0.078
        s = round(s, 4)
        t = self.ui.doubleSpinBox_7.text()
        paremeters = {"Al2O3": Al2O3, "MgO": MgO, "jiandu": jiandu, "zhabi": zhabi, "s": s, "t": t}
        formDoc = QSubWidget(self, paremeters, state=0, ui=self.ui)
        formDoc.setAttribute(Qt.WA_DeleteOnClose)
        formDoc.setWindowTitle("熔化性能")
        formDoc.setWindowFlag(Qt.Window, True)
        formDoc.setWindowOpacity(1)  # 窗口透明度
        formDoc.show()

    def mylabel_clicked_22(self):
        if self.ui.label_17.text() == 'None':
            return 0
        Al2O3 = self.ui.doubleSpinBox.text()
        MgO = self.ui.doubleSpinBox_3.text()
        jiandu = self.ui.doubleSpinBox_4.text()
        zhabi = self.ui.doubleSpinBox_5.text()
        s = self.ui.doubleSpinBox_6.text()
        s = float(s) * 0.078
        s = round(s, 4)
        t = self.ui.doubleSpinBox_7.text()
        paremeters = {"Al2O3": Al2O3, "MgO": MgO, "jiandu": jiandu, "zhabi": zhabi, "s": s, "t": t}
        formDoc = QSubWidget(self, paremeters, state=1, ui=self.ui)
        formDoc.setAttribute(Qt.WA_DeleteOnClose)
        formDoc.setWindowTitle("硫分配")
        formDoc.setWindowFlag(Qt.Window, True)
        formDoc.setWindowOpacity(1)  # 窗口透明度
        formDoc.show()

    def on_pushButton_clicked(self):
        Al2O3 = self.ui.doubleSpinBox.text()
        MgO = self.ui.doubleSpinBox_3.text()
        jiandu = self.ui.doubleSpinBox_4.text()
        zhabi = self.ui.doubleSpinBox_5.text()
        s = self.ui.doubleSpinBox_6.text()
        s = float(s) * 0.078
        s = round(s, 4)
        t = self.ui.doubleSpinBox_7.text()
        paremeters = {"Al2O3": Al2O3, "MgO": MgO, "jiandu": jiandu, "zhabi": zhabi, "s": s, "t": t}

        # self.getMeltingPerform(paremeters)
        # self.getSulfurDistribution(paremeters)
        # self.getNianDu(paremeters)

        formDoc = QSubWidget(self, paremeters, state=0, ui=self.ui)
        formDoc.setAttribute(Qt.WA_DeleteOnClose)
        formDoc.setWindowTitle("liquidus temperature")
        formDoc.setWindowFlag(Qt.Window, True)
        formDoc.setWindowOpacity(1)  # 窗口透明度
        formDoc.show()
        # #
        formDoc = QSubWidget(self, paremeters, state=1, ui=self.ui)
        formDoc.setAttribute(Qt.WA_DeleteOnClose)
        formDoc.setWindowTitle("硫分配")
        formDoc.setWindowFlag(Qt.Window, True)
        formDoc.setWindowOpacity(1)  # 窗口透明度
        formDoc.show()
        #
        formDoc = QSubWidget(self, paremeters, state=2, ui=self.ui)
        formDoc.setAttribute(Qt.WA_DeleteOnClose)
        formDoc.setWindowTitle("粘度")
        formDoc.setWindowFlag(Qt.Window, True)
        formDoc.setWindowOpacity(1)  # 窗口透明度
        formDoc.show()

    def on_pushButton2_clicked(self):
        historyInfomation = {}
        Al2O3 = self.ui.doubleSpinBox.text()
        MgO = self.ui.doubleSpinBox_3.text()
        jiandu = self.ui.doubleSpinBox_4.text()
        zhabi = self.ui.doubleSpinBox_5.text()
        s = self.ui.doubleSpinBox_6.text()
        CaO = self.ui.textEdit.toPlainText()
        SiO2 = self.ui.textEdit_2.toPlainText()
        coff = 1
        last_number_jiandu = int(list(jiandu)[-1])
        s = float(s) * 0.078
        s = round(s, 4)
        t = self.ui.doubleSpinBox_7.text()

        paremeters = {"Al2O3": Al2O3, "MgO": MgO, "jiandu": jiandu, "zhabi": zhabi, "s": s, "t": t, "coff": coff,"CaO":CaO,"SiO2":SiO2}
        historyInfomation['paremeters'] = paremeters
        MeltingPerform = self.getMeltingPerform(paremeters)
        SulfurDistribution = self.getSulfurDistribution(paremeters)
        NianDu = self.getNianDu(paremeters)
        historyInfomation['MeltingPerform'] = MeltingPerform
        historyInfomation['SulfurDistribution'] = SulfurDistribution
        historyInfomation['NianDu'] = NianDu
        self.historyInfo.append(historyInfomation)
        self.ui.textBrowser.setText('')
        for index, item in enumerate(self.historyInfo):
            text_0 = f'{index + 1}th inquiry'
            text_1 = 'Input：Al2O3=' + f'<font size = \"5\" color=\"green\"> {item["paremeters"]["Al2O3"]} </font>' + '  ' + 'MgO=' + f'<font size = \"5\" color=\"green\"> {item["paremeters"]["MgO"]} </font>' + ' ' + 'CaO=' + f'<font size = \"5\" color=\"green\"> {item["paremeters"]["CaO"]} </font>' \
                     + ' ' 'SiO2=' + f'<font size = \"5\" color=\"green\"> {item["paremeters"]["SiO2"]} </font>'+'  '+ 'Slag ratio=' + f'<font size = \"5\" color=\"green\"> {item["paremeters"]["zhabi"]} </font>' + ' ' + 'Sulfur partition ratio=' + f'<font size = \"5\" color=\"green\"> {str(round(float(item["paremeters"]["s"]) / 0.078, 2))} </font>' + ' ' \
                     + 'Temperature=' + f'<font size = \"5\" color=\"green\"> {item["paremeters"]["t"]} </font>' + '.'
            text_2 = 'Output：' + f'<font size = \"5\" color=\"green\"> {item["MeltingPerform"]} </font>' + "   " + f'<font size = \"5\" color=\"green\"> {item["SulfurDistribution"]} </font>' + '   ' + f'<font size = \"5\" color=\"green\"> {item["NianDu"]} </font>'
            # f'<font size = \"7\" color=\"green\"> {item["NianDu"]} </font>'
            self.ui.textBrowser.append(text_0)
            self.ui.textBrowser.append(text_1)
            self.ui.textBrowser.append(text_2)
            self.ui.textBrowser.append(self.divide)
        if len(self.historyInfo) > 1:
            item = self.historyInfo[-2]
            self.ui.label_34.setText(item["SulfurDistribution"].replace('↑', '').replace('↓', ''))
            self.ui.label_33.setText(item["MeltingPerform"].replace('↑', '').replace('↓', ''))
            self.ui.label_31.setText(item["NianDu"].replace('↑', '').replace('↓', ''))
            self.ui.label_43.setVisible(True)
            self.ui.label_44.setVisible(True)
            self.ui.label_45.setVisible(True)

    def on_doubleSpinBox_valueChanged(self):

        R = round(self.ui.doubleSpinBox_4.value(), 2)
        Al2O3 = round(self.ui.doubleSpinBox.value(), 2)
        MgO = round(self.ui.doubleSpinBox_3.value(), 2)
        SiO2 = round((97 - Al2O3 - MgO) / (1 + R), 2)
        CaO = round(R * SiO2, 2)
        print(R, Al2O3, MgO)
        self.ui.textEdit.setText(str(CaO))
        self.ui.textEdit_2.setText(str(SiO2))

    def getMeltingPerform(self, paremeters=None):
        df = self.df
        al2o3_input = float(paremeters['Al2O3'])
        mgo_input = float(paremeters['MgO'])
        jiandu_input = float(paremeters['jiandu'])
        vector = [[mgo_input,al2o3_input, jiandu_input]]
        result_predict = self.metl_model.predict(vector)
        result_start_Melt = result_predict[0][0]
        result_end_Melt = result_predict[0][1]
        print(result_predict,result_start_Melt,result_end_Melt)
        if len(self.historyInfo) == 0:
            text = 'T<sub>20%</sub>=' + str(round(result_start_Melt, 2)) + ';' + 'T<sub>80%</sub>=' + str(
                round(result_end_Melt, 2))
        else:
            item = self.historyInfo[-1]
            start_melt_last = re.findall('\d+\.?\d+', item['MeltingPerform'])[1]
            end_melt_last = re.findall('\d+\.?\d+', item['MeltingPerform'])[3]
            if float(start_melt_last) < float(result_start_Melt):
                change_start = '↑'
            elif float(start_melt_last) > float(result_start_Melt):
                change_start = '↓'
            else:
                change_start = '-'
            if float(end_melt_last) < float(result_end_Melt):
                change_end = '↑'
            elif float(end_melt_last) > float(result_end_Melt):
                change_end = '↓'
            else:
                change_end = '-'
            text = 'T<sub>20%</sub>=' + str(
                round(result_start_Melt, 2)) + change_start + ';' + 'T<sub>80%</sub>=' + str(
                round(result_end_Melt, 2)) + change_end
        self.ui.label_18.setText(text)
        return text

    def getSulfurDistribution(self, paremeters=None):
        al2o3_input = float(paremeters['Al2O3'])
        mgo_input = float(paremeters['MgO'])
        jiandu_input = float(paremeters['jiandu'])
        zhabi = float(paremeters['zhabi'])
        s = float(paremeters['s'])
        t = float(paremeters['t'])
        X = np.array([al2o3_input,jiandu_input, mgo_input,zhabi, s,t, ])
        X = X.reshape(1, -1)
        result_Sulfur_Fe = self.sulfur_model.predict(X)[0][0]
        print('0000')
        if len(self.historyInfo) == 0:
            text = '[s]=' + str(round(result_Sulfur_Fe,3))
        else:
            item = self.historyInfo[-1]
            result_Sulfur_Fe_last = re.findall('\d+\.?\d+', item['SulfurDistribution'])[0]
            if float(result_Sulfur_Fe_last) < round(result_Sulfur_Fe):
                change_Fe = '↑'
            elif float(result_Sulfur_Fe_last) > round(result_Sulfur_Fe):
                change_Fe = '↓'
            else:
                change_Fe = '-'
            text = '[s]=' + str(round(result_Sulfur_Fe, 3))+change_Fe
        self.ui.label_17.setText(text)
        print('1111')
        return text

    def getNianDu(self, paremeters=None):
        # print(paremeters)
        print('niandu')
        al2o3_input = float(paremeters['Al2O3'])
        mgo_input = float(paremeters['MgO'])
        jiandu_input = float(paremeters['jiandu'])
        Temperature = float(paremeters['t'])
        vector = [[al2o3_input, jiandu_input, mgo_input, Temperature]]
        print(vector)
        result_predict = self.visc_model.predict(vector)
        print(result_predict)
        result_niandu = result_predict[0]
        if len(self.historyInfo) == 0:
            text = 'Viscosity=' + str(round(result_niandu / 10, 4))
        else:
            print('1111')
            item = self.historyInfo[-1]
            result_Niandu_last = re.findall('\d+\.?\d+', item['NianDu'])[0]
            print(result_Niandu_last, result_niandu)
            if float(result_Niandu_last) < round(result_niandu / 10, 4):
                change_ninadu = '↑'
            elif float(result_Niandu_last) > round(result_niandu / 10, 4):
                change_ninadu = '↓'
            else:
                change_ninadu = '-'
            text = 'Viscosity=' + str(round(result_niandu / 10, 4)) + change_ninadu
        self.ui.label_19.setText(text)
        return text

    def on_pushButton3_clicked(self):
        formDoc = QSubDataWidget(self, ui=self.ui, historyInfo=self.historyInfo)
        formDoc.setAttribute(Qt.WA_DeleteOnClose)
        formDoc.setWindowFlag(Qt.Window, True)
        formDoc.setWindowOpacity(1)  # 窗口透明度
        formDoc.show()

    def on_pushButton4_clicked(self):
        self.historyInfo = []
        self.ui.textBrowser.setText('')
        self.ui.label_17.setText('')
        self.ui.label_18.setText('')
        self.ui.label_19.setText('')
        self.ui.label_31.setText('')
        self.ui.label_33.setText('')
        self.ui.label_34.setText('')


##  ============窗体测试程序 ================================
if __name__ == "__main__":  ##用于当前窗体测试
    QApplication.setHighDpiScaleFactorRoundingPolicy(Qt.HighDpiScaleFactorRoundingPolicy.PassThrough)
    app = QApplication(sys.argv)  # 创建GUI应用程序
    form = QmyWidget()
    form.show()
    sys.exit(app.exec_())
