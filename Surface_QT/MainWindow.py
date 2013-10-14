# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qt/MainWindow.ui'
#
# Created: Mon Oct 14 16:37:47 2013
#      by: PyQt4 UI code generator 4.8.6
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(800, 600)
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "OpenGL", None, QtGui.QApplication.UnicodeUTF8))
        MainWindow.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.groupBox = QtGui.QGroupBox(self.centralwidget)
        self.groupBox.setTitle(QtGui.QApplication.translate("MainWindow", "Model", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.verticalLayout = QtGui.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.wireframe_check = QtGui.QCheckBox(self.groupBox)
        self.wireframe_check.setText(QtGui.QApplication.translate("MainWindow", "Wireframe", None, QtGui.QApplication.UnicodeUTF8))
        self.wireframe_check.setObjectName(_fromUtf8("wireframe_check"))
        self.verticalLayout.addWidget(self.wireframe_check)
        self.gridLayout.addWidget(self.groupBox, 1, 2, 1, 1)
        self.controls_group = QtGui.QGroupBox(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.controls_group.sizePolicy().hasHeightForWidth())
        self.controls_group.setSizePolicy(sizePolicy)
        self.controls_group.setTitle(QtGui.QApplication.translate("MainWindow", "Camera", None, QtGui.QApplication.UnicodeUTF8))
        self.controls_group.setObjectName(_fromUtf8("controls_group"))
        self.formLayout = QtGui.QFormLayout(self.controls_group)
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.ExpandingFieldsGrow)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.zoom_label = QtGui.QLabel(self.controls_group)
        self.zoom_label.setText(QtGui.QApplication.translate("MainWindow", "Zoom", None, QtGui.QApplication.UnicodeUTF8))
        self.zoom_label.setObjectName(_fromUtf8("zoom_label"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.zoom_label)
        self.zoom_slider = QtGui.QSlider(self.controls_group)
        self.zoom_slider.setMinimum(-100)
        self.zoom_slider.setMaximum(100)
        self.zoom_slider.setOrientation(QtCore.Qt.Horizontal)
        self.zoom_slider.setTickPosition(QtGui.QSlider.TicksBelow)
        self.zoom_slider.setTickInterval(25)
        self.zoom_slider.setObjectName(_fromUtf8("zoom_slider"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.zoom_slider)
        self.azimuth_label = QtGui.QLabel(self.controls_group)
        self.azimuth_label.setText(QtGui.QApplication.translate("MainWindow", "Azimuth", None, QtGui.QApplication.UnicodeUTF8))
        self.azimuth_label.setObjectName(_fromUtf8("azimuth_label"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.LabelRole, self.azimuth_label)
        self.azimuth_slider = QtGui.QSlider(self.controls_group)
        self.azimuth_slider.setMaximum(360)
        self.azimuth_slider.setOrientation(QtCore.Qt.Horizontal)
        self.azimuth_slider.setTickPosition(QtGui.QSlider.TicksBelow)
        self.azimuth_slider.setTickInterval(90)
        self.azimuth_slider.setObjectName(_fromUtf8("azimuth_slider"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.FieldRole, self.azimuth_slider)
        self.elevation_label = QtGui.QLabel(self.controls_group)
        self.elevation_label.setText(QtGui.QApplication.translate("MainWindow", "Elevation", None, QtGui.QApplication.UnicodeUTF8))
        self.elevation_label.setObjectName(_fromUtf8("elevation_label"))
        self.formLayout.setWidget(4, QtGui.QFormLayout.LabelRole, self.elevation_label)
        self.elevation_slider = QtGui.QSlider(self.controls_group)
        self.elevation_slider.setMaximum(90)
        self.elevation_slider.setOrientation(QtCore.Qt.Horizontal)
        self.elevation_slider.setTickPosition(QtGui.QSlider.TicksBelow)
        self.elevation_slider.setTickInterval(90)
        self.elevation_slider.setObjectName(_fromUtf8("elevation_slider"))
        self.formLayout.setWidget(4, QtGui.QFormLayout.FieldRole, self.elevation_slider)
        self.gridLayout.addWidget(self.controls_group, 0, 2, 1, 1)
        self.main_layout = QtGui.QVBoxLayout()
        self.main_layout.setSizeConstraint(QtGui.QLayout.SetDefaultConstraint)
        self.main_layout.setObjectName(_fromUtf8("main_layout"))
        self.gridLayout.addLayout(self.main_layout, 0, 1, 3, 1)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 2, 2, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 20))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setTitle(QtGui.QApplication.translate("MainWindow", "File", None, QtGui.QApplication.UnicodeUTF8))
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionSalir = QtGui.QAction(MainWindow)
        self.actionSalir.setText(QtGui.QApplication.translate("MainWindow", "Salir", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSalir.setObjectName(_fromUtf8("actionSalir"))
        self.menuFile.addAction(self.actionSalir)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.actionSalir, QtCore.SIGNAL(_fromUtf8("triggered()")), MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        pass

