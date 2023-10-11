import utils
import numpy as np
import xraylib as xr
import matplotlib.pyplot as plt
from os.path import exists as file_exists

# wczytanie pliku z kalibracją pierwiastków
with open("Inputs\inputfile.txt", "rt") as elements_file:
    #a dictionary with values of K
    elements_dict = {}
    #a dictionary with values of energies (u_Eeffi)
    energy_elements_dict = {}
    #a dictionary with values of Z-number 
    Z_element = {}
    for line in elements_file:
        columns = line.strip().split()
        element = columns[1]
        k_value = columns[2]
        energy = columns[3]
        Z_number = columns[0]
        elements_dict[element] = k_value
        energy_elements_dict[element] = energy
        Z_element[element] = Z_number
# print(elements_dict)

with open("Inputs\sample_matrix.txt", "rt") as sample_matrix_file:
    sample_dict = {}
    for line in sample_matrix_file:
        columns = line.strip().split()
        element = columns[0]
        concentration = columns[1]
        sample_dict[element] = concentration

# #wczytywanie zeropeak i wyznaczanie livetime
table_of_zeropeaks = utils.file_to_list("Inputs\nodec__zeropeak.txt")
livetime = utils.LT_calc(table_of_zeropeaks)

utils.output_to_file(livetime, "Outputs\livetime")

#wczytywanie mapy fosforu do maski
table_of_P = utils.file_to_list("Inputs\nodec__P.txt")

# baza do maski - zerowanie wartości poniżej 10% max wartości l zliczeń forsforu w próbce
maxoftableP = max([sublist[-1] for sublist in table_of_P])
#print(maxoftableP)
procent = 0.1
mask = [[0 for j in range(len(table_of_P[0]))] for i in range(len(table_of_P))]
for i in range (len(table_of_P)):
    for j in range (len(table_of_P[0])):    
        if table_of_P[i][j] < (procent*maxoftableP):
            mask[i][j] = 0
        else:
            mask[i][j] = 1
utils.output_to_file(mask, "Outputs\mask")

# tu ogólny kod bez uwzględnienia konkretnego pierwiastka
def surface_mass_calc(element):
    K_i = float(elements_dict[element]) 
    K_i = K_i*1000000000
    counts_data = f"Inputs\nodec__{element}.txt"
    counts_table = utils.file_to_list(counts_data)
    table_of_smi = [[0 for j in range(len(counts_table[0]))] for i in range(len(counts_table))]

    for i in range (len(counts_table)):  
        for j in range (len(counts_table[0])):
            table_of_smi[i][j] = (((float(counts_table[i][j])* float(mask[i][j])))/ float(livetime[i][j]) / (float(K_i)))# dzielimy przez 10^9 by zmieni jednostki z cm^2/ug/ms -> cm^2/(g*s) w K_i. 
                                                                                                                         #Calosc mamy w g/g 
    utils.output_to_file(table_of_smi,f"Outputs\{element}_smi")

    return table_of_smi

def Ci_calc(smi_table):
    sm = []

    scater = []
    scater = utils.file_to_list("Inputs\nodec__scater.txt")
    
    sm_livetime = [[0 for j in range(len(scater[0]))] for i in range(len(scater))]
    for i in range(len(scater)):  
        for j in range(len(scater[0])):
            sm_livetime[i][j] = (float(scater[i][j]) / float(livetime[i][j]))
    
    sm = utils.SampSM_calc(sm_livetime)
    sm_masked = [[0 for j in range(len(sm[0]))] for i in range(len(sm))]
    for i in range(len(scater)):  
        for j in range(len(scater[0])):
            sm_masked[i][j] = (sm[i][j]*mask[i][j])
    
    Ci_table = [[0 for j in range(len(sm[0]))] for i in range(len(sm))]
    lambda_factor = [[0 for j in range(len(sm[0]))] for i in range(len(sm))]
    Ci_sum_factor = 0
    lambda_sum_factor = 0
    loop_counts = 0
    utils.output_to_file(sm,"Outputs\sm")

    for i in range (len(sm)):
        for j in range (len(sm[0])):
            if(smi_table[i][j] != 0):
                lambda_factor[i][j] = utils.lambda_factor(sm[i][j],int(Z_element[element]),float(energy_elements_dict[element]),sample_dict)
                lambda_sum_factor += lambda_factor[i][j]
                loop_counts += 1
                # print("Smi = "+str(smi_table[i][j]))
                # print("sm = "+str(sm[i][j]))
                Ci_table[i][j] = (smi_table[i][j] / sm[i][j]/lambda_factor[i][j])
                Ci_sum_factor += Ci_table[i][j]
            else: continue
    lambda_average_factor = lambda_sum_factor/loop_counts
    Ci_average_factor = Ci_sum_factor/loop_counts

    # plt.imshow(lambda_factor,cmap='hot',interpolation='nearest')
    # plt.show()
    # plt.imshow(sm_masked,cmap='hot',interpolation='nearest')
    # plt.show()
    # print("srednia lambda: " + str(lambda_average_factor))
    # print("srednie Ci: " + str(Ci_average_factor))
    return Ci_table



for key in Z_element:
    element = key
    if file_exists(f"Inputs\nodec__{element}.txt"):
        sm_table = surface_mass_calc(element)
        Ci_table = Ci_calc(sm_table)
        utils.output_to_file(Ci_table,f"Outputs\{element}_Ci")

        plt.imshow(Ci_table, cmap='hot',interpolation = 'nearest')
        plt.show()
    else:
        continue    

print("Dziękuję za korzystanie z SliceQuant")



#Wzór 16, dostajemy input składu - lba atomowa/nazwa i ile go jest (Rzowiązanie 1) BIBLIOTEKA XRAYLIB - podaj wsp osłabienia dla energii dla pierwiastka.
# np 3keV, 10keV i 20keV. 
#Napisać funkcję, która będzie wyliczała wypadkowy współczynnik osłabienia 
#ponazywać funkcje normalnie i Ci uwzględnić, że będzoe więcej
#doda kolumne do inputfile w oczekiwaniu na wyniki
