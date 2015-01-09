# ######################################################
# Mike Libassi
# 2015
# to process cProfile csv output this will scrub the
# commas out of the filename:lineno(function) column
# this allows to import into R 
#
# input: file name in local directory
# output: the file name with 'scrubbed.csv' appended
#
# #####################################################

import sys

print ("Input file name?")
infile=raw_input("file: ")

#infile= 'localhost-boolsfp-test1.csv'
outfile = infile+'scrubbed.csv'

fo = open(outfile, "wb")

with open(infile) as fi:
  for line in fi:
    print "Input line"
    print line #str
    newlinea = line.replace(",'", "-")
    newlineb = newlinea.replace("',", "-")
    print "Cleaned Line"
    print newlineb
    fo.write(newlineb)
        

fi.close()
fo.close()
