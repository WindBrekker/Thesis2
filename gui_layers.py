import sys
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
    #input_layout
        main_folder_layout = QHBoxLayout()
        pixel_size_layout = QHBoxLayout()
        text_layout = QHBoxLayout()

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
        
        Input_layout.addLayout(main_folder_layout,4)
        Input_layout.addLayout(text_layout,3)
        Input_layout.addLayout(pixel_size_layout,3)
        

        #Widgets
        #QLabel
        self.Treshold_txt_label = QLabel("Treshold = ",self)
        self.Treshold_unit_label = QLabel("%",self)
        self.pixel_size_txt_label = QLabel("Pixel size = ",self)
        self.pixel_size_unit_label = QLabel("[um]",self)
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
        self.names_inof_label = QLabel("(optional)Enter used nomenclature",self)

  

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
        main_folder_layout.addWidget(self.Main_folder)
        text_layout.addWidget(self.Treshold_txt_label)
        text_layout.addWidget(self.Treshold)
        text_layout.addWidget(self.Treshold_unit_label)
        pixel_size_layout.addWidget(self.pixel_size_txt_label)
        pixel_size_layout.addWidget(self.Pixel)
        pixel_size_layout.addWidget(self.pixel_size_unit_label)

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
        self.use_for_mask_button.setEnabled(True)
        self.next_element_button.setEnabled(True)
        self.previous_element_button.setEnabled(True)
        self.Prefere_folder.clear() 
        self.Prefere_folder.setPlaceholderText("Choose pattern folder")

        #setting custom names in folder:
        self.Main_Folder_Path = str(self.Main_folder.text())
        self.Pixel_size = str(self.Pixel.text())
        self.inputfile = str(self.Inputfile.text())
        self.zeropeak = str(self.Zeropeak.text())
        self.scater = str(self.Scater.text())
        self.Sample_Matrix = str(self.SampMatrix.text())
        self.treshold = str(self.Treshold.text())

        self.element_for_mask = str(self.Mask_value_label.text())
        if self.Pixel_size == "":
            self.Pixel_size = 1000
        if self.inputfile == "":
            self.inputfile = "inputfile"
        if self.zeropeak == "":
            self.zeropeak = "zeropeak"
        if self.scater == "":
            self.scater = "scater"
        if self.Sample_Matrix== "":
            self.Sample_Matrix = "sample_matrix"
        if self.treshold == "":
            self.treshold = 10
            
        #print(self.Pixel_size,self.inputfile, self.zeropeak, self.scater, self.Sample_Matrix)
                
        #finding and listing only subfolders (for excluding inpufile)
        path = Path(self.Main_Folder_Path)
        path_insides = os.listdir(path)
        self.folders_names = [file for file in path_insides if os.path.isdir(os.path.join(self.Main_Folder_Path,file)) ]
        self.Prefere_folder.addItems(self.folders_names)
        self.Prefere_folder.setEnabled(True)
        
    def prefered_folder_selected(self):
        self.current_index = 0
        #set the prefered folder as a variable
        self.chosen_folder = self.Prefere_folder.currentText()
        
        #listing the elements inside
        self.elements_nodec = []
        path = Path(os.path.join(self.Main_Folder_Path, self.chosen_folder))
        path_insides = os.listdir(path)
        for file in path_insides:
            if file.split("__")[1] != f"{self.scater}.txt" and file.split("__")[1] != f"{self.zeropeak}.txt":
                self.elements_nodec.append(file.split("__")[1].split(".")[0])
        
        self.element_name_label.setText(self.elements_nodec[0])
        
        
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
        first_file = file_names[0]
        self.prename = first_file.split("__")[0]
        
        #unpacking sample matrix
        with open(Path(os.path.join(self.Main_Folder_Path,f"{self.Sample_Matrix}.txt")),"rt") as sample_matrix_file:  
            self.sample_dict = {}
            for line in sample_matrix_file:
                columns = line.strip().split()
                element = columns[0]
                concentration = columns[1]
                self.sample_dict[element] = concentration
        
        #calculating livetime with zeropeak
        table_of_zeropeaks = utils.file_to_list(Path(os.path.join(self.Main_Folder_Path,self.chosen_folder,f"{self.prename}__{self.zeropeak}.txt")))
        self.livetime = utils.LT_calc(table_of_zeropeaks) 
        
        if not Path(os.path.join(self.Main_Folder_Path,f"{self.chosen_folder}_output")).exists():
            Path(os.path.join(self.Main_Folder_Path,f"{self.chosen_folder}_output")).mkdir()
        utils.output_to_file(self.livetime, Path(os.path.join(self.Main_Folder_Path,f"{self.chosen_folder}_output",f"{self.prename}_livetime_map"))) 
        self.mask_map = utils.mask_creating(self.elements_nodec[0],self.Main_Folder_Path,self.chosen_folder,self.prename,self.treshold)
        self.sample_pixmap = QPixmap(os.path.join(self.Main_Folder_Path,f"{self.chosen_folder}_output","mask.png"))
        self.sample_picture_label.setPixmap(self.sample_pixmap)
               
        self.sample_pixmap2 = QPixmap(os.path.join(self.Main_Folder_Path,f"{self.chosen_folder}_output","mask_noc.png"))
        self.sample_picture_label2.setPixmap(self.sample_pixmap2)

    def Previous_element(self):
        if self.current_index > 0:
            self.current_index -= 1
            self.element_name_label.setText(self.elements_nodec[self.current_index])
            
        utils.mask_creating(self.elements_nodec[self.current_index],self.Main_Folder_Path,self.chosen_folder,self.prename,self.treshold)
        self.sample_pixmap = QPixmap(os.path.join(self.Main_Folder_Path,f"{self.chosen_folder}_output","mask.png"))
        self.sample_picture_label.setPixmap(self.sample_pixmap)
               
        self.sample_pixmap2 = QPixmap(os.path.join(self.Main_Folder_Path,f"{self.chosen_folder}_output","mask_noc.png"))
        self.sample_picture_label2.setPixmap(self.sample_pixmap2)
        
    def Next_element(self):
        if self.current_index < len(self.elements_nodec) - 1:
            self.current_index += 1
            self.element_name_label.setText(self.elements_nodec[self.current_index])
        utils.mask_creating(self.elements_nodec[self.current_index],self.Main_Folder_Path,self.chosen_folder,self.prename,self.treshold)
        self.sample_pixmap = QPixmap(os.path.join(self.Main_Folder_Path,f"{self.chosen_folder}_output","mask.png"))
        self.sample_picture_label.setPixmap(self.sample_pixmap)
               
        self.sample_pixmap2 = QPixmap(os.path.join(self.Main_Folder_Path,f"{self.chosen_folder}_output","mask_noc.png"))
        self.sample_picture_label2.setPixmap(self.sample_pixmap2)
        
    def ChooseMask(self):
        self.Mask_value_label.setText(str(self.element_name_label.text()))
        self.quantify_button.setEnabled(True)

    def Quantify(self):
        for f in self.folders_names:
            self.chosen_folder = f
            if not Path(os.path.join(self.Main_Folder_Path,f"{self.chosen_folder}_output")).exists():
                Path(os.path.join(self.Main_Folder_Path,f"{self.chosen_folder}_output")).mkdir()
            for key in self.Z_element:
                    element = key
                    if file_exists(os.path.join(self.Main_Folder_Path,self.chosen_folder,  f"{self.prename}__{element}.txt")):
                        K_i = float(self.elements_dict[element])
                        K_i = K_i * 1000000000
                        counts_data = os.path.join(self.Main_Folder_Path, self.chosen_folder,f"{self.prename}__{element}.txt")
                        counts_table = utils.file_to_list(counts_data)
                        table_of_smi = [
                            [0 for j in range(len(counts_table[0]))]
                            for i in range(len(counts_table))
                        ]

                        for i in range(len(counts_table)):
                            for j in range(len(counts_table[0])):
                                table_of_smi[i][j] = (
                                    ((float(counts_table[i][j]) * float(self.mask_map[i][j])))
                                    / float(self.livetime[i][j])
                                    / (float(K_i))
                                ) # dzielimy przez 10^9 by zmieni jednostki z cm^2/ug/ms -> cm^2/(g*s) w K_i.
                                # Calosc mamy w g/g
                        utils.output_to_file(table_of_smi, os.path.join(self.Main_Folder_Path,f"{self.chosen_folder}_output",f"{self.prename}_{element}_smi"))                        
                        sm = []
                        
                        scater_tab = []

                        scater_tab = utils.file_to_list(os.path.join(self.Main_Folder_Path,self.chosen_folder,f"{self.prename}__{self.scater}.txt"))

                        sm_livetime = [[0 for j in range(len(scater_tab[0]))]for i in range(len(scater_tab))]
                        
                        for i in range(len(scater_tab)):
                            for j in range(len(scater_tab[0])):
                                sm_livetime[i][j] = float(scater_tab[i][j]) / float(self.livetime[i][j])

                        sm = utils.SampSM_calc(sm_livetime)
                        sm_masked = [[0 for j in range(len(sm[0]))] for i in range(len(sm))]
                        for i in range(len(scater_tab)):
                            for j in range(len(scater_tab[0])):
                                sm_masked[i][j] = sm[i][j] * self.mask_map[i][j]

                        Ci_table = [[0 for j in range(len(sm[0]))] for i in range(len(sm))]
                        lambda_factor = [[0 for j in range(len(sm[0]))] for i in range(len(sm))]
                        Ci_sum_factor = 0
                        lambda_sum_factor = 0
                        loop_counts = 0
                        utils.output_to_file(sm,os.path.join(self.Main_Folder_Path,f"{self.chosen_folder}_output",f"{self.prename}_sm"))

                        for i in range(len(sm)):
                            for j in range(len(sm[0])):
                                if table_of_smi[i][j] != 0:
                                    lambda_factor[i][j] = utils.lambda_factor(
                                        sm[i][j],
                                        int(self.Z_element[element]),
                                        float(self.energy_elements_dict[element]),
                                        self.sample_dict
                                    )
                                    lambda_sum_factor += lambda_factor[i][j]
                                    loop_counts += 1

                                    Ci_table[i][j] = (
                                        table_of_smi[i][j] / sm[i][j] / lambda_factor[i][j]
                                    )
                                    Ci_sum_factor += Ci_table[i][j]
                                else:
                                    continue
                        lambda_average_factor = lambda_sum_factor / loop_counts
                        Ci_average_factor = Ci_sum_factor / loop_counts

                        with open( os.path.join(self.Main_Folder_Path,f"{self.chosen_folder}_output", f"lambda_Ci_average.txt"), "a") as f:
                            f.write(
                                f'element:  {element},  average lambda: {format(lambda_average_factor, ".2e")},    average Ci: {format(Ci_average_factor, ".2e")}, \n'
                            )                        
                        
                        utils.output_to_file(Ci_table, os.path.join(self.Main_Folder_Path,f"{self.chosen_folder}_output",f"{self.prename}_{element}_smi"))
                        Ci_table = np.array(Ci_table)
                        width_um = Ci_table.shape[1] * self.Pixel_size
                        height_um = Ci_table.shape[0] * self.Pixel_size
                        fig, ax = plt.subplots(figsize=(width_um / 100, height_um / 100))
                        extent = [0, width_um, 0, height_um]

                        custom_cmap = plt.get_cmap('viridis')
                        custom_cmap = ListedColormap(custom_cmap(np.linspace(0.2, 1, 256)))
                        plt.imshow(Ci_table, extent=extent, cmap=custom_cmap, interpolation="nearest")
                        ax.set_aspect('equal')
                        plt.title(f"{element}_Ci_plot")
                        plt.xlabel('X (um)')
                        plt.ylabel('Y (um)')
                        plt.colorbar()
                        plt.savefig(os.path.join(self.Main_Folder_Path,f"{self.chosen_folder}_output",f"{self.prename}_{element}_Ci."))
                        plt.close()
    
                    else:
                        continue
                                    

        print("Dziękuję za korzystanie z SliceQuant")
        exit()          
        
    def Confirmed_saving(self):
        self.saving_button.setEnabled(True)
        self.saving_Ci = str(self.Ci_combobox.currentText())
        self.saving_sm =  str(self.SM_combobox.currentText())
        self.saving_lambda = str(self.Lambda_combobox.currentText())
        self.saving_livetime = str(self.Livetime_combobox.currentText())      
  
    def Saving(self):
        print("Saved")


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()


# prename oddzielony JEDNĄ LUB WIELOPMA podłogami 
# scater inputfile
# scalebar -> jeśli sie uda
# colorbar i nowy kolorek.
# ajust pixel size to plt scale 


