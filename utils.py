import numpy as np
import xraylib as xr
import os
import math
import matplotlib.pyplot as plt

def file_to_list(input):
    try:
        converted_list = np.loadtxt(input,delimiter=',')
        # print(converted_list)
        # print(type(converted_list[0]))
        # print(type(converted_list[0][0]))
        return converted_list
    except:
        print("Couldn't find data")
        return None

def LT_calc(input,a,b):
#zeropeak

    output = []
    for i in range (len(input)):
        output.append([(((float(a)* float(input[i][j]) + float(b)))) for j in range(len(input[i]))]) #Livetime [s]  
    return output

def SampSM_calc(input,a,b):
#scatter

    output = []
    for i in range (len(input)):
        output.append([(((float(a) * float(input[i][j])) + float(b))) for j in range(len(input[i]))]) #g/cm^2
    return output

def output_to_file(input, output):
    # open file in write mode
    with open(f"{output}.txt", "w") as f:
        # loop through 2D list
        for row in input:
            formatted_row = [format('{:.2e}'.format(x)) for x in row]
            # write formatted row to file, separated by commas and ending with newline character
            f.write(','.join(formatted_row) + '\n')

def absorption_coefficient(sample_dict,Ee):
        u_E = 0
        for key in sample_dict:
            ui_E = xr.CS_Total_CP(key,Ee)
            u_E += ui_E*float(sample_dict[key])
        return (u_E) #jednostka cm^2/g

def lambda_factor(rho_D,Z,Eeffi,sample_dict):
    
    phi_in = math.radians(50)
    phi_out = math.radians(50)
    
    Eijk = xr.LineEnergy(Z,xr.KA1_LINE)
    u_Eijk = absorption_coefficient(sample_dict,Eijk)
    u_Eeffi = absorption_coefficient(sample_dict,Eeffi)
    #wczytujemy Eeffi z pliczku input i Eijk z funcji xr.LineEnergy(Z,xr.KA1_LINE)
    
    denominator = rho_D*((u_Eeffi/(math.sin(phi_in)))+(u_Eijk/(math.sin(phi_out))))
    numerator = 1-(math.exp(-1*(denominator)))
    correction_factror = denominator/numerator

    # print("u_Eijk = "+str(u_Eijk))
    # print("eijjk" +str(Eijk))
    # print("u_Eeffi = "+str(u_Eeffi))
    # print("mianownik = "+str(denominator))
    # print("uamek z eeffi"+str(u_Eeffi/(math.sin(phi_in))))
    # print("uamek z eijk"+str(u_Eijk/(math.sin(phi_out))))
    # print("rho_D"+str(rho_D))
    # print("sin = " +str(math.sin(phi_in)))
    # print("licznik = "+str(numerator))



    return correction_factror

def mask_creating(element,Path, folder, prename,treshold,color):
    # wczytywanie mapy do maski
        element_for_mask = element
        file_path = os.path.join(Path, folder, f"{prename}__{element_for_mask}.txt")
        table_of_mask = file_to_list(file_path)        
    # baza do maski - zerowanie wartości poniżej 10% max wartości l zliczeń pierwiastka maski w próbce
        maxof_masktable = max([sublist[-1] for sublist in table_of_mask])
        # print(maxof_masktable)
        procent = (float(treshold)/100)
        mask = [
            [0 for j in range(len(table_of_mask[0]))] for i in range(len(table_of_mask))
        ]
        for i in range(len(table_of_mask)):
            for j in range(len(table_of_mask[0])):
                if table_of_mask[i][j] < (procent * maxof_masktable):
                    mask[i][j] = 0  
                else:
                    mask[i][j] = 1
        output_to_file(mask, os.path.join(Path,f"{folder}_output", f"{prename}_mask"))           
        
        
        plt.imshow(mask, cmap=color, interpolation="nearest")
        plt.title("Mask heatmap")
        plt.savefig(os.path.join(Path,f"{folder}_output","mask.png"))
        plt.close()
        plt.imshow(table_of_mask, cmap=color, interpolation="nearest")
        plt.title("Mask number of counts")
        plt.colorbar()
        plt.savefig(os.path.join(Path,f"{folder}_output","mask_noc.png"))
        plt.close()
        return mask

