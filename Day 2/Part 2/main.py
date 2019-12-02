# AOC Day 2, Part 2
# By Emet Behrendt

original_intcode = (1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,1,10,19,1,19,5,23,1,6,23,27,1,27,5,31,2,31,10,35,2,35,6,39,1,39,5,43,2,43,9,47,1,47,6,51,1,13,51,55,2,9,55,59,1,59,13,63,1,6,63,67,2,67,10,71,1,9,71,75,2,75,6,79,1,79,5,83,1,83,5,87,2,9,87,91,2,9,91,95,1,95,10,99,1,9,99,103,2,103,6,107,2,9,107,111,1,111,5,115,2,6,115,119,1,5,119,123,1,123,2,127,1,127,9,0,99,2,0,14,0)

def main():
	for noun in range(0, 100):
		for verb in range(0, 100):
			intcode = list(original_intcode)
			intcode[1] = noun
			intcode[2] = verb
			index = 0

			while True:
				if intcode[index] == 99:
					break
				
				int_1 = intcode[intcode[index+1]]
				int_2 = intcode[intcode[index+2]]

				if intcode[index] == 1:
					result = int_1 + int_2
				elif intcode[index] == 2:
					result = int_1 * int_2
				else:
					print(f"ERROR. Opcode is {intcode[index]}.")
					return

				intcode[intcode[index+3]] = result

				index += 4
			
			if intcode[0] == 19690720:
				print(noun, verb)
				print(100 * noun + verb)
				return

if __name__ == "__main__":
	main()
