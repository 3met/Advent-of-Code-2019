# Emet Behrendt

def calculate_fuel(mass):
	return int(mass/3) - 2		# int() rounds down

def main():
	with open('inputs.txt', 'r') as file:
		inputs = file.read().split('\n')

	total_rocket_fuel = 0
	for mass in inputs:
		# Calculates initial fuel for module
		total_module_fuel = calculate_fuel(int(mass))
		# Calculates initial fuel for fuel
		fuel_for_fuel = calculate_fuel(total_module_fuel)

		if fuel_for_fuel > 0:
			total_module_fuel += fuel_for_fuel
			while True:
				fuel_for_fuel = calculate_fuel(fuel_for_fuel)
				if fuel_for_fuel > 0:
					total_module_fuel += fuel_for_fuel
				else:
					break

		total_rocket_fuel += total_module_fuel

	print(total_rocket_fuel)

if __name__ == "__main__":
	main()