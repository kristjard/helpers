import pickle 
import sys, getopt
from typing import Protocol

def depickler_pickler(argv):
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
   data = pickle.load(open(inputfile, 'rb'))
   pic_data = pickle.dump(data, open(outputfile, 'wb'), protocol=0)
   
   
depickler_pickler(sys.argv[1:])
   

