import matplotlib.pyplot as plt
import pandas as pd
import sys, getopt


def plottyMcPlotface(argv):

	inputfile = ''
	outputfile = ''
    
	try:
		opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
	except getopt.GetoptError:
		print( 'test.py -i <inputfile> -o <outputfile>')
		sys.exit(2)
        
	for opt, arg in opts:
		if opt == '-h':
			print ('test.py -i <inputfile> -o <outputfile>')
			sys.exit()
		elif opt in ("-i", "--ifile"):
			inputfile = arg
		elif opt in ("-o", "--ofile"):
			outputfile = arg

	with open(inputfile) as f:
    
		data = pd.read_table(f, sep=" ", index_col=0, skipfooter=2)
		index = data.index
		precision = data[:]['Precesion']
		recall = data[:]['Recall']
		avg_precision = data[:]['Avg_Precesion']
		avg_recall = data[:]['Avg_Recall']

	fig, ax = plt.subplots()
	ax.plot(index, precision, 'b', label='precision')
	ax.plot(index, recall, 'g', label='recall' )
	ax.plot(index, avg_precision, 'y', label='average precision')
	ax.plot(index, avg_recall, 'r', label= 'average recall')
	ax.set(xlabel='index', ylabel='value', title='TOPO')
	ax.grid()
	plt.legend()

	#fig.savefig(outputfile)
	plt.show()
	     
   
plottyMcPlotface(sys.argv[1:])

