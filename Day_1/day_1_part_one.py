ac = 0

infile = open('input_file.txt', 'r')

for line in infile:
	tamLine = len(line)

	for i in range(tamLine):

		if int(line[i]) == int(line[(i+1)%tamLine]):
			ac = ac + int(line[i])

infile.close()


outfile = open('output_file.txt', 'w')
outfile.write(str(ac))
outfile.close()