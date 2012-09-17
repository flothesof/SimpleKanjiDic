# -*- coding: utf-8 -*-
"""
Created on Wed Jul 25 14:21:26 2012

@author: FL232714
"""

from PyQt4 import QtCore, QtGui, uic
from xmlparsing import data_structure, example_xml

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

    
if __name__ == '__main__':
    import sys
    Ui_MainWindow = uic.loadUiType("kanji_dictionary.ui")[0]
    
    class ConnectedUI(Ui_MainWindow, QtGui.QMainWindow):
        """User interface class deriving from ui file with additional slots"""
        def __init__(self, window):
            super(Ui_MainWindow, self).__init__()
            self.setupUi(window)
            self.setup_data()
            self.setup_slots()
            self.update_gui()
            
        def setup_slots(self):
            """Connect slots between ui and class functions"""
            QtCore.QObject.connect(self.pushButton,
                                   QtCore.SIGNAL(_fromUtf8("clicked()")),
                                    self.display_next)
            QtCore.QObject.connect(self.pushButton_2,
                                   QtCore.SIGNAL(_fromUtf8("clicked()")),
                                    self.display_previous)
            QtCore.QObject.connect(self.listView,
                                   QtCore.SIGNAL(_fromUtf8("clicked(QModelIndex)")),
                                    self.select_item_from_listview)
            
        def setup_data(self):
            """Loads dictionary data into ui class"""
            xml = example_xml()
            self.data = data_structure(xml)
            self.index = self.data.keys()
            self.current_ind = 0
            self.model = QtGui.QStandardItemModel()
            for item in self.index:
                qt_item = QtGui.QStandardItem(item)  
                self.model.appendRow(qt_item)
            self.listView.setModel(self.model)
            
        def display_next(self):
            """Displays next kanji in dictionary"""
            self.current_ind = (self.current_ind + 1) % len(self.index)
            self.update_gui()
        
        def display_previous(self):
            """Displays previous kanji in dictionary"""
            self.current_ind = (self.current_ind - 1) % len(self.index)
            self.update_gui()

        def display_message(self):
            """Displays a message to the user"""
            QtGui.QMessageBox.information(self, "Click!","SAFT completed")
        
        def select_item_from_listview(self, index):
            """Updates the GUI from a click in the listview"""
            item = self.model.data(index).toString()
            self.current_ind = self.index.index(unicode(item))
            self.update_gui()
        
        def update_gui(self):
            """Updates GUI fields with current entry"""
            current_key = self.index[self.current_ind]
            self.textBrowser.setText(self.data[current_key][0])
            self.textBrowser_2.clear()
            for item in self.data[current_key][1]:
                self.textBrowser_2.append(item)
            self.textBrowser_3.clear()
            for item in self.data[current_key][2]:
                self.textBrowser_3.append(item)
            self.textBrowser_4.clear()
            for item in self.data[current_key][3]:
                self.textBrowser_4.append(item)
            
    App = QtGui.QApplication(sys.argv)
    Window = QtGui.QMainWindow()

    Ui = ConnectedUI(Window)  
    
    Window.show()
    sys.exit(App.exec_())
