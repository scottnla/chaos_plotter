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
import pylab
import sys

filename = sys.argv[1]
width = int(sys.argv[2])
height = int(sys.argv[3])

#load list of 2d points
raw_data = scipy.loadtxt(filename)

#scale the data
scale = scipy.array([width/2.0, height/2.0])
output = scipy.multiply(raw_data, scale)

#bin the data
output = scipy.floor(output)

#histogram it
nx = range(-width/2,width/2)
ny = range(-height/2,height/2)
output = scipy.histogramdd(output,[nx,ny])[0]
output = scipy.transpose(output)

outputFile = filename.rsplit(".",1)[0] + '.dat'
scipy.savetxt(outputFile, output)
