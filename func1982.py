def f_input():
    grade = input("Enter the Grade of concrete to be designed(ex:M25) : ")
    # cement_type = input("")
    aggregate_type = int(input(
        "Enter aggregate type option: \n1. Crushed angular \n2.Rounded aggregate\n"))
    max_aggregate_size = int(
        input("Enter Valid Nominal Maximum Size of Aggregate(10mm,20mm,40mm) :"))
    compacting_factor = float(
        input("Enter degree of workability(compacting factor):"))
    quality_control = int(
        input(
            "Enter Degree of Quality Control from options:\n1.Very Good \n2.Good \n3.Fair\n"
        ))
    exposure_condition = int(
        input(
            "Enter Exposure condition option: \n1. Mild \n2.Moderate \n3.Severe \n4.Very Severe \n5.Extreme \n"
        ))
    sg_cement = float(input("Enter the specific gravity of cement:"))
    sg_ca = float(input("Enter the specific gravity of Course Aggregate:"))
    sg_fa = float(input("Enter the Specific Gravity of Fine Aggregate:"))
    sg_water = float(input("Enter the Specific Gravity of Water:"))
    sa_fa = float(
        input(
            "Enter the zone of Fine Aggregate: \n1. Zone I \n2. Zone II \n3. Zone III \n4. Zone IV\n"
        ))
    return grade, aggregate_type, max_aggregate_size, compacting_factor, quality_control, exposure_condition, sg_cement, sg_ca, sg_fa, sg_water, sa_fa


def f_standard_deviation(compressive_strength, quality_control):
    if compressive_strength == 10:
        if quality_control == 1:
            standard_deviation = 2
        elif quality_control == 2:
            standard_deviation = 2.3
        elif quality_control == 3:
            standard_deviation = 3.3
    elif compressive_strength == 15:
        if quality_control == 1:
            standard_deviation = 2.5
        elif quality_control == 2:
            standard_deviation = 3.5
        elif quality_control == 3:
            standard_deviation = 4.5
    elif compressive_strength == 20:
        if quality_control == 1:
            standard_deviation = 3.6
        elif quality_control == 2:
            standard_deviation = 4.6
        elif quality_control == 3:
            standard_deviation = 5.6
    elif compressive_strength == 25:
        if quality_control == 1:
            standard_deviation = 4.3
        elif quality_control == 2:
            standard_deviation = 5.3
        elif quality_control == 3:
            standard_deviation = 6.3
    elif compressive_strength == 30:
        if quality_control == 1:
            standard_deviation = 5
        elif quality_control == 2:
            standard_deviation = 6
        elif quality_control == 3:
            standard_deviation = 7
    elif compressive_strength == 35:
        if quality_control == 1:
            standard_deviation = 5.3
        elif quality_control == 2:
            standard_deviation = 6.3
        elif quality_control == 3:
            standard_deviation = 7.3
    elif compressive_strength == 40:
        if quality_control == 1:
            standard_deviation = 5.6
        elif quality_control == 2:
            standard_deviation = 6.6
        elif quality_control == 3:
            standard_deviation = 7.6
    elif compressive_strength == 45:
        if quality_control == 1:
            standard_deviation = 6
        elif quality_control == 2:
            standard_deviation = 7
        elif quality_control == 3:
            standard_deviation = 8
    elif compressive_strength == 50:
        if quality_control == 1:
            standard_deviation = 6.4
        elif quality_control == 2:
            standard_deviation = 7.4
        elif quality_control == 3:
            standard_deviation = 8.4
    elif compressive_strength == 55:
        if quality_control == 1:
            standard_deviation = 6.7
        elif quality_control == 2:
            standard_deviation = 7.7
        elif quality_control == 3:
            standard_deviation = 8.7
    elif compressive_strength == 60:
        if quality_control == 1:
            standard_deviation = 6.8
        elif quality_control == 2:
            standard_deviation = 7.8
        elif quality_control == 3:
            standard_deviation = 8.8

    return standard_deviation
