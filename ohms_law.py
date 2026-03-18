# Author: Steve Hauswirth
# Date: 2025-10-12
# Last Modified: 2025-10-16
# Description: Ohm's Law Calculator using match-case structure in Python.

# Main menu for user to select which variable to calculate.
menu = ''' [1] Current
 [2] Voltage
 [3] Resistance
 [4] Power'''

print("Ohm's Law Calculator")
print(menu)
print()

# Get user input for variable to calculate.
choice = int(input("Choose a variable to calculate: "))

# Function to format and print values in appropriate whole number SI units.
def format_and_print_si_units(value, unit):
    if 1 > value >= 0.001:
        value = value * 1_000
        print(f"{unit} = {value:.3f} m{unit}")
    elif 0.001 > value >= 0.000_001:
        value = value * 1_000_000
        print(f"{unit} = {value:.3f} µ{unit}")
    elif 0.000_001 > value >= 0.000_000_001:
        value = value * 1_000_000_000
        print(f"{unit} = {value:.3f} n{unit}")
    elif 0.000_000_001 > value >=0.000_000_000_001:
        value = value * 1_000_000_000_000
        print(f"{unit} = {value:.3f} p{unit}")
    else:
        print(f"{unit} = {value:.3f} {unit}")

# Use match-case to determine which variable to calculate based on user input.
match choice:
    case 1:
        voltage = float(input("Enter Voltage (V): "))
        resistance = float(input("Enter Resistance (R): "))
        current = voltage / resistance
        format_and_print_si_units(current, "A")
        
    case 2:
        current = float(input("Enter Current (I): "))
        resistance = float(input("Enter Resistance (R): "))
        voltage = current * resistance
        format_and_print_si_units(voltage, "V")
            
    case 3:
        voltage = float(input("Enter Voltage (V): "))
        current = float(input("Enter Current (I): "))
        resistance = voltage / current
        format_and_print_si_units(resistance, "Ω")
      
    case 4:
        voltage = float(input("Enter Voltage (V): "))
        current = float(input("Enter Current (I): "))
        power = voltage * current
        format_and_print_si_units(power, "W")
    
    case _:
        print("Invalid choice. Please select a number between 1 and 4.")
