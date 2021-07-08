import FreeCADGui
from PySide import QtGui
from pyOpToolsWB.qthelpers import getUIFilePath
import pyoptools.raytrace.mat_lib as matlib


class materialWidget(QtGui.QWidget):
    def __init__(self):
        super(materialWidget, self).__init__()
        self.initUI()

    def initUI(self):
        fn1 = getUIFilePath("materialWidget.ui")
        self.ui = FreeCADGui.PySideUic.loadUi(fn1, self)
        self.setLayout(self.ui.mainLayout)

        self.ui.Catalog.addItem("Value", [])

        for i in matlib.material.liblist:
            self.ui.Catalog.addItem(i[0], sorted(i[1].keys()))

        self.ui.Catalog.currentIndexChanged.connect(self.catalogChange)

    def catalogChange(self, *args):
        if args[0] == 0:
            self.ui.Value.setEnabled(True)
        else:
            self.ui.Value.setEnabled(False)

        while self.ui.Reference.count():
            self.ui.Reference.removeItem(0)
        self.ui.Reference.addItems(self.ui.Catalog.itemData(args[0]))

    # properties defined to make the new code compatible with the old
    @property
    def Catalog(self):
        return self.ui.Catalog

    @property
    def Value(self):
        return self.ui.Value

    @property
    def Reference(self):
        return self.ui.Reference
