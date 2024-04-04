# --------------Concrete mix design using python of IS 2009---------------------------------------
import math
from func2009 import f_standard_deviation
from func2009 import f_vol_ca
from func2009 import f_input
from func2009 import f_table_5

# ----------Getting input from the user---------------------------------------------------------------
[grade, max_aggregate_size, slump, concrete_type, exposure_condition, concrete_placing,
    aggregate_type, max_cement_content, chemical_admixture, sg_chemical_admixture, percent_chemical_admixture, sg_cement, mineral_admixture, sg_mineral_admixture, percent_mineral_admixture, sg_ca, sg_fa, sg_water, sa_ca] = f_input()

# -----Target Strength for mix proportioning------------------------------------------------
compressive_strength = int((grade.upper()).removeprefix("M"))
standard_deviation = f_standard_deviation(compressive_strength)
target_strength = compressive_strength + 1.65*standard_deviation

# ------Selection of Water-Cement Ratio-----------------------------------------------------
min_cement_content, max_wc_ratio = f_table_5(concrete_type, exposure_condition)
adopted_wc_ratio = max_wc_ratio - 0.05

# ---------- Selection of Water content----------------------------------------------------------
if max_aggregate_size == 10:
    max_water_content = 208
elif max_aggregate_size == 20:
    max_water_content = 186
elif max_aggregate_size == 40:
    max_water_content = 165
else:
    print("Enter Valid Nominal Maximum Size of Aggregate")

if aggregate_type == 1:
    max_water_content = max_water_content
elif aggregate_type == 2:
    max_water_content = max_water_content - 10
elif aggregate_type == 3:
    max_water_content = max_water_content - 15
elif aggregate_type == 4:
    max_water_content = max_water_content - 20
else:
    print("Enter Valid Aggregate type")

if slump > 50:
    slumpx = max_water_content + \
        round(((math.floor((slump - 50)/25))*3*max_water_content)/100)
else:
    slumpx = max_water_content

if chemical_admixture == 1:
    arrived_water_content = math.ceil(
        ((100 - percent_chemical_admixture)/100)*slumpx)
elif chemical_admixture == 2:
    arrived_water_content = math.ceil(slumpx)
else:
    print("Enter Valid option")

# ----------------- Calculation of cement content---------------------------------------------------
cement_content = arrived_water_content/adopted_wc_ratio

if cement_content > min_cement_content:
    if cement_content < max_cement_content:
        adopted_cement_content = cement_content
    else:
        adopted_cement_content = max_cement_content
else:
    adopted_cement_content = min_cement_content


if mineral_admixture == 1:
    cementatious_material = adopted_cement_content*1.1
    flyash_content = round(
        (cementatious_material * (percent_mineral_admixture/100)), 3)
    adopted_cement_content = cementatious_material - flyash_content
elif mineral_admixture == 2:
    ggbs_content = round((adopted_cement_content*0.4), 3)
    adopted_cement_content = adopted_cement_content - ggbs_content
elif mineral_admixture == 3:
    adopted_cement_content = math.ceil(adopted_cement_content)

if mineral_admixture in [1, 2]:
    cementatious_material = cementatious_material
else:
    cementatious_material = adopted_cement_content

free_wcementatious_ratio = round(
    arrived_water_content/cementatious_material, 3)
# ---------------- Proportion of volume of Coarse Aggregate and fine Aggregate------------------------
vol_ca = f_vol_ca(sa_ca, max_aggregate_size)

if adopted_wc_ratio < 0.50:
    c_vol_ca = (round((0.50 - adopted_wc_ratio)/0.05))*0.01 + vol_ca
else:
    c_vol_ca = vol_ca - (round((adopted_wc_ratio - 0.5)/0.05))*0.01


if concrete_placing == 1:
    corrected_vol_ca = c_vol_ca * 0.9
elif concrete_placing == 2:
    corrected_vol_ca = c_vol_ca
else:
    print("Enter the valid option for method of concrete placing")

vol_fa = 1-corrected_vol_ca

# ----------- Mix Calculations-------------------------------------------------------------------
vol_concrete = 1
vol_entraped_air = 0.01
vol_cement = round((adopted_cement_content/(sg_cement*1000)), 3)

if mineral_admixture == 1:
    vol_flyash = round((flyash_content/(sg_mineral_admixture*1000)), 3)
elif mineral_admixture == 2:
    vol_ggbs = round((ggbs_content/(sg_mineral_admixture*1000)), 3)


vol_water = round((arrived_water_content/(sg_water*1000)), 3)
if chemical_admixture == 1:
    mass_chemical_admixture = round(0.02*cementatious_material, 3)
    vol_chemical_admixture = round(
        (mass_chemical_admixture/(sg_chemical_admixture*1000)), 3)
else:
    vol_chemical_admixture = 0

if mineral_admixture == 1:
    vol_all_aggregate = round((
        (vol_concrete-vol_entraped_air) - (vol_cement+vol_flyash+vol_water+vol_chemical_admixture)), 3)
elif mineral_admixture == 2:
    vol_all_aggregate = round((
        (vol_concrete-vol_entraped_air) - (vol_cement+vol_ggbs+vol_water+vol_chemical_admixture)), 3)
elif mineral_admixture == 3:
    vol_all_aggregate = round((
        (vol_concrete-vol_entraped_air) - (vol_cement+vol_water+vol_chemical_admixture)), 3)

mass_ca = math.ceil(vol_all_aggregate * corrected_vol_ca * sg_ca*1000)
mass_fa = math.ceil(vol_all_aggregate * vol_fa * sg_fa*1000)
adopted_cement_content = math.ceil(adopted_cement_content)
fa_proportion = round(mass_fa/adopted_cement_content, 3)
ca_proportion = round(mass_ca/adopted_cement_content, 3)

# -------------- Answers--------------------------------------------------------------------------
print("Mix Proportions are:\n")
print(f'Cement = {adopted_cement_content} kg/m3')
print(f'Water = {arrived_water_content} kg/m3')
print(f'Fine Aggregate = {mass_fa} kg/m3')
print(f'Coarse Aggregate = {mass_ca} kg/m3')
if mineral_admixture == 1:
    print(f'Fly Ash = {flyash_content} kg/m3')
elif mineral_admixture == 2:
    print(f'GGBS = {ggbs_content} kg/m3')

if chemical_admixture == 1:
    print(f'Chemical Admixture = {mass_chemical_admixture} kg/m3')
print(f'Water-Cementitious Ratio = {free_wcementatious_ratio}')
print(
    f'Proportion = {adopted_cement_content/adopted_cement_content}:{fa_proportion}:{ca_proportion}')
