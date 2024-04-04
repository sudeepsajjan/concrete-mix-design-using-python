def f_input():
    grade = input("Enter the Grade of concrete to be designed(ex:M25) : ")
    cement_type = int(input(
        "Enter Cement type option : \n1. OPC 33 grade \n2.OPC 43 grade \n3. OPC 53 grade \n4. PPC/PSC \n"))
    max_aggregate_size = int(
        input("Enter Valid Nominal Maximum Size of Aggregate(10mm,20mm,40mm) :"))
    # max_wc_ratio = float(input("Enter Maximum Water Cement Ratio: "))
    slump = int(input("Enter workability(slump) in mm:"))
    # min_cement_content = int(input("Enter the minimum cement content(kg/m3): "))
    concrete_type = int(input(
        "Enter Concrete type option : \n1. Plane Concrete \n2.Reinforced Concrete \n"))
    exposure_condition = int(input(
        "Enter Exposure condition option: \n1. Mild \n2.Moderate \n3.Severe \n4.Very Severe \n5.Extreme \n"))
    concrete_placing = int(input(
        "Enter Concrete placing option : \n1. Pumping \n2.Non pumping\n"))
# supervision_degree = input("")
    aggregate_type = int(input(
        "Enter aggregate type option: \n1. Crushed angular \n2.Sub angular aggregate \n3.Gravel with some crushed particles \n4.Rounded gravel\n"))
    max_cement_content = int(
        input("Enter the maximum cement content(kg/m3): "))
    chemical_admixture = int(input(
        "Enter Chemical admixture option: \n1. Superplasticizer \n2. No Chemical admixture used \n"))
    if chemical_admixture == 1:
        sg_chemical_admixture = float(
            input("Enter the Specific gravity of chemical admixture:"))
        percent_chemical_admixture = float(
            input("Enter water content reductiom due to chemical admixture:"))

    sg_cement = float(input("Enter the specific gravity of cement:"))
    mineral_admixture = int(input(
        "Enter Mineral admixture option: \n1. Fly Ash \n2. GGBS \n3. No mineral admixture used \n"))
    percent_mineral_admixture = 0
    if mineral_admixture == 1:
        sg_mineral_admixture = float(
            input("Enter the specific gravity of fly ash:"))
        percent_mineral_admixture = float(
            input("Enter the percentage of Fly Ash of total cementatious material content:"))
    elif mineral_admixture == 2:
        sg_mineral_admixture = float(
            input("Enter the specific gravity of GGBS:"))
        percent_mineral_admixture = float(
            input("Enter the percentage of GGBS of total cementatious material content:"))
    else:
        sg_mineral_admixture = 0
        percent_mineral_admixture = 0
    sg_ca = float(input("Enter the specific gravity of Course Aggregate:"))
    sg_fa = float(input("Enter the Specific Gravity of Fine Aggregate:"))
    sg_water = float(input("Enter the Specific Gravity of Water:"))
# sg_ggbs = input("")
# wa_ca = input("")
# wa_fa = input("")
    sa_ca = float(input(
        "Enter the zone of Fine Aggregate: \n1. Zone I \n2. Zone II \n3. Zone III \n4. Zone IV\n"))
# sa_fa = int(input(""))
    return grade, cement_type, max_aggregate_size, slump, concrete_type, exposure_condition, concrete_placing, aggregate_type, max_cement_content, chemical_admixture, sg_chemical_admixture, percent_chemical_admixture, sg_cement, mineral_admixture, sg_mineral_admixture, percent_mineral_admixture, sg_ca, sg_fa, sg_water, sa_ca


def f_standard_deviation(compressive_strength):
    if compressive_strength in (10, 15):
        standard_deviation = 3.5
    elif compressive_strength in (20, 25):
        standard_deviation = 4.0
    elif compressive_strength in (30, 35, 40, 45, 50, 55, 60):
        standard_deviation = 5.0
    elif compressive_strength in (65, 70, 75, 80):
        standard_deviation = 6.0

    return standard_deviation


def f_vol_ca(sa_ca, max_aggregate_size):
    if sa_ca == 1:
        if max_aggregate_size == 10:
            vol_ca = 0.44
        elif max_aggregate_size == 20:
            vol_ca = 0.60
        elif max_aggregate_size == 40:
            vol_ca = 0.69
        else:
            print("Enter Valid Nominal Maximum Size of Aggregate")
    elif sa_ca == 2:
        if max_aggregate_size == 10:
            vol_ca = 0.46
        elif max_aggregate_size == 20:
            vol_ca = 0.62
        elif max_aggregate_size == 40:
            vol_ca = 0.71
        else:
            print("Enter Valid Nominal Maximum Size of Aggregate")
    elif sa_ca == 3:
        if max_aggregate_size == 10:
            vol_ca = 0.48
        elif max_aggregate_size == 20:
            vol_ca = 0.64
        elif max_aggregate_size == 40:
            vol_ca = 0.73
        else:
            print("Enter Valid Nominal Maximum Size of Aggregate")
    elif sa_ca == 4:
        if max_aggregate_size == 10:
            vol_ca = 0.50
        elif max_aggregate_size == 20:
            vol_ca = 0.66
        elif max_aggregate_size == 40:
            vol_ca = 0.75
        else:
            print("Enter Valid Nominal Maximum Size of Aggregate")
    else:
        print("Enter the valid Nominal Maximum Size of Aggregate")

    return vol_ca


concrete_type = 1
exposure_condition = 1
min_cement_content = 0
max_wc_ratio = 0


def f_table_5(concrete_type, exposure_condition):
    if concrete_type == 1:
        if exposure_condition == 1:
            min_cement_content = 220
            max_wc_ratio = 0.60
        elif exposure_condition == 2:
            min_cement_content = 240
            max_wc_ratio = 0.60
        elif exposure_condition == 3:
            min_cement_content = 250
            max_wc_ratio = 0.50
        elif exposure_condition == 4:
            min_cement_content = 260
            max_wc_ratio = 0.45
        elif exposure_condition == 5:
            min_cement_content = 280
            max_wc_ratio = 0.40
    elif concrete_type == 2:
        if exposure_condition == 1:
            min_cement_content = 300
            max_wc_ratio = 0.55
        elif exposure_condition == 2:
            min_cement_content = 300
            max_wc_ratio = 0.50
        elif exposure_condition == 3:
            min_cement_content = 320
            max_wc_ratio = 0.45
        elif exposure_condition == 4:
            min_cement_content = 340
            max_wc_ratio = 0.45
        elif exposure_condition == 5:
            min_cement_content = 360
            max_wc_ratio = 0.40

    return min_cement_content, max_wc_ratio
