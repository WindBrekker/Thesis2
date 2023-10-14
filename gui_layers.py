import sys
import os
import utils
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
        Sample_layout = QHBoxLayout()
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
        self.sample_picture_label2 = QLabel(self)
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
        self.Mask_value_label = QLabel("P",self)
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
        self.sample_pixmap_2 = QPixmap('photo.png')


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
        Sample_layout.addWidget(self.sample_picture_label2)

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
        self.Prefere_folder.clear() 
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
        #set the prefered folder as a variable
        self.chosen_folder = self.Prefere_folder.currentText()
        
        #Unpacking inputfile to a dictioary
        with open(Path(os.path.join(self.Main_Folder_Path,f"{self.inputfile}.txt")),"rt") as elements_file:  
            # a dictionary with values of K
            self.elements_dict = {}
            # a dictionary with values of energies (u_Eeffi)
            self.energy_elements_dict = {}
            # a dictionary with values of Z-number
            self.Z_element = {}
            for line in elements_file:
                columns = line.strip().split()
                element = columns[1]
                k_value = columns[2]
                energy = columns[3]
                Z_number = columns[0]
                self.elements_dict[element] = k_value
                self.energy_elements_dict[element] = energy
                self.Z_element[element] = Z_number
        #print(self.elements_dict)
        
        #Searching for prename
        file_names = os.listdir(Path(os.path.join(self.Main_Folder_Path,self.chosen_folder)))
        if file_names[0] != f"{self.Sample_Matrix}.txt":
            first_file = file_names[0]
        else:
            first_file = file_names[1]
        prename = first_file.split("__")[0]
        
        #unpacking sample matrix
        with open(Path(os.path.join(self.Main_Folder_Path,self.chosen_folder,f"{self.Sample_Matrix}.txt")),"rt") as sample_matrix_file:  
            sample_dict = {}
            for line in sample_matrix_file:
                columns = line.strip().split()
                element = columns[0]
                concentration = columns[1]
                sample_dict[element] = concentration
        
        #calculating livetime with zeropeak
        table_of_zeropeaks = utils.file_to_list(Path(os.path.join(self.Main_Folder_Path,self.chosen_folder,f"{prename}__{self.Zeropeak}.txt")))
        livetime = utils.LT_calc(table_of_zeropeaks) 
        
        if not Path(os.path.join(self.Main_Folder_Path,f"{self.chosen_folder}_output")).exists():
            Path(os.path.join(self.Main_Folder_Path,f"{self.chosen_folder}_output")).mkdir()
        utils.output_to_file(livetime, Path(os.path.join(self.Main_Folder_Path,f"{self.chosen_folder}_output",f"{prename}_livetime_map")))

        # wczytywanie mapy fosforu do maski
        element_for_mask = self.Mask_value_label.text()
        table_of_mask = utils.file_to_list(Path(os.path.join(self.Main_Folder_Path, self.chosen_folder, f"{prename}__{element_for_mask}.txt")))
        
        # baza do maski - zerowanie wartości poniżej 10% max wartości l zliczeń pierwiastka maski w próbce
        maxof_masktable = max([sublist[-1] for sublist in table_of_mask])
        # print(maxof_masktable)
        procent = 0.1
        mask = [
            [0 for j in range(len(table_of_mask[0]))] for i in range(len(table_of_mask))
        ]
        for i in range(len(table_of_mask)):
            for j in range(len(table_of_mask[0])):
                if table_of_mask[i][j] < (procent * maxof_masktable):
                    mask[i][j] = 0
                else:
                    mask[i][j] = 1
        utils.output_to_file(mask, Path(os.path.join(self.Main_Folder_Path,f"{self.chosen_folder}_output", f"{prename}_mask")))            
        plt.imshow(mask, cmap="hot", interpolation="nearest")
        plt.title("Mask heatmap")
        plt.savefig(Path(os.path.join(self.Main_Folder_Path,f"{self.chosen_folder}_output","mask.png")))
        plt.close()
        self.sample_pixmap = QPixmap(os.path.join(self.Main_Folder_Path,f"{self.chosen_folder}_output","mask.png"))
        self.sample_picture_label.setPixmap(self.sample_pixmap)
        
        plt.imshow(os.path.join(self.Main_Folder_Path,self.chosen_folder,), cmap="hot", interpolation="nearest")
        plt.title("Mask heatmap")
        plt.savefig(Path(os.path.join(self.Main_Folder_Path,f"{self.chosen_folder}_output","mask.png")))
        plt.close()
        self.sample_pixmap = QPixmap(os.path.join(self.Main_Folder_Path,f"{self.chosen_folder}_output","mask.png"))
        self.sample_picture_label.setPixmap(self.sample_pixmap)
        
            

    def Confirmed_saving(self):
        self.saving_button.setEnabled(True)  
  
    def Saving(self):
        print("Saved")

    def ChooseMask(self):
        self.Mask_value_label.setText(str(self.element_name_label))

    def Quantify(self):
        print("Quantify")

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