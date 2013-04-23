chaos_plotter
=============

Python script for computing and plotting chaotic dynamic systems.

To run:

1. create a text file with parameters (copy and modify one of the existing .config files)
2. python generate_chaos.py [config file path] [number of iterations] to generate the .out file of raw datapoints
3. python clean_output.py [.out file path] [image width] [image height] creates the binned 2d array.
4. use pylab.imshow() to plot the 2d array.
