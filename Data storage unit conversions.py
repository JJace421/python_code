measurement = float(input("Measurement: "))
unit = input("Measurement unit: ")
converted_unit = input("Conversion unit: ")

units = ['bit','byte','kilobyte','megabyte','gigabyte','terabyte','pentabyte']

if unit in units:
    index1 = units.index(unit)
else:
    print("Retype the unit.")


if converted_unit in units:
    index2 = units.index(converted_unit)
else:
    print("Retype the conversion unit.")


if index1 and index2 != 0:
    num = index1 - index2
    if num > 0:
        measurement *= 1024**num
        print(measurement,converted_unit)
    else:
        measurement /= 1024**(-num)
        print(measurement,converted_unit)
else:
    if index1 == 0:
        index1 = 1 
        num = index1 - index2
        measurement /= (1024**(-num) * 8)
        print(measurement,converted_unit)
    elif index2 == 0:
        index2 = 1
        num = index1 - index2
        measurement *= (1024**num) * 8
        print(measurement,converted_unit)
