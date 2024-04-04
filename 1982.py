import pandas as pd
from func1982 import f_input
from func1982 import f_standard_deviation

# Getting input from the user
grade, aggregate_type, max_aggregate_size, compacting_factor, quality_control, exposure_condition, sg_cement, sg_ca, sg_fa, sg_water, sa_fa = f_input()

# Target Strength for mix proportioning
compressive_strength = int((grade.upper()).removeprefix("M"))
standard_deviation = f_standard_deviation(
    compressive_strength, quality_control)
target_strength = compressive_strength + 1.65 * standard_deviation

# Selection of Water-Cement Ratio

file_path = 'csv files\curve 1982.csv'


df = pd.read_csv(file_path)
# Assuming 'y' and 'x' are the column names in your Excel sheet
# Value in y column for which you want to find the nearest value in 'y'

# Check if the exact value exists
if target_strength in df['y'].values:
    nearest_value_index = df.loc[df['y'] == target_strength].index[0]
    nearest_value_in_y = df.iloc[nearest_value_index]
    nearest_value_x = nearest_value_in_y['x']
    adopted_wc_ratio = nearest_value_x
    '''print("Exact value found in column 'y':", nearest_value_in_y['y'])
    print("Corresponding value in column 'x':", adopted_wc_ratio)'''
else:
    # Find the nearest value in column 'y'
    nearest_value_index = (df['y'] - target_strength).abs().argsort()[0]
    nearest_value_in_y = df.iloc[nearest_value_index]
    nearest_value_x = nearest_value_in_y['x']
    '''print("Nearest value in column 'y':", nearest_value_in_y['y'])
    print("Corresponding value in column 'x':", nearest_value_x)'''

    # Find the next nearest value in column 'y'
    next_nearest_index = (df['y'] - target_strength).abs().argsort()[1]
    next_nearest_value_in_y = df.iloc[next_nearest_index]
    next_nearest_value_x = next_nearest_value_in_y['x']
    '''print("Next nearest value in column 'y':", next_nearest_value_in_y['y'])
    print("Corresponding value in column 'x':", next_nearest_value_x)'''

    def interpolation(d, y):
        output = d[0][1] + (y - d[0][0]) * ((d[1][1] - d[0][1]) /
                                            (d[1][0] - d[0][0]))

        return output

    # Driver Code
    data = [[next_nearest_value_in_y, next_nearest_value_x],
            [nearest_value_in_y, nearest_value_x]]

    # Finding the interpolation
    print("Interpolated value ".format(target_strength),
          interpolation(data, target_strength))
    print(interpolation(data, target_strength).y)
    adopted_wc_ratio = round((interpolation(data, target_strength).y),1)


# ---------- Selection of Water content----------------------------------------------------------
change_water_content_a_t = 0
change_vol_fa_a_t = 0

if compressive_strength <= 35 and sa_fa == 2 and adopted_wc_ratio == 0.6 and compacting_factor == 0.8 and aggregate_type == 1:
    if max_aggregate_size == 10:
        max_water_content = 208
        vol_fa = 40
    elif max_aggregate_size == 20:
        max_water_content = 186
        vol_fa = 35
    elif max_aggregate_size == 40:
        max_water_content = 165
        vol_fa = 30
    else:
        print("Enter Valid Nominal Maximum Size of Aggregate")
elif compressive_strength > 35 and sa_fa == 2 and adopted_wc_ratio == 0.35 and compacting_factor == 0.8 and aggregate_type == 1:
    if max_aggregate_size == 10:
        max_water_content = 200
        vol_fa = 28
    elif max_aggregate_size == 20:
        max_water_content = 180
        vol_fa = 25
    else:
        print("Enter Valid Nominal Maximum Size of Aggregate")
else:
    if sa_fa in [1, 3, 4]:
        change_water_content_sa = 0
        if sa_fa == 1:
            change_vol_fa_sa = 1.5
        elif sa_fa == 3:
            change_vol_fa_sa = -1.5
        elif sa_fa == 4:
            change_vol_fa_sa = -3.0
    if compacting_factor < (0.8) or compacting_factor > (0.8):
        change_water_content_c_f = ((compacting_factor-0.8)/0.1)*3
        change_vol_fa_c_f = 0
    if aggregate_type == 2:
        change_water_content_a_t = -15
        change_vol_fa_a_t = -7
    if compressive_strength <= 35:
        change_water_content_c_s = 0
        change_vol_fa_c_s = ((adopted_wc_ratio-0.6)/0.05)*1
    elif compressive_strength > 35:
        change_water_content_c_s = ((adopted_wc_ratio-0.35)/0.05)*1
        change_vol_fa_c_s = 0

    if compressive_strength <= 35:
        if max_aggregate_size == 10:
            max_water_content = 208
            vol_fa = 40
        elif max_aggregate_size == 20:
            max_water_content = 186
            vol_fa = 35
        elif max_aggregate_size == 40:
            max_water_content = 165
            vol_fa = 30
        else:
            print("Enter Valid Nominal Maximum Size of Aggregate")
    elif compressive_strength > 35:
        if max_aggregate_size == 10:
            max_water_content = 200
            vol_fa = 28
        elif max_aggregate_size == 20:
            max_water_content = 180
            vol_fa = 25
        else:
            print("Enter Valid Nominal Maximum Size of Aggregate")


total_change_water_content = change_water_content_sa + \
    change_water_content_c_f + change_water_content_c_s
total_change_vol_fa = change_vol_fa_sa + \
    change_vol_fa_c_f + change_vol_fa_c_s + change_vol_fa_a_t

arrived_water_content = round((max_water_content +
                              max_water_content*(total_change_water_content/100) +
                              change_water_content_a_t), 2)
corrected_vol_fa = (vol_fa + total_change_vol_fa)/100
corrected_vol_ca = 1 - corrected_vol_fa

# ----------------- Calculation of cement content---------------------------------------------------
cement_content = round(arrived_water_content/adopted_wc_ratio)

# ---------------- Proportion of volume of Coarse Aggregate and fine Aggregate------------------------
if max_aggregate_size == 10:
    vol_entrapped_air = 0.03
elif max_aggregate_size == 20:
    vol_entrapped_air = 0.02
elif max_aggregate_size == 40:
    vol_entrapped_air = 0.01

mass_fa = round((((1-vol_entrapped_air)*1000) - arrived_water_content -
                 (cement_content/sg_cement)) * (corrected_vol_fa*sg_fa))

mass_ca = round((((1-vol_entrapped_air)*1000) - arrived_water_content -
                 (cement_content/sg_cement)) * (corrected_vol_ca*sg_ca))

# -------------- Answers--------------------------------------------------------------------------
print("Mix Proportions are:\n")
print(f'Cement = {cement_content} kg/m3')
print(f'Water = {arrived_water_content} kg/m3')
print(f'Fine Aggregate = {mass_fa} kg/m3')
print(f'Coarse Aggregate = {mass_ca} kg/m3')
print(f'Water Cement Ratio = {adopted_wc_ratio}')
print(
    f'Proportion = {cement_content/cement_content}:{mass_fa/cement_content}:{mass_ca/cement_content}')
