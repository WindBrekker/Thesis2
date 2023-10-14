import utils
import matplotlib.pyplot as plt
from os.path import exists as file_exists
import os
from pathlib import Path


# root_directory = input("Podaj nazwe folderu glownego: ")
# sample_matrix = input("Podaj nazwe folderu z zawartoscia tkanki")
# scater = input("Podaj nazwe pliku scater ")
# zeropeak = input("Podaj nazwe pliku zeropeak ")
root_directory = "test_folder"
sample_matrix = "sample_matrix"
scater = "scater"
zeropeak = "zeropeak"
element_for_mask = input("Podaj nazwe pierwiastka dla ktorego nalozona zostanie maska ")


for root, directories, files in os.walk(root_directory):
    for directory in directories:
        path = os.path.join(root, directory)
        path = Path("C:\\Users\\wikto\\Thesis")
        file_names = os.listdir(path)
        if file_names:
            first_file = file_names[0]
            prename = first_file.split("__")[0]
            with open(f"{path}\\lambda_Ci_average.txt", "w") as f:
                f.write("")

            # wczytanie pliku z kalibracją pierwiastków
            with open("test_folder\\inputfile.txt", "rt") as elements_file:
                # a dictionary with values of K
                elements_dict = {}
                # a dictionary with values of energies (u_Eeffi)
                energy_elements_dict = {}
                # a dictionary with values of Z-number
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

            with open(f"{path}/{sample_matrix}.txt", "rt") as sample_matrix_file:
                sample_dict = {}
                for line in sample_matrix_file:
                    columns = line.strip().split()
                    element = columns[0]
                    concentration = columns[1]
                    sample_dict[element] = concentration

            # #wczytywanie zeropeak i wyznaczanie livetime
            table_of_zeropeaks = utils.file_to_list(f"{path}/{prename}__{zeropeak}.txt")
            livetime = utils.LT_calc(table_of_zeropeaks)


            utils.output_to_file(livetime, f"{path}/{prename}_livetime_map")

            # wczytywanie mapy fosforu do maski
            table_of_P = utils.file_to_list(f"{path}/{prename}__{element_for_mask}.txt")

            # baza do maski - zerowanie wartości poniżej 10% max wartości l zliczeń forsforu w próbce
            maxoftableP = max([sublist[-1] for sublist in table_of_P])
            # print(maxoftableP)
            procent = 0.1
            mask = [
                [0 for j in range(len(table_of_P[0]))] for i in range(len(table_of_P))
            ]
            for i in range(len(table_of_P)):
                for j in range(len(table_of_P[0])):
                    if table_of_P[i][j] < (procent * maxoftableP):
                        mask[i][j] = 0
                    else:

                        mask[i][j] = 1
            utils.output_to_file(mask, f"{path}/{prename}_mask")

            # tu ogólny kod bez uwzględnienia konkretnego pierwiastka
            def surface_mass_calc(element):
                K_i = float(elements_dict[element])
                K_i = K_i * 1000000000
                counts_data = f"{path}/{prename}__{element}.txt"
                counts_table = utils.file_to_list(counts_data)
                table_of_smi = [
                    [0 for j in range(len(counts_table[0]))]
                    for i in range(len(counts_table))
                ]

                for i in range(len(counts_table)):
                    for j in range(len(counts_table[0])):
                        table_of_smi[i][j] = (
                            ((float(counts_table[i][j]) * float(mask[i][j])))
                            / float(livetime[i][j])
                            / (float(K_i))
                        )  # dzielimy przez 10^9 by zmieni jednostki z cm^2/ug/ms -> cm^2/(g*s) w K_i.
                        # Calosc mamy w g/g
                utils.output_to_file(table_of_smi, f"{path}/{prename}_{element}_smi")

                return table_of_smi

            def Ci_calc(smi_table):
                sm = []
                
                scater_tab = []

                scater_tab = utils.file_to_list(f"{path}/{prename}__{scater}.txt")

                sm_livetime = [
                    [0 for j in range(len(scater_tab[0]))]
                    for i in range(len(scater_tab))
                ]
                for i in range(len(scater_tab)):
                    for j in range(len(scater_tab[0])):
                        sm_livetime[i][j] = float(scater_tab[i][j]) / float(
                            livetime[i][j]
                        )

                sm = utils.SampSM_calc(sm_livetime)
                sm_masked = [[0 for j in range(len(sm[0]))] for i in range(len(sm))]
                for i in range(len(scater_tab)):
                    for j in range(len(scater_tab[0])):
                        sm_masked[i][j] = sm[i][j] * mask[i][j]

                Ci_table = [[0 for j in range(len(sm[0]))] for i in range(len(sm))]
                lambda_factor = [[0 for j in range(len(sm[0]))] for i in range(len(sm))]
                Ci_sum_factor = 0
                lambda_sum_factor = 0
                loop_counts = 0
                utils.output_to_file(sm, f"{path}/{prename}_sm")

                for i in range(len(sm)):
                    for j in range(len(sm[0])):
                        if smi_table[i][j] != 0:
                            lambda_factor[i][j] = utils.lambda_factor(
                                sm[i][j],
                                int(Z_element[element]),
                                float(energy_elements_dict[element]),
                                sample_dict,
                            )
                            lambda_sum_factor += lambda_factor[i][j]
                            loop_counts += 1

                            Ci_table[i][j] = (
                                smi_table[i][j] / sm[i][j] / lambda_factor[i][j]
                            )
                            Ci_sum_factor += Ci_table[i][j]
                        else:
                            continue
                lambda_average_factor = lambda_sum_factor / loop_counts
                Ci_average_factor = Ci_sum_factor / loop_counts

                with open(f"{path}\lambda_Ci_average.txt", "a") as f:
                    f.write(
                        f'element:  {element},  average lambda: {format(lambda_average_factor, ".2e")},    average Ci: {format(Ci_average_factor, ".2e")}, \n'
                    )
                return Ci_table

            for key in Z_element:
                element = key
                if file_exists(f"{path}/{prename}__{element}.txt"):
                    sm_table = surface_mass_calc(element)
                    Ci_table = Ci_calc(sm_table)
                    utils.output_to_file(Ci_table, f"{path}/{prename}_{element}_Ci")

                    plt.imshow(Ci_table, cmap="hot", interpolation="nearest")
                    plt.title(f"{element}_Ci_plot")
                    plt.colorbar()
                    plt.savefig(f"{path}/{element}_Ci_plot.png")
                    # plt.close()
                    plt.open()

                else:
                    continue
                

print("Dziękuję za korzystanie z SliceQuant")


# Button z rozszerzeniem image (czy chcemy heatbara czy nie)
# Dorzuci skale uznajc e jeden px to 100\mu m
