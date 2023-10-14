import numpy as np
import xraylib as xr
import math


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

def LT_calc(input):
#zeropeak
    output = []
    for i in range (len(input)):
        output.append([(((0.05* float(input[i][j]) - 0.893)/1000)) for j in range(len(input[i]))])
    return output

def SampSM_calc(input):
#scatter
    output = []
    for i in range (len(input)):
        output.append([(((8.07514 * float(input[i][j])) -1537.368)/1000000) for j in range(len(input[i]))])
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
        return u_E
#Machnac petle dla n pierwiastkow (zczytanych z pliku) z ta funkcja 

#poprawka na probke posrednia
def lambda_factor(rho_D,Z,Eeffi,sample_dict):
    phi_in = math.radians(50)
    phi_out = math.radians(50)
    
    Eijk = xr.LineEnergy(Z,xr.KA1_LINE)
    u_Eijk = absorption_coefficient(sample_dict,Eijk)
    u_Eeffi = absorption_coefficient(sample_dict,Eeffi)
    #wczytujemy Eeffi z pliczku input i Eijk z funcji xr.LineEnergy(Z,xr.KA1_LINE)
    
    denominator = rho_D*((u_Eeffi/(math.sin(phi_in)))+(u_Eijk/(math.sin(phi_out))))
    numerator = 1-(math.exp(-1*(denominator)))
    correction_factror = numerator/denominator

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







#print(energy)
# list_one = file_to_list(input)
# list_two = direct_factor(list_one)
# print(list_two)
# print(type(list_two))
# print(type(list_two[0][0]))
# print(type(list_two[0]))
