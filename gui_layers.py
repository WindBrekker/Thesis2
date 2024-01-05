import sys
import shutil
import os
import utils
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from pathlib import Path
from os.path import exists as file_exists
from PyQt6.QtGui import QPalette, QColor, QIcon, QAction, QPixmap
from pathlib import Path
from PyQt6.QtWidgets import (
    QApplication,
    QLineEdit,
    QLabel,
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QPushButton,
    QHBoxLayout,
    QComboBox,
    QCheckBox,
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
        self.showMaximized()

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
        saving_checkbox_Ci1_layout = QHBoxLayout()
        saving_checkbox_Ci2_layout = QHBoxLayout()
        saving_checkbox_SM1_layout = QHBoxLayout()
        saving_checkbox_SM2_layout = QHBoxLayout()
        saving_checkbox_SMi1_layout = QHBoxLayout()
        saving_checkbox_SMi2_layout = QHBoxLayout()
        saving_checkbox_Ci3_layout = QHBoxLayout()
        saving_checkbox_Ci4_layout = QHBoxLayout()
        saving_checkbox_SM3_layout = QHBoxLayout()
        saving_checkbox_SM4_layout = QHBoxLayout()
        saving_checkbox_SMi3_layout = QHBoxLayout()
        saving_checkbox_SMi4_layout = QHBoxLayout()
        
    #sub Left_layout
        Sample_layout = QHBoxLayout()
        # Sample_layout.addWidget(Color("pink"))
        Panel_layout = QHBoxLayout()
        # Panel_layout.addWidget(Color("orange"))
    #input_layout
        text_layout = QHBoxLayout()
        main_folder_layout = QHBoxLayout()
        pixel_size_layout = QHBoxLayout()
        

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
        
        self.Ci_label = QLabel("Save the concentration maps as:",self)
        self.SM_label = QLabel("Save the sample mass per unit area as:",self)
        self.SMi_label = QLabel("Save the element mass per unit area as:",self)
        self.Ci_unit_label = QLabel("   With units:",self)
        self.SM_unit_label = QLabel("   With units:",self)
        self.SMi_unit_label = QLabel("  With units:",self)
        
        Saving_layout.addWidget(self.Ci_label)
        Saving_layout.addLayout(saving_checkbox_Ci1_layout)
        Saving_layout.addLayout(saving_checkbox_Ci2_layout)
        Saving_layout.addWidget(self.Ci_unit_label)
        Saving_layout.addLayout(saving_checkbox_Ci3_layout)
        Saving_layout.addLayout(saving_checkbox_Ci4_layout)
        Saving_layout.addWidget(self.SM_label)
        Saving_layout.addLayout(saving_checkbox_SM1_layout)
        Saving_layout.addLayout(saving_checkbox_SM2_layout)
        Saving_layout.addWidget(self.SM_unit_label)
        Saving_layout.addLayout(saving_checkbox_SM3_layout)
        Saving_layout.addLayout(saving_checkbox_SM4_layout)
        Saving_layout.addWidget(self.SMi_label)
        Saving_layout.addLayout(saving_checkbox_SMi1_layout)
        Saving_layout.addLayout(saving_checkbox_SMi2_layout)
        Saving_layout.addWidget(self.SMi_unit_label)
        Saving_layout.addLayout(saving_checkbox_SMi3_layout)
        Saving_layout.addLayout(saving_checkbox_SMi4_layout)
        

        
        
        
        Input_layout.addLayout(text_layout,2)
        Input_layout.addLayout(main_folder_layout,4)
        Input_layout.addLayout(pixel_size_layout,4)
        

        #Widgets
        #QLabel
        self.colorbox_label = QLabel("Choose the heatmap colors")
        self.Treshold_txt_label = QLabel("Treshold = ",self)
        self.Treshold_unit_label = QLabel("%",self)
        self.pixel_size_txt_label = QLabel("Pixel size = ",self)
        self.pixel_size_unit_label = QLabel("[um]",self)

        
        self.sample_picture_label = QLabel(self)
        self.sample_picture_label2 = QLabel(self)
        
        
        self.element_name_label = QLabel(self)
        self.element_name_label.setText("None")
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
        self.Mask_value_label2 = QLabel("Current element:",self)
        self.Mask_value_label = QLabel("None",self)
        self.input_info_label = QLabel("Enter the appropriate values*",self)
        self.names_inof_label = QLabel("(optional) Enter used nomenclature",self)

  

        # #QLineEdit
        self.Main_folder = QLineEdit(self)
        self.Main_folder.setPlaceholderText("Main folder path")
        self.Pixel = QLineEdit(self)
        self.Pixel.setPlaceholderText("1000")
        self.Inputfile = QLineEdit(self)
        self.Inputfile.setPlaceholderText("inputfile")
        self.Zeropeak = QLineEdit(self)
        self.Zeropeak.setPlaceholderText("zeropeak")
        self.Scater = QLineEdit(self)    
        self.Scater.setPlaceholderText("scater")
        self.SampMatrix = QLineEdit(self)
        self.SampMatrix.setPlaceholderText("sample_matrix")
        self.Treshold = QLineEdit(self)
        self.Treshold.setPlaceholderText("10")

        # #QComboBox
        self.colorbar_combobox = QComboBox(self)
        self.colorbar_combobox.addItems(["hot","viridis","plasma","inferno", "magma", "cividis", "coolwarm", "YlGnBu", "RdYlBu", "jet", "copper"])
        self.Prefere_folder = QComboBox(self)
        self.Prefere_folder.activated.connect(self.prefered_folder_selected)
        self.Prefere_folder.setEnabled(False)
        self.Prefere_folder.setPlaceholderText("Confirm identifiers first")

        # #QCheckBox
        self.Ci_dat_checkbox = QCheckBox(".dat",self)
        self.Ci_png_checkbox = QCheckBox(".png",self)
        self.Ci_tiff_checkbox = QCheckBox(".tiff",self)
        self.Ci_bmp_checkbox = QCheckBox(".pdf",self)
        
        self.Ci_procent_checkbox = QCheckBox("%",self)
        self.Ci_mg_checkbox = QCheckBox("mg/g",self)
        self.Ci_ug_checkbox = QCheckBox("ug/g",self)
        self.Ci_auto_checkbox = QCheckBox("auto",self)
        
        self.sample_mass_dat_checkbox = QCheckBox(".dat",self)
        self.sample_mass_png_checkbox = QCheckBox(".png",self)
        self.sample_mass_tiff_checkbox = QCheckBox(".tiff",self)
        self.sample_mass_bmp_checkbox = QCheckBox(".pdf",self)
        
        self.sample_mass_g_checkbox = QCheckBox("g/g",self)
        self.sample_mass_mg_checkbox = QCheckBox("mg/g",self)
        self.sample_mass_ug_checkbox = QCheckBox("ug/g",self)
        self.sample_mass_ng_checkbox = QCheckBox("ng/g",self)      
              
        self.element_mass_dat_checkbox = QCheckBox(".dat",self)
        self.element_mass_png_checkbox = QCheckBox(".png",self)
        self.element_mass_tiff_checkbox = QCheckBox(".tiff",self)
        self.element_mass_bmp_checkbox = QCheckBox(".pdf",self)
        
        self.element_mass_g_checkbox = QCheckBox("g/g",self)
        self.element_mass_mg_checkbox = QCheckBox("mg/g",self)
        self.element_mass_ug_checkbox = QCheckBox("ug/g",self)
        self.element_mass_ng_checkbox = QCheckBox("ng/g",self) 
        
        
        
        
        
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
        
        self.saving_button = QPushButton("Exit",self)
        self.saving_button.setEnabled(False)
        self.saving_button.clicked.connect(self.Exit)


        # #Adding widgets
        text_layout.addWidget(self.input_info_label)
        main_folder_layout.addWidget(self.Main_folder)
        pixel_size_layout.addWidget(self.Treshold_txt_label)
        pixel_size_layout.addWidget(self.Treshold)
        pixel_size_layout.addWidget(self.Treshold_unit_label)
        pixel_size_layout.addWidget(self.pixel_size_txt_label)
        pixel_size_layout.addWidget(self.Pixel)
        pixel_size_layout.addWidget(self.pixel_size_unit_label)

        Names_layout.addWidget(self.names_inof_label)
        Names_layout.addWidget(self.Inputfile)
        Names_layout.addWidget(self.Zeropeak)
        Names_layout.addWidget(self.Scater)
        Names_layout.addWidget(self.SampMatrix)
        Names_layout.addWidget(self.colorbox_label)
        Names_layout.addWidget(self.colorbar_combobox)
        Names_layout.addWidget(self.confirm_names_button)
        Names_layout.addWidget(self.Prefere_folder)
        
        
        

        saving_checkbox_Ci1_layout.addWidget(self.Ci_dat_checkbox)
        saving_checkbox_Ci1_layout.addWidget(self.Ci_bmp_checkbox)
        saving_checkbox_Ci2_layout.addWidget(self.Ci_png_checkbox)
        saving_checkbox_Ci2_layout.addWidget(self.Ci_tiff_checkbox)

        saving_checkbox_Ci3_layout.addWidget(self.Ci_procent_checkbox)
        saving_checkbox_Ci3_layout.addWidget(self.Ci_mg_checkbox)
        saving_checkbox_Ci4_layout.addWidget(self.Ci_ug_checkbox)
        saving_checkbox_Ci4_layout.addWidget(self.Ci_auto_checkbox)    

        saving_checkbox_SM1_layout.addWidget(self.sample_mass_dat_checkbox)
        saving_checkbox_SM1_layout.addWidget(self.sample_mass_png_checkbox)
        saving_checkbox_SM2_layout.addWidget(self.sample_mass_tiff_checkbox)
        saving_checkbox_SM2_layout.addWidget(self.sample_mass_bmp_checkbox)

        saving_checkbox_SM3_layout.addWidget(self.sample_mass_g_checkbox)
        saving_checkbox_SM3_layout.addWidget(self.sample_mass_mg_checkbox)
        saving_checkbox_SM4_layout.addWidget(self.sample_mass_ug_checkbox)
        saving_checkbox_SM4_layout.addWidget(self.sample_mass_ng_checkbox)       

        saving_checkbox_SMi1_layout.addWidget(self.element_mass_dat_checkbox)
        saving_checkbox_SMi1_layout.addWidget(self.element_mass_png_checkbox)
        saving_checkbox_SMi2_layout.addWidget(self.element_mass_tiff_checkbox)
        saving_checkbox_SMi2_layout.addWidget(self.element_mass_bmp_checkbox)

        saving_checkbox_SMi3_layout.addWidget(self.element_mass_g_checkbox)
        saving_checkbox_SMi3_layout.addWidget(self.element_mass_mg_checkbox)
        saving_checkbox_SMi4_layout.addWidget(self.element_mass_ug_checkbox)
        saving_checkbox_SMi4_layout.addWidget(self.element_mass_ng_checkbox)
        
        saving_button_layout.addWidget(self.confirm_saving_button)
        saving_button_layout.addWidget(self.saving_button)


        Sample_layout.addWidget(self.sample_picture_label)
        Sample_layout.addWidget(self.sample_picture_label2)

        Panel_layout.addWidget(self.Mask_value_label2)
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
        self.confirm_saving_button.setEnabled(True)
        self.Prefere_folder.clear() 
        self.Prefere_folder.setPlaceholderText("Choose pattern folder")

        #setting custom names in folder:
        self.Main_Folder_Path = str(self.Main_folder.text())
        self.Pixel_size = str(self.Pixel.text())
        self.inputfile_name = str(self.Inputfile.text())
        self.zeropeak_name = str(self.Zeropeak.text())
        self.scater_name = str(self.Scater.text())
        self.Sample_Matrix_name = str(self.SampMatrix.text())
        self.treshold = str(self.Treshold.text())
        self.color_of_heatmap = str(self.colorbar_combobox.currentText())
        

        self.element_for_mask = str(self.Mask_value_label.text())
        if self.Pixel_size == "":
            self.Pixel_size = 1000
        if self.inputfile_name == "":
            self.inputfile_name = "inputfile"
        if self.zeropeak_name == "":
            self.zeropeak_name = "zeropeak"
        if self.scater_name == "":
            self.scater_name = "scater"
        if self.Sample_Matrix_name== "":
            self.Sample_Matrix_name = "sample_matrix"
        if self.treshold == "":
            self.treshold = 10
            
        path = Path(self.Main_Folder_Path)
        
        path_insides = os.listdir(path)
        self.folders_names = [file for file in path_insides if os.path.isdir(os.path.join(path,file))]
        self.Prefere_folder.addItems(self.folders_names) 
        self.Prefere_folder.setEnabled(True)
        
        #Unpacking inputfile to a dictioary
        with open(Path(os.path.join(self.Main_Folder_Path,f"{self.inputfile_name}.txt")),"rt") as elements_file:  
            # a dictionary with values of K
            self.K_value_per_element_dict = {}
            # a dictionary with values of energies (u_Eeffi)
            self.energy_per_element_dict = {}
            # a dictionary with values of Z-number
            self.Z_number_per_element_dict = {}
            for line in elements_file:
                columns = line.strip().split()
                element = columns[1]
                k_value = columns[2] #K_i [cm^2 s^-1 g^-1]
                energy = columns[3]
                Z_number = columns[0]
                self.K_value_per_element_dict[element] = k_value
                self.energy_per_element_dict[element] = energy
                self.Z_number_per_element_dict[element] = Z_number
                
        with open (os.path.join(self.Main_Folder_Path,"inputfile_scater.txt")) as scater_factors:
            for line in scater_factors:
                self.scater_dict = {}
                columns = line.strip().split()
                self.scater_dict["a"] = columns[0]
                self.scater_dict["b"] = columns[1]
        with open (os.path.join(self.Main_Folder_Path,"inputfile_zeropeak.txt")) as zeropeak_factors:
            for line in zeropeak_factors:
                self.zeropeak_dict = {}
                columns = line.strip().split()
                self.zeropeak_dict["a"] = columns[0]
                self.zeropeak_dict["b"] = columns[1]
                
        #unpacking sample matrix
        with open(Path(os.path.join(self.Main_Folder_Path,f"{self.Sample_Matrix_name}.txt")),"rt") as sample_matrix_file:  
            self.concentration_per_element_dict = {}
            for line in sample_matrix_file:
                columns = line.strip().split()
                element = columns[0]
                concentration = columns[1]
                self.concentration_per_element_dict[element] = concentration          
        
    def prefered_folder_selected(self):
        self.current_index = 0
        #set the prefered folder as a variable
        self.chosen_folder = self.Prefere_folder.currentText()
        
        #listing the elements inside
        self.elements_in_nodec = []
        path = Path(os.path.join(self.Main_Folder_Path, self.chosen_folder))
        path_insides = os.listdir(path)
        for file in path_insides:
            reversed_file = file [::-1]
            splitted_file = reversed_file.split("_")[0]
            last_element_of_file = splitted_file[::-1]
            if last_element_of_file.split(".")[0] != self.scater_name and last_element_of_file.split(".")[0] != self.zeropeak_name:
                reversed_element = splitted_file.split(".")[1]
                element = reversed_element[::-1] 
                self.elements_in_nodec.append(element)
               
        
        self.element_name_label.setText(self.elements_in_nodec[0])
        
            
        #Searching for prename
        file_names = os.listdir(Path(os.path.join(self.Main_Folder_Path,self.chosen_folder)))
        first_file = file_names[0]
        self.prename = first_file.split("_")[0]
        self.separator = first_file.split(self.prename)[1].split(self.elements_in_nodec[0])[0]
        
        
        
        #calculating livetime with zeropeak
        zeropeak_matrix = utils.file_to_list(Path(os.path.join(self.Main_Folder_Path,self.chosen_folder,f"{self.prename}{self.separator}{self.zeropeak_name}.txt")))
        self.livetime_matrix = utils.LT_calc(zeropeak_matrix,self.zeropeak_dict["a"],self.zeropeak_dict["b"]) 
        
        if not Path(os.path.join(self.Main_Folder_Path,f"{self.chosen_folder}_output")).exists():
            Path(os.path.join(self.Main_Folder_Path,f"{self.chosen_folder}_output")).mkdir()

        utils.output_to_file(self.livetime_matrix, Path(os.path.join(self.Main_Folder_Path,f"{self.chosen_folder}_output",f"{self.prename}_livetime_map"))) 
        self.mask_map = utils.mask_creating(self.elements_in_nodec[0],self.Main_Folder_Path,self.chosen_folder,self.prename,self.treshold,self.color_of_heatmap)
        
        self.sample_pixmap = QPixmap(os.path.join(self.Main_Folder_Path,f"{self.chosen_folder}_output","mask.png"))
        self.sample_picture_label.setPixmap(self.sample_pixmap)
               
        self.sample_pixmap2 = QPixmap(os.path.join(self.Main_Folder_Path,f"{self.chosen_folder}_output","mask_noc.png"))
        self.sample_picture_label2.setPixmap(self.sample_pixmap2)

    def Previous_element(self):
        if self.current_index > 0:
            self.current_index -= 1
            self.element_name_label.setText(self.elements_in_nodec[self.current_index])
            
            utils.mask_creating(self.elements_in_nodec[self.current_index],self.Main_Folder_Path,self.chosen_folder,self.prename,self.treshold,self.color_of_heatmap)
            self.sample_pixmap = QPixmap(os.path.join(self.Main_Folder_Path,f"{self.chosen_folder}_output","mask.png"))
            self.sample_picture_label.setPixmap(self.sample_pixmap)
                
            self.sample_pixmap2 = QPixmap(os.path.join(self.Main_Folder_Path,f"{self.chosen_folder}_output","mask_noc.png"))
            self.sample_picture_label2.setPixmap(self.sample_pixmap2)
        
    def Next_element(self):
        if self.current_index < len(self.elements_in_nodec) - 1:
            self.current_index += 1
            self.element_name_label.setText(self.elements_in_nodec[self.current_index])
            utils.mask_creating(self.elements_in_nodec[self.current_index],self.Main_Folder_Path,self.chosen_folder,self.prename,self.treshold,self.color_of_heatmap)
            self.sample_pixmap = QPixmap(os.path.join(self.Main_Folder_Path,f"{self.chosen_folder}_output","mask.png"))
            self.sample_picture_label.setPixmap(self.sample_pixmap)
                
            self.sample_pixmap2 = QPixmap(os.path.join(self.Main_Folder_Path,f"{self.chosen_folder}_output","mask_noc.png"))
            self.sample_picture_label2.setPixmap(self.sample_pixmap2)
        
    def ChooseMask(self):
        self.Mask_value_label.setText(str(self.element_name_label.text()))
        self.quantify_button.setEnabled(True)

    def Quantify(self):
        for f in self.folders_names:
            self.folder = f

            #Create folder for outputs, if doesnt exist one yet
            if not Path(os.path.join(self.Main_Folder_Path,"temporary")).exists():
                Path(os.path.join(self.Main_Folder_Path,"temporary")).mkdir()
            if not Path(os.path.join(self.Main_Folder_Path,f"{self.folder}_output")).exists():
                Path(os.path.join(self.Main_Folder_Path,f"{self.folder}_output")).mkdir()
            if not Path(os.path.join(self.Main_Folder_Path,"temporary",f"{self.folder}_output")).exists():
                Path(os.path.join(self.Main_Folder_Path,"temporary",f"{self.folder}_output")).mkdir() 
            self.temporary_folder = Path(os.path.join(self.Main_Folder_Path,"temporary",f"{self.folder}_output"))
            
            #loop for every element in all folders
            for key in self.Z_number_per_element_dict:
                    element = key
                    
                    #check if there is data for the element in this folder
                    if file_exists(os.path.join(self.Main_Folder_Path,self.folder, f"{self.prename}{self.separator}{element}.txt")):
                        K_i = float(self.K_value_per_element_dict[element])
                        counts_data = os.path.join(self.Main_Folder_Path, self.folder,f"{self.prename}{self.separator}{element}.txt")
                        counts_table = utils.file_to_list(counts_data)
                        table_of_smi = [[0 for j in range(len(counts_table[0]))]for i in range(len(counts_table))]
                        
                        for i in range(len(counts_table)):
                            for j in range(len(counts_table[0])):
                                table_of_smi[i][j] = (((float(counts_table[i][j]) * float(self.mask_map[i][j])))/ float(self.livetime_matrix[i][j])/ (float(K_i)))
                        utils.output_to_file(table_of_smi,os.path.join(self.temporary_folder,f"{element}_element_mass_noc"))
                        
                        sm = []
                        scater_tab = []
                        scater_tab = utils.file_to_list(os.path.join(self.Main_Folder_Path,self.folder,f"{self.prename}{self.separator}{self.scater_name}.txt"))
                        sm_livetime = [[0 for j in range(len(scater_tab[0]))]for i in range(len(scater_tab))]
                        
                        for i in range(len(scater_tab)):
                            for j in range(len(scater_tab[0])):
                                sm_livetime[i][j] = float(scater_tab[i][j]) / float(self.livetime_matrix[i][j])

                        sm = utils.SampSM_calc(sm_livetime,self.scater_dict["a"],self.scater_dict["b"])
                        sm_masked = [[0 for j in range(len(sm[0]))] for i in range(len(sm))]
                        for i in range(len(scater_tab)):
                            for j in range(len(scater_tab[0])):
                                sm_masked[i][j] = sm[i][j] * self.mask_map[i][j]
                        utils.output_to_file(sm_masked,os.path.join(self.temporary_folder,"sample_mass_noc")) 
                              
                        

                        Ci_table = [[0 for j in range(len(sm[0]))] for i in range(len(sm))]
                        lambda_factor = [[0 for j in range(len(sm[0]))] for i in range(len(sm))]
                        counter = 0
                        Ci_table_sum = 0
                        lambda_factor_sum = 0
                        for i in range(len(sm)):
                            for j in range(len(sm[0])):
                                if table_of_smi[i][j] != 0:
                                    lambda_factor[i][j] = utils.lambda_factor(sm[i][j], int(self.Z_number_per_element_dict[element]),float(self.energy_per_element_dict[element]),self.concentration_per_element_dict )
                                    Ci_table[i][j] = (table_of_smi[i][j] * lambda_factor[i][j] / sm[i][j])
                                    counter +=1
                                    Ci_table_sum += Ci_table[i][j]
                                    lambda_factor_sum += lambda_factor[i][j]
                                    
                                else:
                                    continue
                        lambda_average_factor = lambda_factor_sum/counter
                        Ci_average_factor = Ci_table_sum/counter
                        
                        utils.output_to_file(lambda_factor,os.path.join(self.Main_Folder_Path,f"{self.folder}_output",f"{self.prename}_{element}_lambda"))
                        with open( os.path.join(self.Main_Folder_Path,f"{self.folder}_output", f"lambda_Ci_average.txt"), "a") as f:
                            f.write(f'element:  {element},  average lambda: {format(lambda_average_factor, ".2e")},    average Ci [g/g]: {format(Ci_average_factor, ".2e")}, \n')                        
                        utils.output_to_file(Ci_table,os.path.join(self.Main_Folder_Path,"temporary",f"{self.folder}_output",f"{self.prename}_{element}_Ci"))
                        
                                               

                                   
                    else:
                        continue  

            
                             
        self.chosen_folder = self.Prefere_folder.currentText()
        self.confirm_names_button.disconnect()
        self.confirm_names_button.setEnabled(False)
        self.previous_element_button.disconnect()
        self.previous_element_button.clicked.connect(self.previous_element_final)
        self.next_element_button.disconnect()
        self.next_element_button.clicked.connect(self.next_element_final)
        self.quantify_button.disconnect()
        self.quantify_button.setText("Go back")
        self.quantify_button.clicked.connect(self.Back_to_quantify)
        self.Prefere_folder.activated.disconnect()
        self.Prefere_folder.activated.connect(self.new_prefered_folder)
        
        iteration = 0
        print(self.elements_in_nodec[iteration])
        while not Path(os.path.join(self.Main_Folder_Path,"temporary",f"{self.chosen_folder}_output",f"{self.prename}_{self.elements_in_nodec[iteration]}_Ci.txt")).exists():
            iteration += 1
            print(iteration)
            print(self.elements_in_nodec[iteration])
        
        
        plt.imshow(utils.file_to_list(os.path.join(self.Main_Folder_Path,"temporary",f"{self.chosen_folder}_output",f"{self.prename}_{self.elements_in_nodec[iteration]}_Ci.txt")), cmap=self.color_of_heatmap, interpolation="nearest")
        plt.title("Concentration map")
        plt.colorbar()
        plt.savefig(os.path.join(self.Main_Folder_Path,"temporary",f"{self.chosen_folder}_output",f"{self.prename}_{self.elements_in_nodec[iteration]}_Ci.png"))
        plt.close()
        
        
        self.sample_pixmap = QPixmap(os.path.join(self.Main_Folder_Path,"temporary",f"{self.chosen_folder}_output",f"{self.prename}_{self.elements_in_nodec[iteration]}_Ci.png"))
        self.sample_picture_label.setPixmap(self.sample_pixmap)
        
        # self.sample_pixmap2 = QPixmap(os.path.join(self.Main_Folder_Path,f"{self.chosen_folder}_output","mask_noc.png"))
        self.sample_picture_label2.setPixmap(self.sample_pixmap)
        
        element_table_not_masked = np.array(utils.file_to_list(os.path.join(self.Main_Folder_Path,"temporary",f"{self.chosen_folder}_output",f"{self.elements_in_nodec[iteration]}_element_mass_noc.txt")))

        self.element_table = element_table_not_masked[element_table_not_masked != 0]
        self.Mean_value_label.setText(str(np.average(self.element_table)))
        self.Median_value_label.setText(str(np.median(self.element_table)))
        self.Min_value_label.setText(str(np.min(self.element_table)))
        self.Max_value_label.setText(str(np.max(self.element_table)))
        
        self.saving_button.setEnabled(True)                                      

    def Back_to_quantify(self):
        
        # self.sample_pixmap = QPixmap(os.path.join(self.Main_Folder_Path,f"{self.folder}_output","mask.png"))
        # self.sample_picture_label.setPixmap(self.sample_pixmap)
        # self.sample_pixmap2 = QPixmap(os.path.join(self.Main_Folder_Path,f"{self.folder}_output","mask_noc.png"))
        # self.sample_picture_label2.setPixmap(self.sample_pixmap2)
        
        self.quantify_button.setText("Quantify")
        self.quantify_button.disconnect()
        self.quantify_button.clicked.connect(self.Quantify)
        self.Prefere_folder.disconnect()
        self.Prefere_folder.activated.connect(self.prefered_folder_selected)
        self.confirm_names_button.clicked.connect(self.Confirmed_names)
        self.previous_element_button.disconnect()
        self.previous_element_button.clicked.connect(self.Previous_element)
        self.next_element_button.disconnect()
        self.next_element_button.clicked.connect(self.Next_element)       
        
    def next_element_final(self):
        if self.current_index < len(self.elements_in_nodec) - 1:
            self.current_index += 1
            self.element_name_label.setText(self.elements_in_nodec[self.current_index])   
            
            
            plt.imshow(utils.file_to_list(os.path.join(self.Main_Folder_Path,"temporary",f"{self.chosen_folder}_output",f"{self.prename}_{self.elements_in_nodec[self.current_index]}_Ci.txt")), cmap=self.color_of_heatmap, interpolation="nearest")
            plt.title("Concentration map")
            plt.colorbar()
            plt.savefig(os.path.join(self.Main_Folder_Path,"temporary",f"{self.chosen_folder}_output",f"{self.prename}_{self.elements_in_nodec[self.current_index]}_Ci.png"))
            plt.close()
            
            
            self.sample_pixmap = QPixmap(os.path.join(self.Main_Folder_Path,"temporary",f"{self.chosen_folder}_output",f"{self.prename}_{self.elements_in_nodec[self.current_index]}_Ci.png"))
            self.sample_picture_label.setPixmap(self.sample_pixmap)
            
            # self.sample_pixmap2 = QPixmap(os.path.join(self.Main_Folder_Path,f"{self.chosen_folder}_output","mask_noc.png"))
            self.sample_picture_label2.setPixmap(self.sample_pixmap)
            
            
            element_table_not_masked = np.array(utils.file_to_list(os.path.join(self.Main_Folder_Path,"temporary",f"{self.chosen_folder}_output",f"{self.elements_in_nodec[self.current_index]}_element_mass_noc.txt")))

            self.element_table = element_table_not_masked[element_table_not_masked != 0]

            self.Mean_value_label.setText(str(format('{:.2e}'.format(np.average(self.element_table)))))
            self.Median_value_label.setText(str(np.median(self.element_table)))
            self.Min_value_label.setText(str(np.min(self.element_table)))
            self.Max_value_label.setText(str(np.max(self.element_table)))
            
    def previous_element_final(self):
        if self.current_index > 0:
            self.current_index -= 1
            self.element_name_label.setText(self.elements_in_nodec[self.current_index])
        
            plt.imshow(utils.file_to_list(os.path.join(self.Main_Folder_Path,"temporary",f"{self.chosen_folder}_output",f"{self.prename}_{self.elements_in_nodec[self.current_index]}_Ci.txt")), cmap=self.color_of_heatmap, interpolation="nearest")
            plt.title("Concentration map")
            plt.colorbar()
            plt.savefig(os.path.join(self.Main_Folder_Path,"temporary",f"{self.chosen_folder}_output",f"{self.prename}_{self.elements_in_nodec[self.current_index]}_Ci.png"))
            plt.close()
            
            
            self.sample_pixmap = QPixmap(os.path.join(self.Main_Folder_Path,"temporary",f"{self.chosen_folder}_output",f"{self.prename}_{self.elements_in_nodec[self.current_index]}_Ci.png"))
            self.sample_picture_label.setPixmap(self.sample_pixmap)
            
            # self.sample_pixmap2 = QPixmap(os.path.join(self.Main_Folder_Path,f"{self.chosen_folder}_output","mask_noc.png"))
            self.sample_picture_label2.setPixmap(self.sample_pixmap)
            
            element_table_not_masked = np.array(utils.file_to_list(os.path.join(self.Main_Folder_Path,"temporary",f"{self.chosen_folder}_output",f"{self.elements_in_nodec[self.current_index]}_element_mass_noc.txt")))

            self.element_table = element_table_not_masked[element_table_not_masked != 0]

            self.Mean_value_label.setText(str(format('{:.2e}'.format(np.average(self.element_table)))))
            self.Median_value_label.setText(str(np.median(self.element_table)))
            self.Min_value_label.setText(str(np.min(self.element_table)))
            self.Max_value_label.setText(str(np.max(self.element_table)))
                    
    def new_prefered_folder(self):
        self.chosen_folder = self.Prefere_folder.currentText()
        
        #listing the elements inside
        self.elements_in_nodec = []
        path = Path(os.path.join(self.Main_Folder_Path, self.chosen_folder))
        path_insides = os.listdir(path)
        for file in path_insides:
            reversed_file = file [::-1]
            splitted_file = reversed_file.split("_")[0]
            last_element_of_file = splitted_file[::-1]
            if last_element_of_file.split(".")[0] != self.scater_name and last_element_of_file.split(".")[0] != self.zeropeak_name:
                reversed_element = splitted_file.split(".")[1]
                element = reversed_element[::-1] 
                self.elements_in_nodec.append(element)
               
        
        self.element_name_label.setText(self.elements_in_nodec[0])    
        
        #Prename
        file_names = os.listdir(Path(os.path.join(self.Main_Folder_Path,self.chosen_folder)))
        first_file = file_names[0]
        self.prename = first_file.split("_")[0]
        
        # self.sample_pixmap = QPixmap(os.path.join(self.Main_Folder_Path,f"{self.chosen_folder}_output",f"{self.prename}_{self.elements_in_nodec[0]}_Ci.png"))
        # self.sample_picture_label.setPixmap(self.sample_pixmap)
        # self.sample_pixmap_2 = QPixmap(os.path.join(self.Main_Folder_Path,f"{self.chosen_folder}_output",f"{self.prename}_{self.elements_in_nodec[0]}_Ci.png"))
        # self.sample_picture_label2.setPixmap(self.sample_pixmap_2)
        
    def Confirmed_saving(self):
        self.quantify_button.setEnabled(True)
        self.use_for_mask_button.setEnabled(True)        
        self.next_element_button.setEnabled(True)
        self.previous_element_button.setEnabled(True)      
  
    def Exit(self):
        for f in self.folders_names:
            self.folder = f
            
            #loop for every element in all folders
            for key in self.Z_number_per_element_dict:
                    element = key
                    
                    #check if there is data for the element in this folder
                    if file_exists(os.path.join(self.Main_Folder_Path,self.folder, f"{self.prename}{self.separator}{element}.txt")):
                        
                        sm = utils.file_to_list(os.path.join(self.Main_Folder_Path, "temporary", f"{self.folder}_output","sample_mass_noc.txt"))
                        table_of_smi = utils.file_to_list(os.path.join(self.Main_Folder_Path, "temporary", f"{self.folder}_output",f"{element}_element_mass_noc.txt"))
                        Ci_table = utils.file_to_list(os.path.join(self.Main_Folder_Path, "temporary", f"{self.folder}_output",f"{self.prename}_{element}_Ci.txt"))
                        
                        
                        if self.element_mass_dat_checkbox.isChecked():
                            if self.element_mass_g_checkbox.isChecked():
                                utils.SMi_saving_dat(table_of_smi,os.path.join(self.Main_Folder_Path,f"{self.folder}_output",f"{self.prename}_{element}_smi"),element,1)
                            if self.element_mass_mg_checkbox.isChecked():
                                utils.SMi_saving_dat(table_of_smi,os.path.join(self.Main_Folder_Path,f"{self.folder}_output",f"{self.prename}_{element}_smi"),element,1000)
                            if self.element_mass_ug_checkbox.isChecked():
                                utils.SMi_saving_dat(table_of_smi,os.path.join(self.Main_Folder_Path,f"{self.folder}_output",f"{self.prename}_{element}_smi"),element,1000000)
                            if self.element_mass_ng_checkbox.isChecked():
                                utils.SMi_saving_dat(table_of_smi,os.path.join(self.Main_Folder_Path,f"{self.folder}_output",f"{self.prename}_{element}_smi"),element,1000000000)
                                                
                        if self.element_mass_png_checkbox.isChecked():
                            if self.element_mass_g_checkbox.isChecked():
                                utils.SMi_saving_plot(table_of_smi,os.path.join(self.Main_Folder_Path,f"{self.folder}_output",f"{self.prename}_{element}_smi"),element,self.Pixel_size,self.color_of_heatmap,1,".png")
                            if self.element_mass_mg_checkbox.isChecked():
                                utils.SMi_saving_plot(table_of_smi,os.path.join(self.Main_Folder_Path,f"{self.folder}_output",f"{self.prename}_{element}_smi"),element,self.Pixel_size,self.color_of_heatmap,1000,".png")
                            if self.element_mass_ug_checkbox.isChecked():
                                utils.SMi_saving_plot(table_of_smi,os.path.join(self.Main_Folder_Path,f"{self.folder}_output",f"{self.prename}_{element}_smi"),element,self.Pixel_size,self.color_of_heatmap,1000000,".png")
                            if self.element_mass_ng_checkbox.isChecked():
                                utils.SMi_saving_plot(table_of_smi,os.path.join(self.Main_Folder_Path,f"{self.folder}_output",f"{self.prename}_{element}_smi"),element,self.Pixel_size,self.color_of_heatmap,1000000000,".png")

                        if self.element_mass_bmp_checkbox.isChecked():
                            if self.element_mass_g_checkbox.isChecked():
                                utils.SMi_saving_plot(table_of_smi,os.path.join(self.Main_Folder_Path,f"{self.folder}_output",f"{self.prename}_{element}_smi"),element,self.Pixel_size,self.color_of_heatmap,1,".pdf")
                            if self.element_mass_mg_checkbox.isChecked():
                                utils.SMi_saving_plot(table_of_smi,os.path.join(self.Main_Folder_Path,f"{self.folder}_output",f"{self.prename}_{element}_smi"),element,self.Pixel_size,self.color_of_heatmap,1000,".pdf")
                            if self.element_mass_ug_checkbox.isChecked():
                                utils.SMi_saving_plot(table_of_smi,os.path.join(self.Main_Folder_Path,f"{self.folder}_output",f"{self.prename}_{element}_smi"),element,self.Pixel_size,self.color_of_heatmap,1000000,".pdf")
                            if self.element_mass_ng_checkbox.isChecked():
                                utils.SMi_saving_plot(table_of_smi,os.path.join(self.Main_Folder_Path,f"{self.folder}_output",f"{self.prename}_{element}_smi"),element,self.Pixel_size,self.color_of_heatmap,1000000000,".pdf")
                        
                        if self.element_mass_tiff_checkbox.isChecked():
                            if self.element_mass_g_checkbox.isChecked():
                                utils.SMi_saving_plot(table_of_smi,os.path.join(self.Main_Folder_Path,f"{self.folder}_output",f"{self.prename}_{element}_smi"),element,self.Pixel_size,self.color_of_heatmap,1,".tiff")
                            if self.element_mass_mg_checkbox.isChecked():
                                utils.SMi_saving_plot(table_of_smi,os.path.join(self.Main_Folder_Path,f"{self.folder}_output",f"{self.prename}_{element}_smi"),element,self.Pixel_size,self.color_of_heatmap,1000,".tiff")
                            if self.element_mass_ug_checkbox.isChecked():
                                utils.SMi_saving_plot(table_of_smi,os.path.join(self.Main_Folder_Path,f"{self.folder}_output",f"{self.prename}_{element}_smi"),element,self.Pixel_size,self.color_of_heatmap,1000000,".tiff")
                            if self.element_mass_ng_checkbox.isChecked():
                                utils.SMi_saving_plot(table_of_smi,os.path.join(self.Main_Folder_Path,f"{self.folder}_output",f"{self.prename}_{element}_smi"),element,self.Pixel_size,self.color_of_heatmap,1000000000,".tiff")
                    
                        
                        if self.Ci_png_checkbox.isChecked():
                            print("png checked")
                            print(element)
                            if self.Ci_auto_checkbox.isChecked():
                                print("auto")
                                utils.saving_plot_auto(Ci_table,os.path.join(self.Main_Folder_Path,f"{self.folder}_output",f"{self.prename}_{element}_Ci"),element,self.Pixel_size,self.color_of_heatmap,".png")
                            else:
                                print("else")
                                if self.Ci_mg_checkbox.isChecked():
                                    utils.Ci_saving_plot(Ci_table,os.path.join(self.Main_Folder_Path,f"{self.folder}_output",f"{self.prename}_{element}_Ci"),element,self.Pixel_size,self.color_of_heatmap,1000,".png")
                                if self.Ci_ug_checkbox.isChecked():
                                    utils.Ci_saving_plot(Ci_table,os.path.join(self.Main_Folder_Path,f"{self.folder}_output",f"{self.prename}_{element}_Ci"),element,self.Pixel_size,self.color_of_heatmap,1000000,".png")
                                if self.Ci_procent_checkbox.isChecked():
                                    utils.Ci_saving_plot(Ci_table,os.path.join(self.Main_Folder_Path,f"{self.folder}_output",f"{self.prename}_{element}_Ci"),element,self.Pixel_size,self.color_of_heatmap,100,".png")
                                    
                        if self.Ci_bmp_checkbox.isChecked():
                            if self.Ci_auto_checkbox.isChecked():
                                utils.saving_plot_auto(Ci_table,os.path.join(self.Main_Folder_Path,f"{self.folder}_output",f"{self.prename}_{element}_Ci"),element,self.Pixel_size,self.color_of_heatmap,".pdf")
                            else:
                                if self.Ci_mg_checkbox.isChecked():
                                    utils.Ci_saving_plot(Ci_table,os.path.join(self.Main_Folder_Path,f"{self.folder}_output",f"{self.prename}_{element}_Ci"),element,self.Pixel_size,self.color_of_heatmap,1000,".pdf")
                                if self.Ci_ug_checkbox.isChecked():
                                    utils.Ci_saving_plot(Ci_table,os.path.join(self.Main_Folder_Path,f"{self.folder}_output",f"{self.prename}_{element}_Ci"),element,self.Pixel_size,self.color_of_heatmap,1000000,".pdf")
                                if self.Ci_procent_checkbox.isChecked():
                                    utils.Ci_saving_plot(Ci_table,os.path.join(self.Main_Folder_Path,f"{self.folder}_output",f"{self.prename}_{element}_Ci"),element,self.Pixel_size,self.color_of_heatmap,100,".pdf")
                                
                        if self.Ci_tiff_checkbox.isChecked():
                            if self.Ci_auto_checkbox.isChecked():
                                utils.saving_plot_auto(Ci_table,os.path.join(self.Main_Folder_Path,f"{self.folder}_output",f"{self.prename}_{element}_Ci"),element,self.Pixel_size,self.color_of_heatmap,".tiff")
                            else:
                                if self.Ci_mg_checkbox.isChecked():
                                    utils.Ci_saving_plot(Ci_table,os.path.join(self.Main_Folder_Path,f"{self.folder}_output",f"{self.prename}_{element}_Ci"),element,self.Pixel_size,self.color_of_heatmap,1000,".tiff")
                                if self.Ci_ug_checkbox.isChecked():
                                    utils.Ci_saving_plot(Ci_table,os.path.join(self.Main_Folder_Path,f"{self.folder}_output",f"{self.prename}_{element}_Ci"),element,self.Pixel_size,self.color_of_heatmap,1000000,".tiff")
                                if self.Ci_procent_checkbox.isChecked():
                                    utils.Ci_saving_plot(Ci_table,os.path.join(self.Main_Folder_Path,f"{self.folder}_output",f"{self.prename}_{element}_Ci"),element,self.Pixel_size,self.color_of_heatmap,100,".tiff")
                                
                        if self.Ci_dat_checkbox.isChecked():
                            if self.Ci_auto_checkbox.isChecked():
                                utils.saving_plot_auto(Ci_table,os.path.join(self.Main_Folder_Path,f"{self.folder}_output",f"{self.prename}_{element}_Ci"),element,self.Pixel_size,self.color_of_heatmap)
                            else:
                                if self.Ci_mg_checkbox.isChecked():
                                    utils.Ci_saving_dat(Ci_table,os.path.join(self.Main_Folder_Path,f"{self.folder}_output",f"{self.prename}_{element}_Ci"),element,1000)
                                if self.Ci_ug_checkbox.isChecked():
                                    utils.Ci_saving_dat(Ci_table,os.path.join(self.Main_Folder_Path,f"{self.folder}_output",f"{self.prename}_{element}_Ci"),element,1000000)
                                if self.Ci_procent_checkbox.isChecked():
                                    utils.Ci_saving_dat(Ci_table,os.path.join(self.Main_Folder_Path,f"{self.folder}_output",f"{self.prename}_{element}_Ci"),element,100)


                        if self.sample_mass_dat_checkbox.isChecked():
                            if self.sample_mass_g_checkbox.isChecked():
                                utils.SM_saving_dat(sm,os.path.join(self.Main_Folder_Path,f"{self.folder}_output",f"{self.prename}_sm"),1)
                            if self.sample_mass_mg_checkbox.isChecked():
                                utils.SM_saving_dat(sm,os.path.join(self.Main_Folder_Path,f"{self.folder}_output",f"{self.prename}_sm"),1000)
                            if self.sample_mass_ug_checkbox.isChecked():
                                utils.SM_saving_dat(sm,os.path.join(self.Main_Folder_Path,f"{self.folder}_output",f"{self.prename}_sm"),1000000)
                            if self.sample_mass_ng_checkbox.isChecked():
                                utils.SM_saving_dat(sm,os.path.join(self.Main_Folder_Path,f"{self.folder}_output",f"{self.prename}_sm"),1000000000)
                                                
                        if self.sample_mass_png_checkbox.isChecked():
                            if self.sample_mass_g_checkbox.isChecked():
                                utils.SM_saving_plot(sm,os.path.join(self.Main_Folder_Path,f"{self.folder}_output",f"{self.prename}_sm"),self.Pixel_size,self.color_of_heatmap,1,".png")
                            if self.sample_mass_mg_checkbox.isChecked():
                                utils.SM_saving_plot(sm,os.path.join(self.Main_Folder_Path,f"{self.folder}_output",f"{self.prename}_sm"),self.Pixel_size,self.color_of_heatmap,1000,".png")
                            if self.sample_mass_ug_checkbox.isChecked():
                                utils.SM_saving_plot(sm,os.path.join(self.Main_Folder_Path,f"{self.folder}_output",f"{self.prename}_sm"),self.Pixel_size,self.color_of_heatmap,1000000,".png")
                            if self.sample_mass_ng_checkbox.isChecked():
                                utils.SM_saving_plot(sm,os.path.join(self.Main_Folder_Path,f"{self.folder}_output",f"{self.prename}_sm"),self.Pixel_size,self.color_of_heatmap,1000000000,".png")

                        if self.sample_mass_bmp_checkbox.isChecked():
                            if self.sample_mass_g_checkbox.isChecked():
                                utils.SM_saving_plot(sm,os.path.join(self.Main_Folder_Path,f"{self.folder}_output",f"{self.prename}_sm"),self.Pixel_size,self.color_of_heatmap,1,".pdf")
                            if self.sample_mass_mg_checkbox.isChecked():
                                utils.SM_saving_plot(sm,os.path.join(self.Main_Folder_Path,f"{self.folder}_output",f"{self.prename}_sm"),self.Pixel_size,self.color_of_heatmap,1000,".pdf")
                            if self.sample_mass_ug_checkbox.isChecked():
                                utils.SM_saving_plot(sm,os.path.join(self.Main_Folder_Path,f"{self.folder}_output",f"{self.prename}_sm"),self.Pixel_size,self.color_of_heatmap,1000000,".pdf")
                            if self.sample_mass_ng_checkbox.isChecked():
                                utils.SM_saving_plot(sm,os.path.join(self.Main_Folder_Path,f"{self.folder}_output",f"{self.prename}_sm"),self.Pixel_size,self.color_of_heatmap,1000000000,".pdf")
                        
                        if self.sample_mass_tiff_checkbox.isChecked():
                            if self.sample_mass_g_checkbox.isChecked():
                                utils.SM_saving_plot(sm,os.path.join(self.Main_Folder_Path,f"{self.folder}_output",f"{self.prename}_sm"),self.Pixel_size,self.color_of_heatmap,1,".tiff")
                            if self.sample_mass_mg_checkbox.isChecked():
                                utils.SM_saving_plot(sm,os.path.join(self.Main_Folder_Path,f"{self.folder}_output",f"{self.prename}_sm"),self.Pixel_size,self.color_of_heatmap,1000,".tiff")
                            if self.sample_mass_ug_checkbox.isChecked():
                                utils.SM_saving_plot(sm,os.path.join(self.Main_Folder_Path,f"{self.folder}_output",f"{self.prename}_sm"),self.Pixel_size,self.color_of_heatmap,1000000,".tiff")
                            if self.sample_mass_ng_checkbox.isChecked():
                                utils.SM_saving_plot(sm,os.path.join(self.Main_Folder_Path,f"{self.folder}_output",f"{self.prename}_sm"),self.Pixel_size,self.color_of_heatmap,1000000000,".tiff")
         
                    else:
                        continue 
        shutil.rmtree(Path(os.path.join(self.Main_Folder_Path,"temporary")))
        print("Dziękuję za korzystanie z SliceQuant")
        exit()  

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()

# Jednostki Auto dla Ci. Ci>0.005 -> %, Ci<0.005 -> ug/g W UTILSACH!