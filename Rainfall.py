inches_str = input("How many inches of rain have fallen: ")
inches_int = int(inches_str)
inches_float = float(inches_str)

volume_int = (inches_int / 12) * 43560
gallons_int = volume_int * 7.48051945
volume_float = (inches_float / 12) * 43560
gallons_float = volume_float * 7.48051945

print(inches_int, 'in. rain on 1 acre is ', int(gallons_int), 'gallons') 
print(inches_float, 'in. rain on 1 acre is ', float(gallons_float), 'gallons') 
