# Emet Behrendt

def calculate_fuel(mass):
	return int(mass/3) - 2		# int() rounds down

def main():
	with open('inputs.txt', 'r') as file:
		inputs = file.read().split('\n')

	total_fuel = 0
	for mass in inputs:
		total_fuel += calculate_fuel(int(mass))

	print(total_fuel)

if __name__ == "__main__":
	main()