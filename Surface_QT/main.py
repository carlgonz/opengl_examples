import sys
from PyQt4 import QtGui
from PyQt4 import QtCore
from traits.trait_types import self

from MainWindow import Ui_MainWindow
from GLWidget import GLWidget


class App(QtGui.QMainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.gl_widget = GLWidget(self)
        self.ui.main_layout.addWidget(self.gl_widget)

        self.ui.zoom_slider.valueChanged.connect(self.gl_widget.zoom)
        self.ui.elevation_slider.valueChanged.connect(self.gl_widget.elevation)
        self.ui.azimuth_slider.valueChanged.connect(self.gl_widget.azimuth)
        self.ui.wireframe_check.toggled.connect(self.gl_widget.wire)

app = QtGui.QApplication(sys.argv)
gui = App()
gui.show()
sys.exit(app.exec_())
