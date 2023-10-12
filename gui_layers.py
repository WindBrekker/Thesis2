import sys
import os
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path
from os.path import exists as file_exists
from PyQt6.QtGui import QPalette, QColor, QIcon, QAction, QPixmap
from pathlib import Path
from PyQt6.QtWidgets import (
    QApplication,
    QLineEdit,
    QLabel,
    QFileDialog,
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QPushButton,
    QHBoxLayout,
    QComboBox,
)




class Color(QWidget):

    def __init__(self, color):
        super(Color, self).__init__()
        self.setAutoFillBackground(True)

        palette = self.palette()
        palette.setColor(QPalette.ColorRole.Window, QColor(color))
        self.setPalette(palette)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()


        self.setWindowTitle("QuantumSlice")
        self.setGeometry(0,0,1200,700)

    #main layout
        pagelayout = QVBoxLayout()
    #sub layouts
        Upper_layout = QHBoxLayout()
        # Upper_layout.addWidget(Color("orange"))
        Lower_layout = QHBoxLayout()
        # Lower_layout.addWidget(Color("blue"))

    #sub upper_layouts
        Results_layout = QHBoxLayout()
        # Results_layout.addWidget(Color("purple"))
    #sub lower_layout
        Left_layout = QVBoxLayout()
        # Left_layout.addWidget(Color("orange"))
        Data_layout = QVBoxLayout()
        # Data_layout.addWidget(Color("red"))
    #data_layout
        Input_layout = QVBoxLayout()
        #Input_layout.addWidget(Color("blue"))
        Names_layout = QVBoxLayout()
        Names_layout.addWidget(Color("transparent"))
        Saving_layout = QVBoxLayout()
        Saving_layout.addWidget(Color("transparent"))
    #sub saving_layout
        saving_button_layout = QHBoxLayout()
    #sub Left_layout
        Sample_layout = QVBoxLayout()
        # Sample_layout.addWidget(Color("pink"))
        Panel_layout = QHBoxLayout()
        # Panel_layout.addWidget(Color("orange"))

        #Adding layouts
        pagelayout.addLayout(Upper_layout,1)
        pagelayout.addLayout(Lower_layout,9)

        Upper_layout.addLayout(Results_layout)

        Lower_layout.addLayout(Left_layout,6)
        Lower_layout.addWidget(Color("transparent"),1)
        Lower_layout.addLayout(Data_layout,3)

        Left_layout.addLayout(Panel_layout,2)
        Left_layout.addLayout(Sample_layout,8)

        Data_layout.addLayout(Input_layout,1)
        Data_layout.addLayout(Names_layout,3)
        Data_layout.addLayout(Saving_layout,5)
        Data_layout.addLayout(saving_button_layout,1)

        #Widgets
        #QLabel
        self.Ci_label = QLabel(self)
        self.Ci_label.setText("Save the Ci map:")
        self.SM_label = QLabel(self)
        self.SM_label.setText("Save the SM map:")
        self.Livetime_label = QLabel(self)
        self.Livetime_label.setText("Save the livetime map:")
        self.Lambda_label = QLabel(self)
        self.Lambda_label.setText("Save the lambda map:")
        self.sample_picture_label = QLabel(self)
        self.sample_picture_label.setText("Sample_photo")
        self.element_name_label = QLabel(self)
        self.element_name_label.setText("element of suprise")
        self.Cursor_data_label = QLabel("Cursor data",self)
        self.X_label = QLabel("X:",self)
        self.X_value_label = QLabel("",self)
        self.Y_label = QLabel("Y:",self)
        self.Y_value_label = QLabel("",self)
        self.Value_label = QLabel("Value:",self)
        self.Value_value_label = QLabel("",self)
        self.Mean_label = QLabel("Mean:",self)
        self.Mean_value_label = QLabel("",self)
        self.Median_label = QLabel("Median:",self)
        self.Median_value_label = QLabel("",self)
        self.Min_label = QLabel("Min:",self)
        self.Min_value_label = QLabel("",self)
        self.Max_label = QLabel("Max:",self)
        self.Max_value_label = QLabel("",self)
        self.Mask_label = QLabel("Mask:",self)
        self.Mask_value_label = QLabel("K",self)
        self.input_info_label = QLabel("Enter the appropriate values",self)
        self.names_inof_label = QLabel("Enter used nomenclature",self)



        # #QLineEdit
        self.Main_folder = QLineEdit(self)
        self.Main_folder.setPlaceholderText("Main folder path")

        self.Pixel = QLineEdit(self)
        self.Pixel.setPlaceholderText("Pixel size")

        self.Inputfile = QLineEdit(self)
        self.Inputfile.setPlaceholderText("Inputfile")

        self.Zeropeak = QLineEdit(self)
        self.Zeropeak.setPlaceholderText("Zeropeak")

        self.Scater = QLineEdit(self)
        self.Scater.setPlaceholderText("Scater")

        self.SampMatrix = QLineEdit(self)
        self.SampMatrix.setPlaceholderText("Sample Matrix")

        # #QComboBox
        self.Ci_combobox = QComboBox(self)
        self.Ci_combobox.addItems(["Don't save", ".png", ".bmp", ".tiff", ".dat"])
        self.SM_combobox = QComboBox(self)
        self.SM_combobox.addItems(["Don't save", ".png", ".bmp", ".tiff", ".dat"])
        self.Lambda_combobox = QComboBox(self)
        self.Lambda_combobox.addItems(["Don't save",".dat"])
        self.Livetime_combobox = QComboBox(self)
        self.Livetime_combobox.addItems([ "Don't save",".dat"])
        self.Prefere_folder = QComboBox(self)
        self.Prefere_folder.activated.connect(self.prefered_folder_selected)
        self.Prefere_folder.setEnabled(False)
        self.Prefere_folder.setPlaceholderText("Confirm identifiers first")

        # #QPixmap
        self.sample_pixmap = QPixmap('photo.png')


        # #QPushButton
        self.previous_element_button = QPushButton("<", self)
        self.previous_element_button.setEnabled(False)
        self.previous_element_button.clicked.connect(self.Previous_element)
        self.next_element_button = QPushButton(">", self)
        self.next_element_button.setEnabled(False)
        self.next_element_button.clicked.connect(self.Next_element)
        self.use_for_mask_button = QPushButton("Use for mask", self)
        self.use_for_mask_button.setEnabled(False)
        self.use_for_mask_button.clicked.connect(self.ChooseMask)
        self.quantify_button = QPushButton("Quantify", self)
        self.quantify_button.setEnabled(False)
        self.quantify_button.clicked.connect(self.Quantify)

        self.confirm_names_button = QPushButton("Confirm",self)
        self.confirm_names_button.clicked.connect(self.Confirmed_names)
        self.confirm_saving_button = QPushButton("Confirm",self)
        self.confirm_saving_button.clicked.connect(self.Confirmed_saving)
        
        self.saving_button = QPushButton("Save",self)
        self.saving_button.setEnabled(False)
        self.saving_button.clicked.connect(self.Saving)


        # #Adding widgets
        Input_layout.addWidget(self.input_info_label)
        Input_layout.addWidget(self.Main_folder)
        Input_layout.addWidget(self.Pixel)

        Names_layout.addWidget(self.names_inof_label)
        Names_layout.addWidget(self.Inputfile)
        Names_layout.addWidget(self.Zeropeak)
        Names_layout.addWidget(self.Scater)
        Names_layout.addWidget(self.SampMatrix)
        Names_layout.addWidget(self.confirm_names_button)
        Names_layout.addWidget(self.Prefere_folder)
        
        
        Saving_layout.addWidget(self.Ci_label)
        Saving_layout.addWidget(self.Ci_combobox)
        Saving_layout.addWidget(self.SM_label)
        Saving_layout.addWidget(self.SM_combobox)
        Saving_layout.addWidget(self.Lambda_label)
        Saving_layout.addWidget(self.Lambda_combobox)
        Saving_layout.addWidget(self.Livetime_label)
        Saving_layout.addWidget(self.Livetime_combobox)
        saving_button_layout.addWidget(self.confirm_saving_button)
        saving_button_layout.addWidget(self.saving_button)


        Sample_layout.addWidget(self.sample_picture_label)

        Panel_layout.addWidget(self.element_name_label)
        Panel_layout.addWidget(self.previous_element_button)
        Panel_layout.addWidget(self.next_element_button)
        Panel_layout.addWidget(self.use_for_mask_button)
        Panel_layout.addWidget(self.quantify_button)

        Results_layout.addWidget(self.Cursor_data_label)
        Results_layout.addWidget(Color("transparent"))
        Results_layout.addWidget(self.X_label)
        Results_layout.addWidget(self.X_value_label)
        Results_layout.addWidget(Color("transparent"))
        Results_layout.addWidget(self.Y_label)
        Results_layout.addWidget(self.Y_value_label)
        Results_layout.addWidget(Color("transparent"))
        Results_layout.addWidget(self.Value_label)
        Results_layout.addWidget(self.Value_value_label)
        Results_layout.addWidget(Color("transparent"))
        Results_layout.addWidget(Color("transparent"))
        Results_layout.addWidget(Color("transparent"))
        Results_layout.addWidget(self.Mean_label)
        Results_layout.addWidget(self.Mean_value_label)
        Results_layout.addWidget(Color("transparent"))
        Results_layout.addWidget(self.Median_label)
        Results_layout.addWidget(self.Median_value_label)
        Results_layout.addWidget(Color("transparent"))
        Results_layout.addWidget(self.Min_label)
        Results_layout.addWidget(self.Min_value_label)
        Results_layout.addWidget(Color("transparent"))
        Results_layout.addWidget(self.Max_label)
        Results_layout.addWidget(self.Max_value_label)
        Results_layout.addWidget(Color("transparent"))
        Results_layout.addWidget(self.Mask_label)
        Results_layout.addWidget(self.Mask_value_label)
        Results_layout.addWidget(Color("transparent"))
        

        widget = QWidget()
        widget.setLayout(pagelayout)
        self.setCentralWidget(widget)

    def Confirmed_names(self):
        #Let user use buttons:
        self.use_for_mask_button.setEnabled(True)
        self.next_element_button.setEnabled(True)
        self.previous_element_button.setEnabled(True)
        self.Prefere_folder.setPlaceholderText("Choose pattern folder")

        #setting custom names in folder:
        self.Main_Folder_Path = str(self.Main_folder.text())
        # self.Pixel_size = str(self.Pixel.text())
        # self.inputfile = str(self.Inputfile.text())
        # self.Zeropeak = str(self.Zeropeak.text())
        # self.Scater = str(self.Scater.text())
        # self.Sample_Matrix = str(self.SampMatrix.text())
        self.element_for_mask = str(self.Mask_value_label.text())
        self.Pixel_size = 5
        self.inputfile = "inputfile"
        self.Zeropeak = "zeropeak"
        self.Scater = "scater"
        self.Sample_Matrix = "sample_matrix"
                
        #finding and listing only subfolders (for excluding inpufile)
        path = Path(self.Main_Folder_Path)
        path_insides = os.listdir(path)
        folders_names = [file for file in path_insides if os.path.isdir(os.path.join(self.Main_Folder_Path,file)) ]
        self.Prefere_folder.addItems(folders_names)
        self.Prefere_folder.setEnabled(True)
        
    def prefered_folder_selected(self):
        sth

    def Confirmed_saving(self):
        self.saving_button.setEnabled(True)  
  
    def Saving(self):
        print("Saved")

    def ChooseMask(self):
        self.Mask_value_label.setText(str(self.element_name_label))

    def Quantify(self):
        
        self.sample_picture_label.setPixmap(self.sample_pixmap)
        self.resize(self.sample_pixmap.width(), self.sample_pixmap.height())



    def Previous_element(self):
        print("go back")
        #change element to previous one
        #make heatmap with plt    

    def Next_element(self):
        print("Next")
        

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()