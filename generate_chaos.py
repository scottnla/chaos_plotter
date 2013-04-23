"""
Title:
Description:
Usage:
Date Started:
Last Modified:
http://asymptoticdesign.wordpress.com/
This work is licensed under a Creative Commons 3.0 License.
(Attribution - NonCommerical - ShareAlike)
http:#creativecommons.org/licenses/by-nc-sa/3.0/

In summary, you are free to copy, distribute, edit, and remix the work.
Under the conditions that you attribute the work to the author, it is for
noncommercial purposes, and if you build upon this work or otherwise alter
it, you may only distribute the resulting work under this license.

Of course, these permissions may be waived with permission from the author.

Description of Usage:
scottnla@faraday-cage:~/$ python readSerial.py [filename]
Reads serial information from an arduino circuit, writes it to file.
"""
import scipy
import random
import sys

filename = sys.argv[1]
maxIterations = int(sys.argv[2])

parameterFile = open(filename, 'r')
params = []

for line in parameterFile:
	params.append(float(line.split()[1]))

seed = complex(0.1,0.3214)

nextPt = lambda z, params: params[1] + 1.0j*params[5]  + params[2]*z*z.conjugate() + params[3]*z*(z.real)**int(params[0]) + params[4]*(z.conjugate())**int(params[0]-1)

counter = 0;

outputFile = filename.rsplit(".",1)[0] 
output = open(outputFile + '.out', 'w')
output.write(str(seed.real) + "\t" + str(seed.imag) + "\n")

while(counter < maxIterations):
	seed = nextPt(seed, params)
	seed = complex(round(seed.real, 3), round(seed.imag, 3))
	output.write(str(seed.real) + "\t" + str(seed.imag) + "\n")
	counter += 1

output.close()
