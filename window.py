# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Window.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.



from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        icon = QtGui.QIcon.fromTheme("icon.png")
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.Next_button = QtWidgets.QPushButton(self.centralwidget)
        self.Next_button.setObjectName("Next_button")
        self.gridLayout.addWidget(self.Next_button, 1, 2, 1, 2)
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName("stackedWidget")

        self.cpu = QtWidgets.QWidget()
        self.cpu.setObjectName("cpu")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.cpu)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.cpu_comboBox = QtWidgets.QComboBox(self.cpu)
        self.cpu_comboBox.setObjectName("cpu_comboBox")
        self.gridLayout_2.addWidget(self.cpu_comboBox, 1, 1, 1, 1)
        self.cpu_lable = QtWidgets.QLabel(self.cpu)
        self.cpu_lable.setStyleSheet("")
        self.cpu_lable.setObjectName("cpu_lable")
        self.gridLayout_2.addWidget(self.cpu_lable, 1, 0, 1, 1)
        self.cpu_table = QtWidgets.QTableWidget(self.cpu)
        self.cpu_table.setStyleSheet("")
        self.cpu_table.setObjectName("cpu_table")
        self.cpu_table.setColumnCount(0)
        self.cpu_table.setRowCount(0)
        self.gridLayout_2.addWidget(self.cpu_table, 0, 0, 1, 2)
        self.stackedWidget.addWidget(self.cpu)

        con = sqlite3.connect("computer")
        cur = con.cursor()
        query = "SELECT * " \
                "FROM cpu"
        cur.execute(query)
        cpus = cur.fetchall()
        self.cpu_id = cpus[0][0]
        self.cpu_table.setRowCount(len(cpus))
        self.cpu_table.setColumnCount(len(cpus[0]))
        self.cpu_table.setHorizontalHeaderLabels(
            ["id", "Название", "Сокет", "Тип памяти", "Энергопотребление", "Графическое ядро",
             "Максимальная температура", "Цена"])
        self.cpu_comboBox.clear()
        for i, cpu in enumerate(cpus):
            self.cpu_comboBox.addItem(str(cpu[0]))
            for j, param in enumerate(cpu):
                self.cpu_table.setItem(i, j, QtWidgets.QTableWidgetItem(str(param)))

        con.close()

        self.motherboard = QtWidgets.QWidget()
        self.motherboard.setObjectName("motherboard")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.motherboard)
        self.gridLayout_3.setObjectName("gridLayout_2")
        self.motherboard_comboBox = QtWidgets.QComboBox(self.motherboard)
        self.motherboard_comboBox.setObjectName("motherboard_comboBox")
        self.gridLayout_3.addWidget(self.motherboard_comboBox, 1, 1, 1, 1)
        self.motherboard_lable = QtWidgets.QLabel(self.motherboard)
        self.motherboard_lable.setStyleSheet("")
        self.motherboard_lable.setObjectName("motherboard_lable")
        self.gridLayout_3.addWidget(self.motherboard_lable, 1, 0, 1, 1)
        self.motherboard_table = QtWidgets.QTableWidget(self.motherboard)
        self.motherboard_table.setStyleSheet("")
        self.motherboard_table.setObjectName("motherboard_table")
        self.motherboard_table.setColumnCount(0)
        self.motherboard_table.setRowCount(0)
        self.gridLayout_3.addWidget(self.motherboard_table, 0, 0, 1, 2)
        self.stackedWidget.addWidget(self.motherboard)

        self.gpu = QtWidgets.QWidget()
        self.gpu.setObjectName("gpu")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.gpu)
        self.gridLayout_4.setObjectName("gridLayout_2")
        self.gpu_comboBox = QtWidgets.QComboBox(self.gpu)
        self.gpu_comboBox.setObjectName("gpu_comboBox")
        self.gridLayout_4.addWidget(self.gpu_comboBox, 1, 1, 1, 1)
        self.gpu_lable = QtWidgets.QLabel(self.gpu)
        self.gpu_lable.setStyleSheet("")
        self.gpu_lable.setObjectName("gpu_lable")
        self.gridLayout_4.addWidget(self.gpu_lable, 1, 0, 1, 1)
        self.gpu_table = QtWidgets.QTableWidget(self.gpu)
        self.gpu_table.setStyleSheet("")
        self.gpu_table.setObjectName("gpu_table")
        self.gpu_table.setColumnCount(0)
        self.gpu_table.setRowCount(0)
        self.gridLayout_4.addWidget(self.gpu_table, 0, 0, 1, 2)
        self.stackedWidget.addWidget(self.gpu)

        self.cooler = QtWidgets.QWidget()
        self.cooler.setObjectName("cooler")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.cooler)
        self.gridLayout_5.setObjectName("gridLayout_2")
        self.cooler_comboBox = QtWidgets.QComboBox(self.cooler)
        self.cooler_comboBox.setObjectName("cooler_comboBox")
        self.gridLayout_5.addWidget(self.cooler_comboBox, 1, 1, 1, 1)
        self.cooler_lable = QtWidgets.QLabel(self.cooler)
        self.cooler_lable.setStyleSheet("")
        self.cooler_lable.setObjectName("cooler_lable")
        self.gridLayout_5.addWidget(self.cooler_lable, 1, 0, 1, 1)
        self.cooler_table = QtWidgets.QTableWidget(self.cooler)
        self.cooler_table.setStyleSheet("")
        self.cooler_table.setObjectName("cooler_table")
        self.cooler_table.setColumnCount(0)
        self.cooler_table.setRowCount(0)
        self.gridLayout_5.addWidget(self.cooler_table, 0, 0, 1, 2)
        self.stackedWidget.addWidget(self.cooler)

        self.ram = QtWidgets.QWidget()
        self.ram.setObjectName("ram")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.ram)
        self.gridLayout_6.setObjectName("gridLayout_2")
        self.ram_comboBox = QtWidgets.QComboBox(self.ram)
        self.ram_comboBox.setObjectName("ram_comboBox")
        self.gridLayout_6.addWidget(self.ram_comboBox, 1, 1, 1, 1)
        self.ram_lable = QtWidgets.QLabel(self.ram)
        self.ram_lable.setStyleSheet("")
        self.ram_lable.setObjectName("ram_lable")
        self.gridLayout_6.addWidget(self.ram_lable, 1, 0, 1, 1)
        self.ram_table = QtWidgets.QTableWidget(self.ram)
        self.ram_table.setStyleSheet("")
        self.ram_table.setObjectName("ram_table")
        self.ram_table.setColumnCount(0)
        self.ram_table.setRowCount(0)
        self.gridLayout_6.addWidget(self.ram_table, 0, 0, 1, 2)
        self.stackedWidget.addWidget(self.ram)

        self.hdd = QtWidgets.QWidget()
        self.hdd.setObjectName("hdd")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.hdd)
        self.gridLayout_7.setObjectName("gridLayout_2")
        self.hdd_comboBox = QtWidgets.QComboBox(self.hdd)
        self.hdd_comboBox.setObjectName("hdd_comboBox")
        self.gridLayout_7.addWidget(self.hdd_comboBox, 1, 1, 1, 1)
        self.hdd_lable = QtWidgets.QLabel(self.hdd)
        self.hdd_lable.setStyleSheet("")
        self.hdd_lable.setObjectName("hdd_lable")
        self.gridLayout_7.addWidget(self.hdd_lable, 1, 0, 1, 1)
        self.hdd_table = QtWidgets.QTableWidget(self.hdd)
        self.hdd_table.setStyleSheet("")
        self.hdd_table.setObjectName("hdd_table")
        self.hdd_table.setColumnCount(0)
        self.hdd_table.setRowCount(0)
        self.gridLayout_7.addWidget(self.hdd_table, 0, 0, 1, 2)
        self.stackedWidget.addWidget(self.hdd)

        self.ssd = QtWidgets.QWidget()
        self.ssd.setObjectName("ssd")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.ssd)
        self.gridLayout_8.setObjectName("gridLayout_2")
        self.ssd_comboBox = QtWidgets.QComboBox(self.ssd)
        self.ssd_comboBox.setObjectName("ssd_comboBox")
        self.gridLayout_8.addWidget(self.ssd_comboBox, 1, 1, 1, 1)
        self.ssd_lable = QtWidgets.QLabel(self.ssd)
        self.ssd_lable.setStyleSheet("")
        self.ssd_lable.setObjectName("ssd_lable")
        self.gridLayout_8.addWidget(self.ssd_lable, 1, 0, 1, 1)
        self.ssd_table = QtWidgets.QTableWidget(self.ssd)
        self.ssd_table.setStyleSheet("")
        self.ssd_table.setObjectName("ssd_table")
        self.ssd_table.setColumnCount(0)
        self.ssd_table.setRowCount(0)
        self.gridLayout_8.addWidget(self.ssd_table, 0, 0, 1, 2)
        self.stackedWidget.addWidget(self.ssd)

        self.power_unit = QtWidgets.QWidget()
        self.power_unit.setObjectName("power_unit")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.power_unit)
        self.gridLayout_9.setObjectName("gridLayout_2")
        self.power_unit_comboBox = QtWidgets.QComboBox(self.power_unit)
        self.power_unit_comboBox.setObjectName("power_unit_comboBox")
        self.gridLayout_9.addWidget(self.power_unit_comboBox, 1, 1, 1, 1)
        self.power_unit_lable = QtWidgets.QLabel(self.power_unit)
        self.power_unit_lable.setStyleSheet("")
        self.power_unit_lable.setObjectName("power_unit_lable")
        self.gridLayout_9.addWidget(self.power_unit_lable, 1, 0, 1, 1)
        self.power_unit_table = QtWidgets.QTableWidget(self.power_unit)
        self.power_unit_table.setStyleSheet("")
        self.power_unit_table.setObjectName("power_unit_table")
        self.power_unit_table.setColumnCount(0)
        self.power_unit_table.setRowCount(0)
        self.gridLayout_9.addWidget(self.power_unit_table, 0, 0, 1, 2)
        self.stackedWidget.addWidget(self.power_unit)

        self.body = QtWidgets.QWidget()
        self.body.setObjectName("body")
        self.gridLayout_10 = QtWidgets.QGridLayout(self.body)
        self.gridLayout_10.setObjectName("gridLayout_2")
        self.body_comboBox = QtWidgets.QComboBox(self.body)
        self.body_comboBox.setObjectName("body_comboBox")
        self.gridLayout_10.addWidget(self.body_comboBox, 1, 1, 1, 1)
        self.body_lable = QtWidgets.QLabel(self.body)
        self.body_lable.setStyleSheet("")
        self.body_lable.setObjectName("body_lable")
        self.gridLayout_10.addWidget(self.body_lable, 1, 0, 1, 1)
        self.body_table = QtWidgets.QTableWidget(self.body)
        self.body_table.setStyleSheet("")
        self.body_table.setObjectName("body_table")
        self.body_table.setColumnCount(0)
        self.body_table.setRowCount(0)
        self.gridLayout_10.addWidget(self.body_table, 0, 0, 1, 2)
        self.stackedWidget.addWidget(self.body)

        self.gridLayout.addWidget(self.stackedWidget, 0, 0, 1, 4)
        self.Back_button = QtWidgets.QPushButton(self.centralwidget)
        self.Back_button.setObjectName("Back_button")
        self.gridLayout.addWidget(self.Back_button, 1, 0, 1, 2)
        MainWindow.setCentralWidget(self.centralwidget)

        self.Back_button.clicked.connect(self.back_page)
        self.Next_button.clicked.connect(self.next_page)
        self.cpu_comboBox.currentTextChanged.connect(self.choose_cpu)
        self.motherboard_comboBox.currentTextChanged.connect(self.choose_motherboard)
        self.gpu_comboBox.currentTextChanged.connect(self.choose_gpu)


        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        self.stackedWidget.currentChanged.connect(self.load_page)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.motherboard_id = None

    def choose_cpu(self, cpu_id):
        self.cpu_id = cpu_id

    def choose_motherboard(self, motherboard_id):
        if motherboard_id is int:
            motherboard_id = int(motherboard_id)
            self.motherboard_id = motherboard_id

    def choose_gpu(self, gpu_id):
        self.gpu_id = gpu_id

    # чтобы перелистовать страницы
    def next_page(self):
        self.stackedWidget.setCurrentIndex(self.stackedWidget.currentIndex() + 1)

    def back_page(self):
        self.stackedWidget.setCurrentIndex(self.stackedWidget.currentIndex() - 1)

    # чтобы загрузить базу данных
    def load_page(self, id):
        #ПРОЦЕССОР
        if id == 0:
            con = sqlite3.connect("computer")
            cur = con.cursor()
            query = "SELECT * " \
                    "FROM cpu"
            cur.execute(query)
            cpus = cur.fetchall()
            self.cpu_id = cpus[0][0]
            self.cpu_table.setRowCount(len(cpus))
            self.cpu_table.setColumnCount(len(cpus[0]))
            self.cpu_table.setHorizontalHeaderLabels(
                ["id", "Название", "Сокет", "Тип памяти", "Энергопотребление", "Графическое ядро",
                 "Максимальная температура", "Цена"])
            self.cpu_comboBox.clear()
            for i, cpu in enumerate(cpus):
                self.cpu_comboBox.addItem(str(cpu[0]))
                for j, param in enumerate(cpu):
                    self.cpu_table.setItem(i, j, QtWidgets.QTableWidgetItem(str(param)))

            con.close()

        #МАТЕРИНСКАЯ ПЛАТА
        elif id == 1:
            con = sqlite3.connect("computer")
            cur = con.cursor()
            query = "SELECT Socket " \
                    "FROM cpu " \
                    "WHERE id = ?"
            cur.execute(query, (self.cpu_id,))
            socket_ = cur.fetchone()[0]

            query = "SELECT *" \
                    "FROM mother_plate " \
                    "WHERE Socket=?"
            cur.execute(query, (socket_,))
            motherboards = cur.fetchall()
            self.motherboard_id = motherboards[0][0]
            self.motherboard_table.setRowCount(len(motherboards))
            self.motherboard_table.setColumnCount(len(motherboards[0]))
            self.motherboard_table.setHorizontalHeaderLabels(
                ["id", "Название", "Сокет", "Размер", "Тип памяти", "Количество слотов памяти",
                 "Разъём памяти процессора", "PCI-Express", "Цена"])
            self.motherboard_comboBox.clear()
            for i, motherboard in enumerate(motherboards):
                self.motherboard_comboBox.addItem(str(motherboard[0]))
                for j, param in enumerate(motherboard):
                    self.motherboard_table.setItem(i, j, QtWidgets.QTableWidgetItem(str(param)))

            con.close()

        #ВИДЕОКАРТА
        elif id == 2:
            con = sqlite3.connect("computer")
            cur = con.cursor()
            # выбор pci из таблицы mother_plate, где id = motherboard_id
            query = "SELECT PCI_Express " \
                    "FROM mother_plate " \
                    "WHERE id = ?"
            cur.execute(query, (self.motherboard_id,))
            pci_express_ = cur.fetchone()[0]

            query = "SELECT *" \
                    "FROM video_card " \
                    "WHERE PCI_Express=?"
            cur.execute(query, (pci_express_,))
            gpus = cur.fetchall()
            self.gpu_id = gpus[0][0]
            self.gpu_table.setRowCount(len(gpus)) # устанавливает количество строк в таблице с платами
            self.gpu_table.setColumnCount(len(gpus[0])) # устанавливает количество столбцов в таблице равным количеству параметров
            self.gpu_table.setHorizontalHeaderLabels(
                ["id", "Название", "Рекомендованный источник питания", "Размер", "PCI-Express", "Цена",])
            self.gpu_comboBox.clear()  # очищает comboBox перед добавлением новых элементов
            for i, gpu in enumerate(gpus):
                self.gpu_comboBox.addItem(str(gpu[0])) # добавляет элементы в gpu_comboBox
                for j, param in enumerate(gpu):
                    self.gpu_table.setItem(i, j, QtWidgets.QTableWidgetItem(str(param)))

            con.close()

        #КУЛЕР
        elif id == 3:
            con = sqlite3.connect("computer")
            cur = con.cursor()
            query = "SELECT Energy_consumption " \
                    "FROM cpu " \
                    "WHERE id = ?"
            cur.execute(query, (self.cpu_id,))
            temperature_ = cur.fetchone()[0]

            query = "SELECT *" \
                    "FROM cooler " \
                    "WHERE dissipated_power >= ?"
            cur.execute(query, (temperature_ * 2,))  # умножаем макс.температуру процессора на 2
            coolers = cur.fetchall()
            self.cooler_table.setRowCount(len(coolers))
            self.cooler_table.setColumnCount(len(coolers[0]))
            self.cooler_table.setHorizontalHeaderLabels(
                ["id", "Название", "Сокет", "Рассеиваемая мощность", "Высота", "Цена",])
            self.cooler_comboBox.clear()
            for i, cooler in enumerate(coolers):
                self.cooler_comboBox.addItem(str(cooler[0]))
                for j, param in enumerate(cooler):
                    self.cooler_table.setItem(i, j, QtWidgets.QTableWidgetItem(str(param)))

            con.close()
        
        #ОПЕРАТИВНАЯ ПАМЯТЬ
        elif id == 4:
            con = sqlite3.connect("computer")
            cur = con.cursor()
            # даю query разные названия
            query_type = "SELECT type_of_memory " \
                         "FROM mother_plate " \
                         "WHERE id = ?"
            cur.execute(query_type, (self.motherboard_id,))
            type_memory_ = cur.fetchone()[0]

            query_slots = "SELECT  number_of_memory_slots " \
                          "FROM mother_plate " \
                          "WHERE id = ?"
            cur.execute(query_slots, (self.motherboard_id,))
            number_slots_ = cur.fetchone()[0]

            query_ram = "SELECT * " \
                         "FROM ram " \
                         "WHERE type_of_memory = ? AND number_of_memory_modules <= ?"
            cur.execute(query_ram, (type_memory_, number_slots_))
            rams = cur.fetchall()
            self.ram_table.setRowCount(len(rams))
            self.ram_table.setColumnCount(len(rams[0]))
            self.ram_table.setHorizontalHeaderLabels(
                    ["id", "Название", "Тип памяти", "Тип модуля памяти", "Количество модулей в комплекте", "Объём памяти", "Цена",])
            self.ram_comboBox.clear()
            for i, ram in enumerate(rams):
                self.ram_comboBox.addItem(str(ram[0]))
                for j, param in enumerate(ram):
                    self.ram_table.setItem(i, j, QtWidgets.QTableWidgetItem(str(param)))

            con.close()

        #ЖЁСТКИЙ ДИСК
        elif id == 5    :
            con = sqlite3.connect("computer")
            cur = con.cursor()
            query = "SELECT Energy_consumption " \
                    "FROM cpu " \
                    "WHERE id = ?"
            cur.execute(query, (self.cpu_id,))
            energy_ = cur.fetchone()[0]

            query = "SELECT *" \
                    "FROM hdd " \
                    "WHERE Energy_consumption < ?"
            cur.execute(query, (energy_,))
            hdds = cur.fetchall()
            self.hdd_table.setRowCount(len(hdds))
            self.hdd_table.setColumnCount(len(hdds[0]))
            self.hdd_table.setHorizontalHeaderLabels(
                    ["id", "Название", "Тип памяти", "Тип модуля памяти", "Количество модулей в комплекте", "Объём памяти", "Цена",])
            self.hdd_comboBox.clear()
            for i, hdd in enumerate(hdds):
                self.hdd_comboBox.addItem(str(hdd[0]))
                for j, param in enumerate(hdd):
                    self.hdd_table.setItem(i, j, QtWidgets.QTableWidgetItem(str(param)))

            con.close()

        #SSD
        elif id == 6:
            con = sqlite3.connect("computer")
            cur = con.cursor()
            query = "SELECT Energy_consumption " \
                    "FROM cpu " \
                    "WHERE id = ?"
            cur.execute(query, (self.cpu_id,))
            energy_ = cur.fetchone()[0]

            query = "SELECT *" \
                    "FROM SSD_m2 " \
                    "WHERE Energy_consumption < ?"
            cur.execute(query, (energy_,))
            ssds = cur.fetchall()
            self.ssd_table.setRowCount(len(ssds))
            self.ssd_table.setColumnCount(len(ssds[0]))
            self.ssd_table.setHorizontalHeaderLabels(
                ["id", "Название", "Тип памяти", "Тип модуля памяти", "Количество модулей в комплекте", "Объём памяти",
                 "Цена", ])
            self.ssd_comboBox.clear()
            for i, ssd in enumerate(ssds):
                self.ssd_comboBox.addItem(str(ssd[0]))
                for j, param in enumerate(ssd):
                    self.ssd_table.setItem(i, j, QtWidgets.QTableWidgetItem(str(param)))

            con.close()

        #БЛОК ПИТАНИЯ
        elif id == 7:
            con = sqlite3.connect("computer")
            cur = con.cursor()
            query = "SELECT Recommended_power_supply " \
                    "FROM video_card " \
                    "WHERE id = ?"
            cur.execute(query, (self.gpu_id,))
            recommend_power_ = cur.fetchone()[0]

            query = "SELECT *" \
                    "FROM power_unit " \
                    "WHERE power > ?"
            cur.execute(query, (recommend_power_,))
            power_units = cur.fetchall()
            self.power_unit_table.setRowCount(len(power_units))
            self.power_unit_table.setColumnCount(len(power_units[0]))
            self.power_unit_table.setHorizontalHeaderLabels(
                ["id", "Название", "Тип памяти", "Тип модуля памяти", "Количество модулей в комплекте", "Объём памяти",
                 "Цена", ])
            self.power_unit_comboBox.clear()
            for i, power_unit in enumerate(power_units):
                self.power_unit_comboBox.addItem(str(power_unit[0]))
                for j, param in enumerate(power_unit):
                    self.power_unit_table.setItem(i, j, QtWidgets.QTableWidgetItem(str(param)))

            con.close()

        #КОРПУС
        '''elif id == 8:'''



    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Конфигуратор ПК"))
        self.Next_button.setText(_translate("MainWindow", "Вперёд"))
        self.cpu_lable.setText(_translate("MainWindow", "Выберите ID процессора"))
        self.Back_button.setText(_translate("MainWindow", "Назад"))
        self.motherboard_lable.setText(_translate("MainWindow", "Выберите ID материнской платы"))
        self.gpu_lable.setText(_translate("MainWindow", "Выберите ID видеокарты"))
        self.cooler_lable.setText(_translate("MainWindow", "Выберите ID охлаждения"))
        self.ram_lable.setText(_translate("MainWindow", "Выберите ID оперативной памяти"))
        self.hdd_lable.setText(_translate("MainWindow", "Выберите ID жёсткого диска"))
        self.ssd_lable.setText(_translate("MainWindow", "Выберите ID SSD"))
        self.power_unit_lable.setText(_translate("MainWindow", "Выберите ID блока питания"))
        self.body_lable.setText(_translate("MainWindow", "Выберите ID корпуса"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
