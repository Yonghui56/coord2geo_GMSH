# Python Program for quick gmsh grid gen

import string,sys

def convert_pts_togmsh(filename,outputname,startpoint):
	
	# Read in data using this bit
	fin=open(filename, 'r')
	i=0
	x = []; y = []; z = [];
	
	lines = fin.readlines()

	for line in lines:
		# comments indicated by #
		if line[0] != '#' or line[0] != '':
			i=i+1
			data = str.split(line)
			x.append(float(data[0]))
			y.append(float(data[1]))
			z.append(float(data[2]))

			n_lines = int(i)

	# Write data out with this;

	fout = open(outputname,'w')

	lc_name = "%s_lc" % filename[0:3]
	# Format
	# Point(1) = {0, 0, 0, lc};
	fout.write("%s = 0.005;\n" % lc_name)
	j = startpoint
	for i in range(n_lines):
		outputline  = "Point(%i) = { %8.8f, %8.8f, %8.8f, %s};\n " \
					      % (j,x[i],y[i],z[i],lc_name )
		j = j + 1
		fout.write(outputline)

	# gmsh bspline format	
	# Write out splinefit line
	fout.write("Spline(%i) = {%i:%i};\n" \
		   % (startpoint,startpoint,startpoint+n_lines-1))
	fout.close
	fin.close
	
def main():
  inputfile = sys.argv[1]
  convert_pts_togmsh(inputfile,inputfile+".geo",1)

if __name__ == "__main__":
    main()