def Ci_saving_dat(input,path,element,size):
    if size == 100:
        unit = "_percent"
    if size == 1000:
        unit = "_mg_g"
    if size == 1000000:
        unit = "_ug_g"
    
    
    Ci_table = np.array(input)
    
    Ci_table = [[Ci_table[i][j] * size for j in range(len(Ci_table[0]))] for i in range(len(Ci_table))]
    
    output_to_file(Ci_table,f"{path}{unit}")   
    
def SMi_saving_dat(input,path,element,size):
    if size == 1000:
        unit = "_mg_g"
    if size == 1000000:
        unit = "_ug_g"
    if size == 1:
        unit = "_g_g"
    if size == 1000000000:
        unit = "_ng_g"
    
    
    SMi_table = np.array(input)
    
    SMi_table = [[SMi_table[i][j] * size for j in range(len(SMi_table[0]))] for i in range(len(SMi_table))]
    
    output_to_file(SMi_table,f"{path}{unit}")  
    
def SM_saving_dat(input,path,size):
    if size == 1000:
        unit = "_mg_g"
    if size == 1000000:
        unit = "_ug_g"
    if size == 1:
        unit = "_g_g"
    if size == 1000000000:
        unit = "_ng_g"
    
    
    SM_table = np.array(input)
    
    SM_table = [[SM_table[i][j] * size for j in range(len(SM_table[0]))] for i in range(len(SM_table))]
    
    output_to_file(SM_table,f"{path}{unit}")  

def Ci_saving_plot(input,path,element,pixel_size,color,size,extention):
    if size == 100:
        unit = "_procent"
    if size == 1000:
        unit = "_mg_g"
    if size == 1000000:
        unit = "_ug_g"
    
    Ci_table = np.array(input)
    width_um = Ci_table.shape[1]
    height_um = Ci_table.shape[0]
    plt.xlim(0, (width_um * float(pixel_size)/1000))
    plt.ylim((height_um * float(pixel_size)/1000),0)
    Ci_table = [[Ci_table[i][j] * size for j in range(len(Ci_table[0]))] for i in range(len(Ci_table))]
    plt.imshow(Ci_table, cmap=color, interpolation="nearest")
    plt.title(f"Concentration map of {element} {unit}")
    plt.xlabel('X (mm)')
    plt.ylabel('Y (mm)')
    plt.colorbar()
    plt.savefig(f"{path}{unit}{extention}")
    plt.close()
    
def SMi_saving_plot(input,path,element,pixel_size,color,size,extention):
    if size == 1000:
        unit = "_mg_g"
    if size == 1000000:
        unit = "_ug_g"
    if size == 1:
        unit = "_g_g"
    if size == 1000000000:
        unit = "_ng_g"
    
    
    SMi_table = np.array(input)
    width_um = SMi_table.shape[1]
    height_um = SMi_table.shape[0]
    plt.xlim(0, (width_um * float(pixel_size)/1000))
    plt.ylim((height_um * float(pixel_size)/1000),0)
    SMi_table = [[SMi_table[i][j] * size for j in range(len(SMi_table[0]))] for i in range(len(SMi_table))]
    plt.imshow(SMi_table, cmap=color, interpolation="nearest")
    plt.title(f"Mass map of element: {element} {unit}")
    plt.xlabel('X (mm)')
    plt.ylabel('Y (mm)')
    plt.colorbar()
    plt.savefig(f"{path}{unit}{extention}")
    plt.close()
    
def SM_saving_plot(input,path,pixel_size,color,size,extention):
    if size == 1000:
        unit = "_mg_g"
    if size == 1000000:
        unit = "_ug_g"
    if size == 1:
        unit = "_g_g"
    if size == 1000000000:
        unit = "_ng_g"
    
    
    SM_table = np.array(input)
    width_um = SM_table.shape[1]
    height_um = SM_table.shape[0]
    plt.xlim(0, (width_um * float(pixel_size)/1000))
    plt.ylim((height_um * float(pixel_size)/1000),0)
    SM_table = [[SM_table[i][j] * size for j in range(len(SM_table[0]))] for i in range(len(SM_table))]
    plt.imshow(SM_table, cmap=color, interpolation="nearest")
    plt.title(f"Sample mass map {unit}")
    plt.xlabel('X (mm)')
    plt.ylabel('Y (mm)')
    plt.colorbar()
    plt.savefig(f"{path}{unit}{extention}")
    plt.close()