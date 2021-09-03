# OMPORT MODULES
import csv

# READ THE CSV
rows = []

with open("stars.csv",'r') as f:
    csvreader = csv.reader(f)
    for row in csvreader:
        rows.append(row)

headers = rows[0]
star_data = rows[1:]
print(headers)
print(star_data)

# CONVERT STAR SOLAR MASS INTO SI UNIT OR KILOGRAM
star_solar_mass_si_unit = []

for index,solar_mass in enumerate(star_data[6]):
    si_unit = float(solar_mass[index])*1.989e+30
    star_solar_mass_si_unit.append(si_unit)

print(star_solar_mass_si_unit)

# CONVERT STAR SOLAR RADIUS INTO SI UNIT OR METERS
star_solar_radius_si_unit = []

for index,solar_radius in enumerate(star_data[7]):
    si_unit = float(solar_radius[index])* 6.957e+8
    star_solar_radius_si_unit.append(si_unit)

print(star_solar_radius_si_unit)